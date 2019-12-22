# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:04:38 2015

@author: linuxfreebird
"""

from distutils.core import setup, Extension
#import numpy.distutils.misc_util
 
c_ext = Extension("_fstoh", sources=["_fstoh.cpp"],
  language='c++',extra_compile_args=["-std=c++11"])
 
setup(
    ext_modules=[c_ext],
#    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
)
