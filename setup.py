import pathlib
from setuptools import setup

# The directory containing this file
PATH = pathlib.Path(__file__).parent


def readme() -> str:
    with open(r'README.md', encoding="utf8") as f:
        README = f.read()
    return README


# This call to setup() does all the work
setup(
    name="autowhatspy",
    version="1.0.7",
    description="WhatsApp and Email Automation with Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords=['autowhatspy', 'whatsapp', 'email', 'web', 'bulk messaging'],
    url="https://github.com/SamratDuttaOfficial/autowhatspy",
    download_url="https://github.com/SamratDuttaOfficial/autowhatspy/blob/main/dist/autowhatspy-1.0.7.tar.gz",
    author="Samrat Dutta",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["autowhatspy"],
    include_package_data=True,
    install_requires=["selenium", "pyperclip"],
)