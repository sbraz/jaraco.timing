#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

with open('README.txt') as readme:
	long_description = readme.read()
with open('CHANGES.txt') as changes:
	long_description += '\n\n' + changes.read()

setup_params = dict(
	name='jaraco.timing',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="jaraco.timing",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/jaraco.timing",
	packages=setuptools.find_packages(),
	namespace_packages=['jaraco'],
	setup_requires=[
		'hgtools',
		'pytest-runner',
	],
	tests_require=[
		'pytest',
	],
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
