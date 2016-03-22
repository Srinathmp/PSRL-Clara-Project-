#!/usr/bin/env python

from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension

extensions = Extension('clara.pylpsolve', ['clara/pylpsolve.pyx'],
                       libraries=['lpsolve55'])

setup(name='clara',
      version='1.0',
      description='CLuster And RepAir tool for introductory \
programming assignments',
      author='Ivan Radicek',
      author_email='radicek@forsyte.at',
      url='https://github.com/iradicek/clara',
      packages=['clara'],
      ext_modules = cythonize(extensions),
      install_requires=['pycparser', 'zss'],
      scripts=['bin/clara']
     )