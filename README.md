# BIRDMAn

[![GitHub Actions CI](https://github.com/gibsramen/birdman/workflows/BIRDMAn%20CI/badge.svg)](https://github.com/gibsramen/BIRDMAn/actions)
[![Documentation Status](https://readthedocs.org/projects/birdman/badge/?version=stable)](https://birdman.readthedocs.io/en/stable/?badge=stable)
[![PyPI](https://img.shields.io/pypi/v/birdman.svg)](https://pypi.org/project/birdman)

**B**ayesian **I**nferential **R**egression for **D**ifferential **M**icrobiome **An**alysis (**BIRDMAn**) is a framework for performing differential abundance analysis through Bayesian inference.

## Installation

Currently BIRDMAn requires Python 3.7 or higher.

```bash
conda install -c conda-forge dask biom-format patsy xarray
pip install cmdstanpy
pip install git+git://github.com/arviz-devs/arviz.git
pip install birdman
```

You have to install `cmdstan` through the `cmdstanpy.install_cmdstan` function first. See the [CmdStanPy documentation](https://mc-stan.org/cmdstanpy/installation.html#install-cmdstan) for details.

See the [documentation](https://birdman.readthedocs.io/en/stable/?badge=stable) for details on usage.
