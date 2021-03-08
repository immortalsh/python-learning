# -*- coding: utf-8 -*-

# Created  Sat Nov 14 16:16:48 2020


# traverse.py
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nvalue:" + value)
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys():
    print("\n" + name.title())
