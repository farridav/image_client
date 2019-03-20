#!/usr/bin/env python3

from setuptools import setup

setup(
    name='image-client',
    packages=['image_client'],
    version='1.0.0',
    url='https://github.com/farridav/image_client.git',
    author='David Farrington',
    author_email='david@shipit.ltd',
    description='Image Manipulation tool',
    long_description='Image Manipulation tool',
    install_requires=[
        'Pillow==5.4.1'
    ],
    extras_require={},
    include_package_data=True,
    platforms='any',
    zip_safe=False
)
