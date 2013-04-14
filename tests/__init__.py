# -*- coding: utf-8 -*-

import blink
import unittest

class BlinkTest(unittest.TestCase):
    def setUp(self):
        self._blink = blink.Blink()
        self._test = lambda: None

    def test_bind_with_callback(self):
        self._blink.bind('test', self._test)
        self.assertIn('test', self._blink._events)
        self.assertEqual(len(self._blink._events), 1)
        self._blink.bind('test', self._test)
        self.assertIn(self._test, self._blink._events['test'])
        self.assertEqual(len(self._blink._events['test']), 2)

    def test_bind_without_callback(self):
        self._blink.bind('test')(self._test)
        self.assertIn('test', self._blink._events)
        self.assertEqual(len(self._blink._events), 1)
        self._blink.bind('test')(self._test)
        self.assertIn(self._test, self._blink._events['test'])
        self.assertEqual(len(self._blink._events['test']), 2)

    def test_unbind_known_event(self):
        self._blink.bind('test')(self._test)
        self._blink.unbind('test')
        self.assertEqual(self._blink._events, {})

    def test_bind_with_arbitrary_arguments(self):
        pass

    def test_unbind_unknown_event(self):
        pass

    def test_trigger_with_known_event(self):
        pass

    def test_trigger_with_unknown_event(self):
        pass