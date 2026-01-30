# MicroPython-servo
A simple MicroPython library for micro-servo.

## Features
- Easy to use.
- Compatible with EP32 and Raspberry.

## Example of use
```python
from servo import Servo
from time import sleep
my_servo = Servo(pwm_pin=0, min_pulse=500_000, max_pulse=2_400_000, frequency=50)
for degree in [0, 90, 180]:
  my_servo.rotate(degree)
  sleep(1)
