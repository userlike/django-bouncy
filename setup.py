#!/usr/bin/env python

from setuptools import setup

import os

# import sys
import textwrap

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-bouncy",
    version="0.2.7",
    author="Nick Catalano",
    packages=["django_bouncy", "django_bouncy.migrations", "django_bouncy.tests"],
    url="https://github.com/ofa/django-bouncy",
    description=(
        "A way to handle bounce and abuse reports delivered by Amazon's Simple"
        " Notification Service regarding emails sent by Simple Email Service"
    ),
    long_description=textwrap.dedent(open(os.path.join(ROOT, "README.rst")).read()),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Django>=4.2",
        "python-dateutil>=2.8",
        "cryptography>=39",
        "pem>=21.1.0",
    ],
    keywords="aws ses sns seacucumber boto",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
)
