from setuptools import setup, find_packages

setup(
    name = 'fbmsgbot',
    packages = find_packages(exclude=['tests*']),
    version = '0.1.8',
    description = 'Python bot for Facebook Messenger',
    author = 'Benjamin Cunningham & Austin Hendy',
    author_email = 'bencunningham17@gmail.com',
    url = 'https://github.com/ben-cunningham/pybot',
    download_url = 'https://github.com/ben-cunningham/pybot/tarball/0.1.8',
    classifiers = [],
)