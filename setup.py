"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='electronut-circuitpython-ili9163',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='displayio driver for ILI9163 TFT-LCD displays.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://github.com/electronut/Electronutlabs_CircuitPython_ILI9163',

    # Author details
    author='Electronut Labs',
    author_email='tavish@electronut.in',

    install_requires=[
        'Adafruit-Blinka',
    ],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='adafruit blinka circuitpython micropython ili9163 displayio',

    py_modules=['electronutlabs_ili9163'],
)
