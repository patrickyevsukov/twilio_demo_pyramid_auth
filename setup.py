# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

import os.path as op

from setuptools import find_packages, setup

from twilio_demo_pyramid_auth import __version__


README = ""
with open(op.join(op.abspath(op.dirname(__file__)), "README.rst")) as r:
    README = r.read()


third_party_dependencies = (
    "pyramid==1.8.3",
    "pyramid_exclog==1.0.0",
    "twilio==6.3.0",
    "waitress==1.0.2",
)


setup(
    name="twilio_demo_pyramid_auth",
    version=__version__,
    description="Demo of Twilio auth with Pyramid",
    long_description=README,
    author="Patrick Yevsukov",
    url="https://patrick.yevsukov.com",
    license="OSI Approved License",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=third_party_dependencies,
    keywords="twilio pyramid auth authentication",
    classifiers=[
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications :: Telephony",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "paste.app_factory": [
            "main = twilio_demo_pyramid_auth.app:main",
        ],
    },
)
