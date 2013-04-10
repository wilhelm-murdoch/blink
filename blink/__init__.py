# -*- coding: utf-8 -*-

class BlinkException(Exception): pass

class Blink(object):
    def __init__(self):
        self._events = {}

    def bind(self, event, callback=None):
        if event not in self._events:
            self._events[event] = []

        if callback is None:
            def _decorator(callback):
                self.bind(event, callback)
            return _decorator

        self._events[event].append(callback)


    def unbind(self, event, callback=None):
        if callback is None:
            del self._events[event]
        else:
            return self._events[event].remove(callback)


    def trigger(self, event, *args, **kwargs):
        if event not in self._events:
            raise BlinkException("Event %s has not been set.".format(event))

        for callback in self._events[event]:
            callback(*args, **kwargs)

blink = Blink()