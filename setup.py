#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'txstate-taiga-contrib-ldap-auth',
    version = ":versiontools:txstate_taiga_contrib_ldap_auth:",
    description = "TxState adaptation of the Taiga plugin for ldap authentication",
    long_description = "",
    keywords = 'txstate taiga',
    author = 'Andrew Thyng',
    author_email = 'ajt79@txstate.edu',
    url = 'https://github.com/txstate-etc/txstate-taiga-contrib-ldap-auth/tree/master/txstate_taiga_contrib_ldap_auth',
    license = 'AGPL',
    include_package_data = True,
    packages = ['txstate_taiga_contrib_ldap_auth'],
    install_requires=[
        'django >= 1.7',
		'ldap3 >= 0.9.8.4'
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
