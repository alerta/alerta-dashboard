#!/usr/bin/env python

import setuptools

import dashboard

setuptools.setup(
    name="alerta-dashboard",
    version=dashboard.__version__,
    description='Alerta dashboard WSGI application',
    url='https://github.com/alerta/alerta-dashboard',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=[
        'Flask',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'alerta-dashboard = dashboard.dashboard:main'
        ]
    },
    keywords='alerta dashboard wsgi application',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Flask',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring',
    ]
)
