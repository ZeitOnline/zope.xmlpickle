##############################################################################
#
# Copyright (c) 2006-2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.xmlpickle package

"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


TESTS_REQUIRE = [
    'zope.testrunner',
]


setup(
    name='zope.xmlpickle',
    version='3.5.0.dev0',
    url='https://github.com/zopefoundation/zope.xmlpickle',
    license='ZPL 2.1',
    description='XML-based Pickling',
    author='Zope Corporation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
    ),
    keywords="zope3 pickle xml",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP'
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
    },
    include_package_data=True,
    zip_safe=False,
 )
