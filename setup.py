#!/usr/bin/env python3
"""
Setup script for Workerssal Mail Service
"""

from setuptools import setup, find_packages

setup(
    name="wssal-mail-service",
    version="1.0.0",
    description="Automated Email Marketing Tool for Brands & Influencers",
    author="Workerssal",
    author_email="official@workerssal.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "colorama>=0.4.4",
        "pandas>=1.3.0",
        "openpyxl>=3.0.7",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "wssal-mail-service=wssal_mail_service:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
) 