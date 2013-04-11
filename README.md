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

## Examples

```python
  from blink import Blink

  blinker = Blink()

  @blinker.bind('test-event')
  def toUpper(username='', *args, **kwargs):
    print username.upper()

  @blinker.bind('test-event')
  def toLower(username='', *args, **kwargs):
    print username.lower()

  def test():
    blinker.trigger('test-event', username='mErPfLaKeS')

  test()
  >>> 'MERPFLAKES'
  >>> 'merpflakes'
```
