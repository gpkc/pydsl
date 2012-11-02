#!/usr/bin/python
# -*- coding: utf-8 -*-
#This file is part of pydsl.
#
#pydsl is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#pydsl is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with pydsl.  If not, see <http://www.gnu.org/licenses/>.

"""Wrapper Classes"""

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2012, Nestor Arocha"
__email__ = "nesaro@gmail.com"

import logging
LOG = logging.getLogger(__name__)
from abc import ABCMeta, abstractmethod, abstractproperty
from pydsl.Memory.Loader import load_function

class Content:
    """String wrapper"""
    def __init__(self, content):
        self.content = TokenList(content)
            
    def guess(self):
        from pydsl.Guess import Guesser
        guess = Guesser()
        return guess(self)

    def check(self, grammar):
        return grammar in self.guess()

    def available_alphabets(self):
        return None

    def available_grammars(self):
        return None

class FunctionsMeta(type):
    def __dir__(cls):
        from pydsl.Memory.Search.Searcher import MemorySearcher
        from pydsl.Memory.Search.Indexer import Indexer
        from pydsl.Config import GLOBALCONFIG
        searcher = MemorySearcher([Indexer(x) for x in GLOBALCONFIG.memorylist])
        return [ x["identifier"] for x in searcher.search({"ancestors":{"$in":"Function"}})]

    def __getattr__(cls, key):
        return load_function(key)

    @staticmethod
    def available_transforms(content):
        from pydsl.Memory.Search.Searcher import MemorySearcher
        from pydsl.Memory.Search.Indexer import Indexer
        from pydsl.Config import GLOBALCONFIG
        searcher = MemorySearcher([Indexer(x) for x in GLOBALCONFIG.memorylist])
        resultlist = []
        for element in content.guess():
            resultlist += searcher.search({"input":{"$part":{"input":element}}})
        return resultlist

class FunctionPool(metaclass=FunctionsMeta):
    pass

class NetworkPool:
    pass

