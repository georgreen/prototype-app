# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in data_collection_app/__init__.py
from data_collection_app import __version__ as version

setup(
	name='data_collection_app',
	version=version,
	description='Admin interface for data collection.',
	author='Inquire.Solute',
	author_email='georgreen.ngunga.dev@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
