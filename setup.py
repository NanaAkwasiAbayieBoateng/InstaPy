from setuptools import setup

__version__ = '0.0.1'
__author__ = 'Tim Grossmann'

requirements = [
    'selenium==2.53.6',
    'clarifai==2.0.31',
    'pyvirtualdisplay',
    'emoji'
]

description = 'Instagram Like, Comment and Follow Automation Script'

setup(
    name='instagram_sion_',
    version=__version__,
    author=__author__,
    author_email='SC@SC.SC',
    url='www.bomb.com',
    py_modules='instapy',
    description=description,
    install_requires=requirements
)
