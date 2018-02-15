#!/usr/bin/env python3
from setuptools import Extension
from setuptools import setup

setup(
	name = "helloworld",
	version = "1.0",
	ext_modules = [Extension("helloworld", ["bind.c", "libmypy.c"])]
);
