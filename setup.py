#!/usr/bin/env python
import pathlib

import setuptools

from sprockets.mixins import correlation


def read_requirements(name):
    requirements = []
    for line in pathlib.Path('requires', name).read_text().split('\n'):
        if '#' in line:
            line = line[:line.index('#')]
        line = line.strip()
        if line.startswith('-r'):
            requirements.extend(read_requirements(line[2:].strip()))
        elif line and not line.startswith('-'):
            requirements.append(line)
    return requirements


setuptools.setup(
    name='sprockets.mixins.correlation',
    version=correlation.__version__,
    description='Stuff to correlate requests, logs, and the like',
    long_description=pathlib.Path('README.rst').read_text(),
    url='https://github.com/sprockets/sprockets.mixins.correlation.git',
    author='AWeber Communications',
    author_email='api@aweber.com',
    license=pathlib.Path('LICENSE').read_text(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=setuptools.find_packages(),
    namespace_packages=['sprockets'],
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('test-requirements.txt'),
    test_suite='nose.collector',
    zip_safe=True,
    python_requires='>=3.5'
)
