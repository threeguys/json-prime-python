#
#    Copyright 2020 Ray Cole
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import unittest
import sys
import json
import glob
import os

sys.path.append('..')

from jsonprime import expression

class TestMappings(unittest.TestCase):

    def test_football_mappings(self):
        with open('football/football.json', 'rt') as f:
            data = json.load(f)

        for mapping_name in glob.glob('football/mappings/*.json'):
            with self.subTest(filename=mapping_name):
                expected_name = 'football/expected/%s' % os.path.basename(mapping_name)

                with open(mapping_name, 'rt') as f:
                    config = json.load(f)

                with open(expected_name, 'rt') as f:
                    expected = json.load(f)

                result = expression(config, data)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
