from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in elifapp/__init__.py
from elifapp import __version__ as version

setup(
	name="elifapp",
	version=version,
	description="Elifapp",
	author="ERPGulf",
	author_email="support@ERPGulf.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
