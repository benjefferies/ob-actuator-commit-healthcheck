import os
from unittest import TestCase, mock

import requests_mock

import wait


class TestWait(TestCase):

    @mock.patch.dict(os.environ, {'URL': 'http://test'})
    @requests_mock.mock()
    def test_is_up(self, m):
        # Given
        m.get('http://test/actuator/health', json={'status': 'UP'})

        # When
        is_up = wait.is_up(None)

        # Then
        self.assertTrue(is_up)

    @mock.patch.dict(os.environ, {'URL': 'http://test'})
    @requests_mock.mock()
    def test_not_up(self, m):
        # Given
        m.get('http://test/actuator/health', json={'status': 'DOWN'})

        # When
        is_up = wait.is_up(None)

        # Then
        self.assertFalse(is_up)

    @mock.patch.dict(os.environ, {'URL': 'http://test', 'COMMIT': 'abc'})
    @requests_mock.mock()
    def test_is_on_commit(self, m):
        # Given
        m.get('http://test/actuator/info', json={'git': {'commit': {'id': 'abc'}}})

        # When
        is_commit = wait.is_on_commit(None, 'abc')

        # Then
        self.assertTrue(is_commit)

    @mock.patch.dict(os.environ, {'URL': 'http://test', 'COMMIT': 'abc'})
    @mock.patch.dict(os.environ, {'URL': 'http://test'})
    @requests_mock.mock()
    def test_not_on_commit(self, m):
        # Given
        m.get('http://test/actuator/info', json={'git': {'commit': {'id': 'abc'}}})

        # When
        is_commit = wait.is_on_commit(None, 'abd')

        # Then
        self.assertFalse(is_commit)

