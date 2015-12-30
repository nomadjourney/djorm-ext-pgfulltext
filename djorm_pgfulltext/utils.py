import psycopg2.extensions

from django.utils.text import force_text


def adapt(text):
    a = psycopg2.extensions.adapt(force_text(text))
    a.prepare(psycopg2.extensions.connection)
    return a
