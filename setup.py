#!/usr/bin/env python

from setuptools import setup

setup(
    name='YourAppName',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    dependency_links = ['https://www.djangoproject.com/download/1.7c1/tarball#egg=django-1.7rc1'],
    install_requires=['Django==1.7rc1'],
)
