# Colormap Complex

<p align="center">
  <a href="https://github.com/34j/colormap-complex/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/colormap-complex/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://colormap-complex.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/colormap-complex.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/34j/colormap-complex">
    <img src="https://img.shields.io/codecov/c/github/34j/colormap-complex.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/colormap-complex/">
    <img src="https://img.shields.io/pypi/v/colormap-complex.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/colormap-complex.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/colormap-complex.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://colormap-complex.readthedocs.io" target="_blank">https://colormap-complex.readthedocs.io </a>

**Source Code**: <a href="https://github.com/34j/colormap-complex" target="_blank">https://github.com/34j/colormap-complex </a>

---

Complex / 2d colormap

## Installation

Install this via pip (or your favourite package manager):

```shell
pip install colormap-complex
```

## Usage

```python
from colormap_complex import colormap
import numpy as np

lin = np.linspace(-1, 1, 100)
x, y = np.meshgrid(lin, lin)
z = x + 1j * y
c = colormap(z.real, z.imag, type="oklab", scale=True)
plt.imshow(c, extent=(-1, 1, -1, 1), origin='lower')
```

### All colormaps

![colormaps](https://raw.githubusercontent.com/34j/colormap-complex/main/colormap-all.jpg)

### Examples

![z^(2/3+i)](https://raw.githubusercontent.com/34j/colormap-complex/main/complex-function-z-2-3-i.jpg)
![z^(2/3+i)](https://raw.githubusercontent.com/34j/colormap-complex/main/complex-function-z-2-3-i-cyl.jpg)
![z^(2/3+i)](https://raw.githubusercontent.com/34j/colormap-complex/main/complex-function-z-2-3-i-cyl-magnitude.jpg)

### Description

- `"bremm", "cubediagonal", "schumann", "steiger", "teulingfig2", "ziegler"` colormaps are collected from [spinthil/pycolormap-2d](https://github.com/spinthil/pycolormap-2d) which is based on:
  > M. Steiger, J. Bernard, S. Thum, S. Mittelstädt, M. Hutter, D. A. Keim, and J. Kohlhammer, “Explorative Analysis of 2D Color Maps,” in International Conferences in Central Europe on Computer Graphics, Visualization and Computer Vision, 2015, vol. 23, pp. 151–160.
- Other colormaps are built on top of [colour-science/colour](https://github.com/colour-science/colour) and created by the author.
- `"oklab", "prolab"` are perceptually uniform (lightness) colormaps.
- `"oklch", "prolch"` are perceptually uniform (chroma) colormaps. X axis corresponds to Hue and Y axis to Lightness.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

This package was created with
[Copier](https://copier.readthedocs.io/) and the
[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
project template.
