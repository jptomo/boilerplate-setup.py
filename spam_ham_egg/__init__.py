from __future__ import absolute_import


VERSION = (0, 0, 1, None)

__version__ = '{0:d}.{1:d}.{2:d}'.format(*VERSION)
if VERSION[3]:
    __version__ += '.{3:d}'.format(*VERSION)
