# Blink

Blink allows you to easily bind jQuery-like events to your Python apps.

## Dependencies

Python 2.6+ and tested on Python 3+

* nose 1.1.2
* yanc 0.2.3

## Make Targets

1. `make install` installs Blink locally in development mode.
2. `make uninstall` removes Blink locally
3. `make test` runs the unit test suite
4. `make clean` removes any garbage files that usage and installation generates

## Installing From Github

    $: pip install git+git://github.com/wilhelm-murdoch/blink.git

Or, add the following line to a `requirements.txt` file:

    -e git+ssh://git@github.com/wilhelm-murdoch/blink.git#egg=blink

## Example

```python
  from blink import blink

  @blink.bind('blink:event')
  def blinker_event(message):
    print message

  blink.trigger('blink:event', message='This is a message.')
  >>> 'This is a message.'
```

Or, create your own `blink.Blink` instance to pass throughout your application:

```python
  import blink

  blinker = blink.Blink()
```

### Methods

#### blink.bind

Bind a callback to the specified event.

```python
  def callback(message):
    print message

  blink.bind('blink:event', callback)
  blink.trigger('blink:event', message='This is a message.')
  >>> 'This is a message.'
```

You can also use the `blink.bind()` method as a decorator:

```python
  @blink.bind('blink:event')
  def callback(message):
    print message

  blink.trigger('blink:event', message='This is a message.')
  >>> 'This is a message.'
```

#### blink.unbind

Unbinds the specified `callback` from the specified `event`:

```python
  blink.unbind('blink:event', callback)
```

However, if you wish to unbind all callbacks from a specified `event`, just leave out the `callback` parameter:

```python
  blink.unbind('blink:event')
```

#### blink.trigger

Invokes all callbacks associated with the specified `event` name. You may pass
arbitrary arguments through and they will be appear as `*args` and or `**kwargs` within each associated callback.

```python
  blink.trigger('blink:event', 1, 2, 3, 4, foo=True, bar=False)
```
