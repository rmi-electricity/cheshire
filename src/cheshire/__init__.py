"""A template repository for a Python package created by Catalyst Cooperative."""
import logging

import pkg_resources

# In order for the package modules to be available when you import the package,
# they need to be imported here somehow. Not sure if this is best practice though.
import cheshire.cli
import cheshire.dummy  # noqa: F401

__author__ = "RMI"
__contact__ = "...@rmi.org"
__maintainer__ = "Cheshire Cat"
__license__ = "BSD 3-Clause License"
__maintainer_email__ = "...@rmi.org"
__version__ = pkg_resources.get_distribution("rmi.cheshire").version
__docformat__ = "restructuredtext en"
__description__ = "A template for Python package repositories."
__long_description__ = """
This should be a paragraph long description of what the package does.
"""
__projecturl__ = "https://github.com/rmi-electricity/cheshire"
__downloadurl__ = "https://github.com/rmi-electricity/cheshire"

# Create a root logger for use anywhere within the package.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
