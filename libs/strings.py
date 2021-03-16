"""
libs.strings

By default, uses `en-us.json` file inside the `strigs` to-level folder.

If language changes, set `libs.strigs.default_locale` and run `libs.strigs.refresh()`
"""

import json
default_locale = "en-us"
cached_strings = {}


def refresh():
    global cached_strings
    with open(f"strings/{default_locale}.json") as f:
        cached_strings = json.load(f)


def gettext(name):
    return cached_strings[name]


refresh()
