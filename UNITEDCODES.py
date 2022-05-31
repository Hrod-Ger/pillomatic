import RPi.GPIO as gpio
import sys
from __future__ import division
import time
import Adafruit_PCA9685
import numpy as np
import cv2

# WEBCAM
webcam = cv2.VideoCapture(0)

# SERVO MOTORS
pwm = Adafruit_PCA9685.PCA9685()
# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# STEPPER MOTOR
motorPins = (7,11,13,15)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(motorPins, gpio.OUT)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
pills = 0
while pills < 2:
    # Deposit pill
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(4)
    
    numColor = 0
    _, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	# Set range for red color and define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

	# Set range for green color and define mask
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    
    # Detect only that particular color
    kernal = np.ones((5, 5), "uint8")
    
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                            mask = red_mask)
    
    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                    (x + w, y + h),
                                    (0, 0, 255), 2)
            numColor = 1
            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                    (x + w, y + h),
                                    (0, 255, 0), 2)
            numColor = 2
            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

    # Move servo on channel 2 between extremes.
    pwm.set_pwm(2, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(2, 0, servo_max)
    time.sleep(4)
    
    # Move servo on channel 3 between extremes.
    print('Moving servo on channel 3, press Ctrl-C to quit...')
    pwm.set_pwm(3, 0, servo_min)
    time.sleep(7)
    pwm.set_pwm(3, 0, servo_max)
    time.sleep(1)
    
# Extract pill
gpio.output(motorPins, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
time.sleep(0.002)
gpio.output(motorPins, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
time.sleep(0.002)
gpio.output(motorPins, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
time.sleep(0.002)
gpio.output(motorPins, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
time.sleep(0.002)
# Move servo on channel 6 between extremes.
pwm.set_pwm(6, 0, servo_min)
time.sleep(1)
pwm.set_pwm(6, 0, servo_max)
time.sleep(1)

gpio.output(motorPins, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
time.sleep(0.002)
gpio.output(motorPins, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
time.sleep(0.002)
gpio.output(motorPins, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
time.sleep(0.002)
gpio.output(motorPins, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
time.sleep(0.002)