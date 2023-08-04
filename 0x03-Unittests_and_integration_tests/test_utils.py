#!/usr/bin/env python3
""" method to test that the method returns what it is supposed to."""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize
import requests
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ("b": 2)),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Tests the access_nested_map method.
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
    """
    Test the access_nested_map method and raise an error if need be
    """
    with self.assertRaises(Exception):
        access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """the utils.get_json function."""
     @parameterized.expand([
         ("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False})
         ])
     def test_get_json(self, test_url, test_payload, mock_requests_get):
         """tests"""
         mock_requests_get.return_value.json.return_value = test_payload
         result = get_json(test_url)
         self.assertEqual(result, test_payload)
         mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the memoization decorator
    """
    def test_memoize(self):
        """
        Test that utils.memoize decorator works
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

         with patch.object(TestClass, 'a_method') as mock_object:
             test = TestClass()
             test.a_property()
             test.a_property()
             mock_object.assert_called_once()
