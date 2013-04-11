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
