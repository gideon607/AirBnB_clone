#!/usr/bin/python3
"""Testunit for console program"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class testing console"""

    def create(self):
        """creating the instance"""
        return HBNBCommand()

    def test_quit(self):
        """ testing for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test unit for the method EOF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

