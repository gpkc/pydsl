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

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2013, Nestor Arocha"
__email__ = "nesaro@gmail.com"

import unittest

class TestGuesser(unittest.TestCase):
    """Guesser"""
    def setUp(self):
        from pydsl.Config import load_default_memory
        load_default_memory()


    def testStuff(self):
        from pydsl.Guess import Guesser
        guesser = Guesser()
        expected_result = sorted(['IntegerTree','cstring','hex','unixFilename','integer','calc_ply','ascii', 'test_alphabet', 'australian_postcode','swiss_postcode'])
        self.assertListEqual(sorted(list(guesser('1234'))), expected_result)
        self.assertListEqual(sorted(list(guesser([x for x in '1234']))), expected_result)
        #self.assertListEqual(guesser.guess_alphabet('1234'), ['ascii'])
        #self.assertListEqual(guesser.guess_grammar('1234'), ['integer','cstring'])
        #self.assertRaises(Exception, guesser, None)

    def testListInput(self):
        pass

    def testEmptyInput(self):
        pass
