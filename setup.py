# coding: utf-8
from setuptools import find_packages, setup

pkgname = "apc.versionplugin.debianize"

setup(name=pkgname,
      version="0.0.2",
      description="Version Increment Plugin that builds with debianize",
      author="Lars van de Kerkhof",
      author_email="lars@permanentmarkers.nl",
      maintainer="Lars van de Kerkhof",
      maintainer_email="lars@permanentmarkers.nl",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['apc', 'apc.versionplugin'],
      zip_safe=True,
      install_requires=[
          "setuptools",
          "apc.version",
          "apc.versionplugin.default",
      ],
      entry_points={},
)