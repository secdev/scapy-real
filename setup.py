#! /usr/bin/env python

"""
Scapy-real: we raise an error and ask people to move away.
"""

import warnings
from setuptools import setup
from setuptools.command.install import install


long_description = """
# Scapy-real is outdated. Please use Scapy instead #

This project only exists for historical reasons, and should
not be used.

Links to scapy:
 - PyPi: https://pypi.org/project/scapy/
 - GitHub: https://github.com/secdev/scapy/
 - Website: https://scapy.net/
"""

class PostInstallCommand(install):
  """Post-installation for installation mode."""

  def run(self):
    pad_desc = "\n" + "\n".join(("#" * 60,)) + "\n"
    raise DeprecationWarning(pad_desc + long_description + pad_desc)


setup(
    name='scapy-real',
    packages=['scapy-real'],
    version='2.3',
    zip_safe=False,
    description='Legacy Scapy - Do not use',
    long_description=long_description,
    author='Philippe BIONDI',
    cmdclass={
        'install': PostInstallCommand,
    },
)
