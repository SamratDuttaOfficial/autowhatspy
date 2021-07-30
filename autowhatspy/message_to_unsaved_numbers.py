'''
Made by: Samrat Dutta
LinkedIn: https://www.linkedin.com/in/samratduttaofficial
Github: https://github.com/SamratDuttaOfficial

This script can be used to send messages to numbers.
This script can also be used to send messages to people you are already not talking to on WhatsApp.
If a number is already in your contacts and you are talking to them, use the message_to_groups_or_contacts.py script.

NOTE: Open firefox. GO to about:profiles and make a new profile.
Save it in your project directory with whatever name firefox assigns it.
Open that profile, open web.whatsapp.com and scan QR.
Now the path of the profile is sent as a parameter of the functions below.
'''

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options


def message_to_numbers(msg, numbers_list, gechodriver, gechodriver_log, user_profile, country_code, image=None):
    try:
        with open(numbers_list, 'r', encoding='utf8') as f:
            numbers = [number.strip() for number in f.readlines()]
    except FileNotFoundError:
        print('ERROR: Please provide a proper path of the numbers list file. '
              'Make sure the file contains all the numbers in different lines.')
        exit(0)
    except:
        print('The file content should will be like this:\n'
              '9198xxxxxx56\n'
              '96xxxxxx23\n'
              '94xxxxxx56\n'
              '9178xxxxxx65\n')
        exit(0)

    try:
        with open(msg, 'r', encoding='utf8') as f:
            msg_text = f.read()
    except FileNotFoundError:
        print('ERROR: Please provide a proper path of the message text file.')
        exit(0)
    except:
        print('An error occurred reading the message text file.')
        exit(0)

    options = Options()
    options.headless = True
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_profile = webdriver.FirefoxProfile(user_profile)

    try:
        browser = webdriver.Firefox(executable_path=gechodriver, options=options, capabilities=firefox_capabilities,
                                    service_log_path=gechodriver_log, firefox_profile=firefox_profile)
    except WebDriverException:
        browser = webdriver.Firefox(options=options, capabilities=firefox_capabilities,
                                    service_log_path=gechodriver_log, firefox_profile=firefox_profile)

    browser.maximize_window()
    print("Browser Opened")
    print("Message to be sent:\n" + msg_text)

    for number in numbers:
        if (len(number) == 10):
            # This formatted the number in a proper way.
            number = str(country_code) + number
        if ((len(number) < 10) | (len(number) == 11) | (len(number) > 12)):
            # Number too small or too big. Invalid number.
            print("Invalid Number: " + number)
            continue

        browser.get('https://web.whatsapp.com/send?phone=' + number)

        input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
        try:
            input_box = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            # Wait some seconds to find the input box.
            # If not found within that time, declare that the number does not exist and continue.
            # Here we are waiting for 25 seconds.
        except TimeoutException:
            print("Number not found: " + number)
            print('Check the number. Also check the internet connection on your phone and PC.')
            continue
        except:
            print('Some error occurred while sending the message to the number ' + number)
            continue

        try:
            input_box.send_keys(msg_text)
            # We were using pyperclip.copy(msg) and then pasting here, but it did not work in headless mode.
            # No idea why.
            input_box.send_keys(Keys.ENTER)

            sent_pending_xpath = '//span[@aria-label=" Pending "]'
            # First wait till sent_pending is found at least once.
            sent_pending = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.XPATH, sent_pending_xpath)))
            for i in range(0, 24):
                try:
                    sent_pending = browser.find_element_by_xpath(sent_pending_xpath)
                except:
                    sent_pending = None
                    print("Message sent to " + number)
                    break
                time.sleep(5)
            if sent_pending is not None:
                print("Timeout! Maximum waiting time (125 seconds) are over and the message could not be sent. "
                      "Please check your internet connection and the length of the message. "
                      "Error occurred for number " + number)

        except:
            print('Some error occurred while sending the message to ' + number)
            print('Please check the internet connection on your phone and PC')

        if image:
            try:
                attachment_box = browser.find_element_by_xpath('//div[@title="Attach"]')
                attachment_box.click()
                time.sleep(1)

                image_box = browser.find_element_by_xpath(
                    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
                )
                image_box.send_keys(image)
                time.sleep(2)

                send_btn_xpath = '//span[@data-icon="send"]'
                send_btn = WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, send_btn_xpath)))
                send_btn.click()

                sent_pending_xpath = '//span[@aria-label=" Pending "]'
                # First wait till sent_pending is found at least once.
                sent_pending = WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, sent_pending_xpath)))
                for i in range(0, 24):
                    try:
                        sent_pending = browser.find_element_by_xpath(sent_pending_xpath)
                    except:
                        sent_pending = None
                        print("Image/video sent to " + number)
                        break
                    time.sleep(5)
                if sent_pending is not None:
                    print("Timeout! Maximum waiting time (125 seconds) are over and the image/video could not be sent."
                          " Please check your internet connection or use a smaller file. Timeout occurred for " + number)
            except NoSuchElementException:
                print('Error: Unable to locate some elements for the number ' + number)
                pass
            except:
                print("Some error occurred while sending the image/video to " + number)
                pass

    time.sleep(10)  # Giving some time to the msgs to be sent, for slow connections.
    browser.close()
    print("Browser Closed")
