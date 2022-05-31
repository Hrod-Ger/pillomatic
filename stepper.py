import RPi.GPIO as gpio
import time
import sys

motorPins = (7,11,13,15)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio.setup(motorPins, gpio.OUT)
motor_direction = input('select motor direction 1=anticlockwise, 2=clockwise: ')
while True:
    try:
        if(motor_direction == 2):
            print('motor running clockwise\n')
            gpio.output(motorPins, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
            time.sleep(0.002)

        elif(motor_direction == 1):
            print('motor running anti-clockwise\n')
            gpio.output(motorPins, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
            time.sleep(0.002)
            gpio.output(motorPins, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
            time.sleep(0.002)

            
    #press ctrl+c for keyboard interrupt
    except KeyboardInterrupt:
        #query for setting motor direction or exit
        motor_direction = input('select motor direction 1=anticlockwise, 2=clockwise or 3=exit: ')
        #check for exit
        if(motor_direction == 3):
            print('motor stopped')
            sys.exit(0)
