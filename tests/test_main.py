from collections.abc import Callable
from os import environ
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from scipy.special import (
    airy,
    digamma,
    erf,
    fresnel,
    gamma,
    hankel1,
    hankel2,
    iv,
    jv,
    kv,
    yv,
)
from slugify import slugify

from colormap_complex import ALL_COLORMAPS, ColormapType, colormap
from colormap_complex.matplotlib import get_mpl_1d_colormap

CI = environ.get("CI", "false").lower() == "true"
CACHE_PATH = Path(__file__).parent / ".cache"


@pytest.fixture(autouse=True)
def setup_cache() -> None:
    CACHE_PATH.mkdir(parents=True, exist_ok=True)


@pytest.mark.parametrize("type", ALL_COLORMAPS)
def test_colormap(type: ColormapType) -> None:
    lin = np.linspace(0, 1, 100)
    x, y = np.meshgrid(lin, lin)
    c = colormap(type=type)(x, y)
    fig, ax = plt.subplots()
    ax.imshow(c, extent=(0, 1, 0, 1), origin="lower")
    ax.set_title(type)
    fig.savefig(CACHE_PATH / f"colormap-{type}.jpg")
    plt.close(fig)


def test_colormap_all() -> None:
    lin = np.linspace(0, 1, 100)
    x, y = np.meshgrid(lin, lin)
    w = int(np.ceil(np.sqrt(len(ALL_COLORMAPS))))
    h = int(np.ceil(len(ALL_COLORMAPS) / w))
    fig, ax = plt.subplots(h, w, figsize=(2 * w, 2 * h), layout="constrained")
    ax = ax.flatten()
    for i, type in enumerate(ALL_COLORMAPS):
        c = colormap(type=type)(x, y)
        ax[i].imshow(c, extent=(0, 1, 0, 1), origin="lower")
        ax[i].set_title(type)
    for i in range(len(ALL_COLORMAPS), len(ax)):
        fig.delaxes(ax[i])
    fig.savefig(CACHE_PATH / "colormap-all.jpg")
    plt.close(fig)


@pytest.mark.skipif(CI, reason="Slow")
@pytest.mark.parametrize(
    "name,f",
    [
        ("z", lambda z: z),
        ("z^3", lambda z: z**3),
        ("Ai(z)", lambda z: airy(z)[0]),
        ("jv(0, z)", lambda z: jv(0, z)),
        ("yv(0, z)", lambda z: yv(0, z)),
        ("iv(0, z)", lambda z: iv(0, z)),
        ("kv(0, z)", lambda z: kv(0, z)),
        ("hankel1(0, z)", lambda z: hankel1(0, z)),
        ("hankel2(0, z)", lambda z: hankel2(0, z)),
        ("gamma(z)", lambda z: gamma(z)),
        ("digamma(z)", lambda z: digamma(z)),
        ("erf(z)", lambda z: erf(z)),
        ("FresnelS(z)", lambda z: fresnel(z)[0]),
        ("sqrt(1-1/z^2+z^3)", lambda z: np.sqrt(1 - 1 / z**2 + z**3)),
        ("z^(2/3+i)", lambda z: z ** (2 / 3 + 1j)),
    ],
)
@pytest.mark.parametrize(
    "cylindrical,magnitude_growth", [(False, False), (True, False), (True, True)]
)
def test_complex_function(
    name: ColormapType,
    f: Callable[[Any], Any],
    cylindrical: bool,
    magnitude_growth: bool,
) -> None:
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.6), layout="constrained")
    lin = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(lin, lin)
    z = f(x + 1j * y)
    if cylindrical:
        cf0 = ax[0].pcolormesh(x, y, np.abs(z), shading="auto")
        ax[0].set_title("|f(z)|")
        cf1 = ax[1].pcolormesh(x, y, np.angle(z), shading="auto", cmap="twilight")
        ax[1].set_title("arg f(z)")
    else:
        cf0 = ax[0].pcolormesh(x, y, z.real, shading="auto")
        ax[0].set_title("Re f(z)")
        cf1 = ax[1].pcolormesh(x, y, z.imag, shading="auto")
        ax[1].set_title("Im f(z)")
    fig.colorbar(cf0, ax=ax[0])
    fig.colorbar(cf1, ax=ax[1])
    ax[0].set_aspect("equal")
    ax[1].set_aspect("equal")
    # both part
    ax[2].set_title("f(z)")
    if cylindrical:
        r = np.abs(z)
        angle = np.angle(z)
        if magnitude_growth:
            r = np.fmod(np.log(r), 1)
        cmap = colormap(type="oklch")
        c = cmap(angle / (2 * np.pi), r, scale=True)
        ax[2].set_title("f(z) (oklch)")
        cba = fig.colorbar(
            ScalarMappable(
                norm=Normalize(angle.min(), angle.max()), cmap=get_mpl_1d_colormap(cmap, 0.5)
            ),
            ax=ax[2],
        )
        cba.set_ticks([-np.pi, 0, np.pi])
        cba.set_ticklabels([r"$-\pi$", r"$0$", r"$\pi$"])
        cbr = fig.colorbar(
            ScalarMappable(
                norm=Normalize(0, 1) if magnitude_growth else Normalize(np.min(r), np.max(r)),
                cmap=get_mpl_1d_colormap(cmap, 0.5, axis=1),
            ),
            ax=ax[2],
        )
        if magnitude_growth:
            cbr.set_ticks([0, 0.5, 1])
            cbr.set_ticklabels([r"$1$", r"$e^{\frac{1}{2}}$", r"$e$"])
    else:
        c = colormap(type="oklab")(z.real, z.imag, scale=True)
        ax[2].set_title("f(z) (oklab)")
    ax[2].imshow(c, extent=(-1, 1, -1, 1), origin="lower")
    for ax_ in ax:
        ax_.set_xlabel("Re z")
        ax_.set_ylabel("Im z")
    fig.suptitle(f"Complex function: {name}")
    fig.savefig(
        CACHE_PATH
        / (
            f"complex-function-{slugify(name)}"
            + ("-cyl" if cylindrical else "")
            + ("-magnitude" if magnitude_growth else "")
            + ".jpg"
        ),
        dpi=200,
    )
    plt.close(fig)
