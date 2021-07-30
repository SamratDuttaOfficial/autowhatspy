'''
Made by: Samrat Dutta
LinkedIn: https://www.linkedin.com/in/samratduttaofficial
Github: https://github.com/SamratDuttaOfficial

This script can be used to send messages in groups you are a member of.
This script can also be used to send messages to people you are already talking to on WhatsApp.
If a number is in contacts but you are not talking to him/her on WhatsApp, you can't use this script.
For that purpose, use the message_to_unsaved_numbers.py script

NOTE: Open firefox. GO to about:profiles and make a new profile.
Save it in this directory, with whatever name firefox assigns it.
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


def message_to_contacts(msg, contacts, gechodriver, gechodriver_log, user_profile, image=None):
    try:
        with open(contacts, 'r', encoding='utf8') as f:
            groups = [group.strip() for group in f.readlines()]
    except FileNotFoundError:
        print('ERROR: Please provide a proper path of the groups/contacts list file. '
              'Make sure the file contains all the contacts/groups in different lines.')
        exit(0)
    except:
        print('The file content for list of groups should be like this:\n'
              'Group1\n'
              'Group2\n'
              'Group3\n'
              'Another Group\n'
              'Group 5\n')
        print('The file content for list of contacts should be like this:\n'
              'Samrat Dutta\n'
              'Abraham Lincoln\n'
              'Sachin\n'
              'Sourav\n'
              'Mr. Das\n')
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
    browser.get('https://web.whatsapp.com/')
    print("Browser Opened")
    print("Message to be sent:\n" + msg_text)

    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    try:
        search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
        print('Found SearchBox')
    except TimeoutException:
        print('SearchBox not found! Check if you are logged in to WhatsApp from the Firefox profile.')
        exit(0)
    except:
        print('Some error occurred while finding SearchBox')
        exit(0)

    for group in groups:
        search_box.clear()
        search_box.send_keys(group)
        # We could have also done pyperclip.copy(group) and then search_box.send_keys(Keys.SHIFT, Keys.INSERT)
        time.sleep(2)
        group_xpath = f'//span[@title="{group}"]'

        try:
            group_title = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, group_xpath)))
            # Wait some seconds to find the group title.
            # If not found within that time, declare that the group/contact does not exist and continue.
            # Here we are waiting for 25 seconds.
        except TimeoutException:
            print('Group/Contact not found: ' + group)
            print('Check the Group/Contact name. Also check the internet connection on your phone and PC.')
            continue
        except:
            print('Some error occurred while sending the message to the contact/group ' + group)
            continue

        group_title.click()
        time.sleep(1)

        input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
        try:
            input_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            input_box.send_keys(msg_text)
            # We were using pyperclip.copy(msg_text) and then pasting here, but it did not work in headless mode.
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
                    print("Message sent to " + group)
                    break
                time.sleep(5)
            if sent_pending is not None:
                print("Timeout! Maximum waiting time (125 seconds) are over and the message could not be sent. "
                      "Please check your internet connection and the length of the message. "
                      "Error occurred for contact/group " + group)

        except TimeoutException:
            print('InputBox not found! Please check the internet connection on your phone and PC.')
        except:
            print('An error occurred while sending the message to ' + group)

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
                        print("Image/video sent to " + group)
                        break
                    time.sleep(5)
                if sent_pending is not None:
                    print("Timeout! Maximum waiting time (125 seconds) are over and the image/video could not be sent."
                          " Please check your internet connection or use a smaller file. Timeout occurred for " + group)
            except NoSuchElementException:
                print('Error: Unable to locate some elements for the contact/group ' + group)
                pass
            except:
                print("Some error occurred while sending the image/video to " + group)
                pass

    time.sleep(10)  # Giving some time to the msgs to be sent, for slow connections.
    browser.close()
    print("Browser Closed")


def message_to_groups(msg, groups, gechodriver, gechodriver_log, user_profile, image=None):
    message_to_contacts(msg, groups, gechodriver, gechodriver_log, user_profile, image)
    # This function just calls the above function LOL.
