# coding=utf-8
import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


s = u"Base de geodatos vacía ííííííí"

print(remove_accents(s))
