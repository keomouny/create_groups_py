#!/usr/bin/env python 3

import unittest
import os
from exo_groups.create_groups import CreateGroups


class TestCreateGroups(unittest.TestCase):

    def test_get_data_from_file(self):
        test_create_grp = CreateGroups()
        test_create_grp.get_data_from_file()
        self.assertTrue(os.path.exists('groupes.txt'))
        self.assertIs(type(test_create_grp.names_list), list)

    def test_create_json_file(self):
        self.assertTrue(os.path.exists('groupes.json'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
