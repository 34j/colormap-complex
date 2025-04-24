from __future__ import annotations

from typing import Literal

import numpy as np
from matplotlib.colors import BivarColormapFromImage, ListedColormap

from ._main import Colormap


def get_mpl_colormap(colormap: Colormap, /, N: int = 128, M: int = 128) -> BivarColormapFromImage:
    """
    Get a matplotlib colormap from a function.

    Parameters
    ----------
    colormap : Colormap
        The colormap function to use.
    N : int
        The number of colors in the x axis.
    M : int
        The number of colors in the y axis.

    Returns
    -------
    BivarColormapFromImage
        Matplotlib colormap.

    """
    return BivarColormapFromImage(
        colormap(np.linspace(0, 1, N)[:, None], np.linspace(0, 1, M)[None, :]),
        name=colormap.__name__,
    )


def get_mpl_1d_colormap(
    colormap: Colormap,
    v: float,
    /,
    axis: Literal[0, 1] = 0,
    N: int = 128,
) -> ListedColormap:
    """
    Get a matplotlib colormap from a function.

    Parameters
    ----------
    colormap : Callable[[NDArray[np.number]], NDArray[np.number]]
        The colormap function to use.
    v : float
        The value to use for the colormap.
    axis : Literal[0, 1]
        The axis to take the colormap from.
    N : int
        The number of colors in the colormap.

    Returns
    -------
    BivarColormapFromImage
        Matplotlib colormap.

    """
    if axis == 0:
        x = np.linspace(0, 1, N)
        y = np.full_like(x, v)
    else:
        y = np.linspace(0, 1, N)
        x = np.full_like(y, v)
    return ListedColormap(colormap(x, y), name=colormap.__name__)
