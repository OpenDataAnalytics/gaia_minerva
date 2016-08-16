"""Main builder script for Gaia."""

import sys
import re
from setuptools import setup, find_packages

with open('README.md') as f:
    desc = f.read()

# parse requirements file
with open('requirements.txt') as f:
    requires = []       # main requirements
    extras = {}         # optional requirements
    current = requires  # current section

    comment = re.compile('(^#.*$|\s+#.*$)')
    v26 = re.compile(r'\s*;\s*python_version\s*<\s*[\'"]2.7[\'"]\s*')
    for line in f.readlines():
        line = line.strip()

        # detect a new optional package section
        if line.startswith('# optional:'):
            package = line.split(':')[1].strip()
            extras[package] = []
            current = extras[package]

        line = comment.sub('', line)
        if not line:
            continue

        if v26.search(line):
            # version 2.6 only
            if sys.version_info[:2] == (2, 6):
                line = v26.sub('', line)
                current.append(line)
        else:
            # all other versions
            current.append(line)

setup(
    name='gaia_minerva',
    version='0.0.1',
    description='Run gaia tasks via minerva analysis and girder jobs',
    long_description=desc,
    author='Gaia and Minerva developers',
    author_email='kitware@kitware.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering'
    ],
    keywords='geospatial GIS workflow data gaia minerva',
    packages=find_packages(exclude=['tests*', 'server*', 'docs']),
    require_python='>=2.6',
    url='https://github.com/OpenDataAnalytics/gaia_minerva',
    extras_require=extras,
    entry_points={
        'gaia.plugins': [
            "gaia_minerva.inputs = girder.plugins.gaia_minerva.inputs",
        ]
    }
)
