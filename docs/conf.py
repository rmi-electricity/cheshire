"""Configuration file for the Sphinx documentation builder."""
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import shutil
from datetime import datetime
from pathlib import Path

import pkg_resources
from sphinx.application import Sphinx

DOCS_DIR = Path(__file__).parent.resolve()

# -- Path setup --------------------------------------------------------------
# We are building and installing the pudl package in order to get access to
# the distribution metadata, including an automatically generated version
# number via pkg_resources.get_distribution() so we need more than just an
# importable path.

# The full version, including alpha/beta/rc tags
release = pkg_resources.get_distribution("rmi.cheshire").version

# -- Project information -----------------------------------------------------

project = "New RMI Python Project"
copyright = f"{datetime.today().year}, RMI, CC-BY-4.0"  # noqa: A001
author = "RMI"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "autoapi.extension",
    "sphinx_issues",
]
todo_include_todos = True

# Automatically generate API documentation during the doc build:
autoapi_type = "python"
autoapi_dirs = [
    "../src/cheshire",
]
autoapi_ignore = [
    "*_test.py",
    "*/package_data/*",
]
autoapi_python_class_content = "both"
autodoc_typehints = "description"
# GitHub repo
issues_github_path = "rmi-electricity/cheshire"

# In order to be able to link directly to documentation for other projects,
# we need to define these package to URL mappings:
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "setuptools": ("https://setuptools.pypa.io/en/latest/", None),
    "tox": ("https://tox.wiki/en/latest/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
master_doc = "index"
html_theme = "pydata_sphinx_theme"
# html_logo = "_static/Small_PNG-RMI_logo_PrimaryUse.PNG"
html_icon = "_static/favicon-16x16.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "navigation_with_keys": True,
    "light_logo": "Small_PNG-RMI_logo_PrimaryUse.PNG",
    "dark_logo": "Small_PNG-RMI_logo_PrimaryUse_White_Horizontal.PNG",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Custom build operations -------------------------------------------------
def cleanup_rsts(app: Sphinx, exception: Exception) -> None:
    """Remove generated RST files when the build is finished."""
    (DOCS_DIR / "path/to/temporary/rst/file.rst").unlink()


def cleanup_csv_dir(app: Sphinx, exception: Exception) -> None:
    """Remove generated CSV files when the build is finished."""
    csv_dir = DOCS_DIR / "path/to/temporary/csv/dir/"
    if csv_dir.exists() and csv_dir.is_dir():
        shutil.rmtree(csv_dir)


def setup(app: Sphinx) -> None:
    """Add custom CSS defined in _static/custom.css."""
    app.add_css_file("custom.css")
    # Examples of custom docs build steps:
    # app.connect("build-finished", cleanup_rsts)
    # app.connect("build-finished", cleanup_csv_dir)
