#!/usr/bin/env python
from __future__ import print_function
import jinja2

my_dict = {"a": "whatever"}

my_template = """
some
text
of
something
{{ a }}
something
"""

t = jinja2.Template(my_template)
print(t.render(my_dict))
