# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest

from ..directories import DirectoriesCommand
from hamcrest import assert_that
from hamcrest import equal_to
from mock import Mock


class TestLookup(unittest.TestCase):

    def setUp(self):
        self.scheme = 'http'
        self.host = 'example.com'
        self.port = 9489
        self.version = '0.1'
        self.session = Mock()

    def test_lookup(self):
        self.session.get.return_value = Mock(json=Mock(return_value={"return": "value"}),
                                             status_code=200)

        cmd = DirectoriesCommand(self.scheme, self.host, self.port, self.version, self.session)

        result = cmd.lookup(profile='default', term='Alice')

        self.session.get.assert_called_once_with(
            'http://example.com:9489/0.1/directories/lookup/default',
            params={'term': 'Alice'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_when_not_200(self):
        self.session.get_return_value = Mock(status_code=404)

        cmd = DirectoriesCommand(self.scheme, self.host, self.port, self.version, self.session)

        self.assertRaises(Exception, cmd.lookup, profile='my_profile', term='lol')

    def test_headers(self):
        self.session.get.return_value = Mock(json=Mock(return_value={"return": "value"}),
                                             status_code=200)

        cmd = DirectoriesCommand(self.scheme, self.host, self.port, self.version, self.session)

        result = cmd.headers(profile='default')

        self.session.get.assert_called_once_with(
            'http://example.com:9489/0.1/directories/lookup/default/headers',
            params={})
        assert_that(result, equal_to({'return': 'value'}))

    def test_headers_when_not_200(self):
        self.session.get_return_value = Mock(status_code=404)

        cmd = DirectoriesCommand(self.scheme, self.host, self.port, self.version, self.session)

        self.assertRaises(Exception, cmd.lookup, profile='my_profile')
