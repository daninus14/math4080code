from distutils.core import setup, Extension

module1 = Extension("et", sources=["et.c", "gem.c", "gembed.c"])

setup( name="PackageName",
	version = "1.0",
	description = "this is a demo package description",
	ext_modules = [module1]
	)