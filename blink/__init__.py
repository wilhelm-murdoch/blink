# -*- coding: utf-8 -*-

class BlinkException(Exception): pass

class Blink(object):
    def __init__(self):
        self._events = dict()

    def bind(self, event, callback=None):
        """Binds an event to the specified callback. If no callback is
        specified, this method assumes it is being used as a decorator.

        Parameters::
            event str
                The name of the event to assign callbacks to.
            callback function, None
                The callback to associate with the specified event.
        """
        if event not in self._events:
            self._events[event] = []

        if callback is None:
            def _decorator(callback):
                self.bind(event, callback)
            return _decorator

        self._events[event].append(callback)

    def unbind(self, event, callback=None):
        """Unbinds an event from the specified callback. If no callback is
        specified, this method will remove the specified event and all
        associated callbacks.

        Parameters::
            event str
                The name of the event to assign callbacks to.
            callback function, None
                The callback to disassociate with the specified event.
        """
        if callback is None:
            del self._events[event]
        else:
            return self._events[event].remove(callback)

    def trigger(self, event, *args, **kwargs):
        """Invokes all callbacks associated with the specified `event` name.
        You may pass arbitrary arguments through and they will be appear as
        `*args` and or `**kwargs` within each associated callback.

        Parameters::
            event str
                The name of the event to invoke.
        """
        if event not in self._events:
            raise BlinkException("Event %s has not been set.".format(event))

        for callback in self._events[event]:
            callback(*args, **kwargs)

blink = Blink()