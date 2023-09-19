#!/usr/bin/python3

""" This is unittestmodeule for Base class """

import unittest

import os
import json

from models.base import Base

class TestBase(unittest.TestCase):
    """ Base class Unit test """

    def __init__with_id(self):
        """ Initializing the BaseClass with id """
        base = Base()
        self.assertEqual(base.id, None)

    def __init__without_id(self):
        """" Initializing the BaseClass id with no value """
        base = Base()
        self.assertEqual(base.id, )

if __name__ == '__main__':
    unittest.main()
