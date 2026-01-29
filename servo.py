'''Librería servo.'''
from machine import Pin, PWM

class Servo:

    def __init__(self, pwm_pin:int, min_pulse:int = 500_000, max_pulse:int = 2_400_000, frequency:int = 50) -> None:
        '''Una clase para el Servo motor.\n
           Args:
                pwm_pin: El pin de la señal PWM.
                min_pulse: El pulso mínimo en nanosegundos.
                max_pulse: El pulso máximo en nanosegundos.
                frequency: La frecuencia en Hz.'''
        self.__servo = PWM(Pin(pwm_pin), freq = frequency)
        self.__min_pulse = min_pulse
        self.__max_pulse = max_pulse


    def rotate(self, degrees:int) -> None:
        '''Mueve el servo a los grados deseados (0-180°).'''
        if degrees < 0 or degrees > 180:
            raise ValueError("Sólo ángulos con rango de 0 a 180.")
        duty_cycle = int(self.__min_pulse + (degrees / 180) * (self.__max_pulse - self.__min_pulse))
        self.__servo.duty_ns(duty_cycle)

if __name__ == '__main__':
    servo = Servo(17)
    from time import sleep

    try:
        degrees = [0, 90]
        while True:
            for degree in degrees:
                servo.rotate(degree)
                print(degree)
                sleep(1)

    except KeyboardInterrupt:
        servo.rotate(0)
        