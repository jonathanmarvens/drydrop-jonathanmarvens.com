# -*- coding: utf-8 -*-
"""
    pygments.styles
    ~~~~~~~~~~~~~~~

    Contains built-in styles.

    :copyright: 2006-2008 by Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

from pygments.plugin import find_plugin_styles
from pygments.util import ClassNotFound


#: Maps style names to 'submodule::classname'.
STYLE_MAP = {
    'default':  'default::DefaultStyle',
}


def get_style_by_name(name):
    if name in STYLE_MAP:
        mod, cls = STYLE_MAP[name].split('::')
        builtin = "yes"
    else:
        for found_name, style in find_plugin_styles():
            if name == found_name:
                return style
        # perhaps it got dropped into our styles package
        builtin = ""
        mod = name
        cls = name.title() + "Style"

    try:
        mod = __import__('pygments.styles.' + mod, None, None, [cls])
    except ImportError:
        raise ClassNotFound("Could not find style module %r" % mod +
                         (builtin and ", though it should be builtin") + ".")
    try:
        return getattr(mod, cls)
    except AttributeError:
        raise ClassNotFound("Could not find style class %r in style module." % cls)


def get_all_styles():
    """Return an generator for all styles by name,
    both builtin and plugin."""
    for name in STYLE_MAP:
        yield name
    for name, _ in find_plugin_styles():
        yield name
