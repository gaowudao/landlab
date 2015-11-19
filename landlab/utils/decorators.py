"""General decorators for the landlab library."""

import warnings
from functools import wraps


def make_return_array_immutable(func):
    """Decorate a function so that its return array is read-only.

    Parameters
    ----------
    func : function
        A function that returns a numpy array.

    Returns
    -------
    func
        A wrapped function that returns a read-only view of an array.
    """
    @wraps(func)
    def _wrapped(self, *args, **kwds):
        array = func(self, *args, **kwds)
        immutable_array = array.view()
        immutable_array.flags.writeable = False
        return immutable_array
    return _wrapped


def deprecated(func):
    """Mark a function as deprecated.

    Parameters
    ----------
    func : function
        A function.

    Returns
    -------
    func
        A wrapped function that issues a deprecation warning.
    """
    @wraps(func)
    def _wrapped(*args, **kwargs):
        warnings.warn(
            "Call to deprecated function {name}.".format(name=func.__name__),
            category=DeprecationWarning)
        return func(*args, **kwargs)
    _wrapped.__dict__.update(func.__dict__)

    return _wrapped
