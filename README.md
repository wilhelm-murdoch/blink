```python
  from blink import Blink
  
  blinker = Blink()
  
  @blinker.bind('test-event')
  def toUpper(username='', *args, **kwargs):
    return username.upper()

  @blinker.bind('test-event')
  def toLower(username='', *args, **kwargs):
    return username.lower()

  def test():
    blinker.trigger('test-event', username='mErPfLaKeS')
    
  print bar()
  >>> 'MERPFLAKES'
  >>> 'merpflakes'
```
