#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is part of pydsl.
#
# pydsl is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
# pydsl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pydsl.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2017, Nestor Arocha"
__email__ = "nesaro@gmail.com"

"""

Parser expression grammars

Loosely based on pymeta

https://launchpad.net/pymeta

See also http://en.wikipedia.org/wiki/Parsing_expression_grammar

"""

from .definition import Grammar
from itertools import chain

class ZeroOrMore(Grammar):
    def __init__(self, element):
        Grammar.__init__(self)
        self.element = element

    def first(self):
        return Choice([self.element])


class OneOrMore(Grammar):
    def __init__(self, element):
        Grammar.__init__(self)
        self.element = element

    def first(self):
        return Choice([self.element])

class Sequence(Grammar, list):
    def __init__(self, *args, **kwargs):
        base_alphabet = kwargs.pop('base_alphabet', None)
        Grammar.__init__(self, base_alphabet)
        list.__init__(self, *args, **kwargs)
        for x in self:
            if not isinstance(x, Grammar):
                raise TypeError(x)

    def __hash__(self):
        return hash(tuple(self))

    @classmethod
    def from_string(cls, string):
        from .definition import String
        return cls([String(x) for x in string])

class Choice(set, Grammar):
    """Uses a list of grammar definitions with common base alphabets"""
    def __init__(self, grammarlist, calculate_base_alphabet = True):
        set.__init__(self, grammarlist)
        if calculate_base_alphabet:
            base_alphabet = set()
            for x in self:
                base_alphabet = base_alphabet.union(x.alphabet)
        else:
            base_alphabet = None
        Grammar.__init__(self, base_alphabet)

    def __str__(self):
        return str([str(x) for x in self])

    def __add__(self, other):
        return Choice([x for x in self] + [x for x in other])

    def __hash__(self):
        return hash(tuple(x for x in self))

class Optional(object):
    def __init__(self, element):
        Grammar.__init__(self)
        self.element = element

class Not(object):
    def __init__(self, element):
        self.element = element

class And(object):
    def __init__(self, element):
        Grammar.__init__(self)
        self.element = element

