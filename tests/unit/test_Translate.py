#!/usr/bin/env python
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

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2015, Nestor Arocha"
__email__ = "nesaro@gmail.com"

import unittest

class TestTranslate(unittest.TestCase):
    def testEcho(self):
        from pydsl.translator import translate, PythonTranslator
        from pydsl.grammar.definition import RegularExpression
        from pydsl.check import checker_factory
        cstring = checker_factory(RegularExpression('.*'))
        def function(my_input):
            return my_input
        pt = PythonTranslator(function)
        self.assertEqual(translate(pt,{'my_input':"1234"}),"1234")

