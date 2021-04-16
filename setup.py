# Inspired by the EMPress setup.py file
from setuptools import find_packages, setup

__version__ = "0.0.2"

classifiers = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Intended Audience :: Science/Research
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
    Topic :: Scientific/Engineering :: Bio-Informatics
"""
short_desc = (
    "Framework for differential microbiome abundance using Bayesian "
    "inference"
)

with open('README.md') as f:
    long_description = f.read()

setup(
    name="birdman",
    author="Gibraan Rahman",
    author_email="grahman@eng.ucsd.edu",
    description=short_desc,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gibsramen/BIRDMAn",
    version=__version__,
    license='BSD-3-Clause',
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.stan"]},
    install_requires=[
        "numpy",
        "cmdstanpy",
        "dask[complete]",
        "dask-jobqueue",
        "biom-format",
        "patsy",
        "xarray",
        "pandas",
        "arviz"
    ],
    extras_require={"dev": ["pytest", "scikit-bio", "sphinx"]},
    classifiers=[s.strip() for s in classifiers.split('\n') if s]
)
