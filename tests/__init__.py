# -*- coding: utf-8 -*-

import blink
import unittest

class BlinkTest(unittest.TestCase):
    def setUp(self):
        self._blink = blink.Blink()
        self._test = lambda *args, **kwargs: (args, kwargs)

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

    def test_unbind_unknown_event(self):
        try:
            self._blink.unbind('test')
        except Exception, e:
            self.assertTrue(isinstance(e, blink.BlinkException))
            self.assertEqual(e.message, 'Event test has not been set.')

    def test_trigger_with_arguments(self):
        class _static: result=()
        def _test(*args, **kwargs):
            _static.result=(args, kwargs)
        self._blink.bind('test')(_test)
        self._blink.trigger('test', 1, 2, 3, foo=True, bar=False)
        self.assertEqual(_static.result[0], (1, 2, 3))
        self.assertEqual(_static.result[1], {'foo': True, 'bar': False})

    def test_trigger_with_known_event(self):
        class _static: n=0
        def _test():
            _static.n+=1
        self._blink.bind('test')(_test)
        self._blink.trigger('test')
        self.assertEqual(_static.n, 1)
        self._blink.trigger('test')
        self._blink.trigger('test')
        self.assertEqual(_static.n, 3)

    def test_trigger_with_unknown_event(self):
        try:
            self._blink.trigger('test')
        except Exception, e:
            self.assertTrue(isinstance(e, blink.BlinkException))
            self.assertEqual(e.message, 'Event test has not been set.')