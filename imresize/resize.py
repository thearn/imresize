from scipy.misc import lena
from scipy.interpolate import RectBivariateSpline
import numpy as np


def imresize(image, size, interp=None, mode=None):
    """
    Resizes a digital image using bivariate spline approximation.
    """
    shape = image.shape
    m, n = shape[0], shape[1]

    if len(shape) == 3 and shape[-1] == 3 or shape[-1] == 4:
        channels = [imresize(image[:, :, i], size) for i in range(shape[-1])]
        m_, n_ = channels[0].shape
        resized = np.empty((m_, n_, shape[-1]))
        for i in range(shape[-1]):
            resized[:, :, i] = channels[i]
        return resized

    if isinstance(size, float) or isinstance(size, int):
        X = np.linspace(0, m - 1, int(size * m))
        Y = np.linspace(0, n - 1, int(size * n))

    elif hasattr(size, "__iter__"):
        if len(size) <= 3:
            X = np.linspace(0, m - 1, size[0])
            Y = np.linspace(0, n - 1, size[1])
        else:
            raise Exception("Size not specified correctly")

    interp = RectBivariateSpline(np.arange(m), np.arange(n), image)
    resized = interp(X, Y)

    return resized
