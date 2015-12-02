from __future__ import absolute_import


VERSION = ({% set lst = cookiecutter.version.split('.') %}{{ lst[0] }}}, {{ lst[1] }}, {{ lst[2] }}, None)

__version__ = '{0:d}.{1:d}.{2:d}'.format(*VERSION)
if VERSION[3]:
    __version__ += '.{3:d}'.format(*VERSION)
