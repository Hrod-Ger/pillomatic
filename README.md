# pill-o-matic
Main code for the RLP project

# Table of contents
- [What is this?](https://github.com/Hrod-Ger/pillomatic#what-is-this)
- [Requirements](https://github.com/Hrod-Ger/pillomatic#requirements)
- [Algorithms](https://github.com/Hrod-Ger/pillomatic#algorithms)
- [Licence](https://github.com/Hrod-Ger/pillomatic#licence)
- [Use-case](https://github.com/Hrod-Ger/pillomatic#use-case)
- [Contribution](https://github.com/Hrod-Ger/pillomatic#contribution)
- [Authors](https://github.com/Hrod-Ger/pillomatic#authors)
- [Bibliography](https://github.com/Hrod-Ger/pillomatic#bibliography)

# What is this?
This is our RLP project. It is a pill dispenser that can classify the pills given and distribute them at the correct date and time.
Our main goal with this project is to make easier the life of the people with our robot.

# Requirements
For running each sample code:
- Python 3.9.x
- NumPy
- time
- Matplotlib
- RPi.GPIO
- cv2

# Algorithms
We use one algorithm to detect via a WebCam which colour is the pill in order to classify it:
- [Code](https://github.com/Hrod-Ger/pillomatic/blob/main/src/main.py)

# License
MIT

# Use-case
This project can be used to classify pills or small objects by their colour.

# Contribution
You can contribute to improve this project!

# Authors
- [Roger Martin](https://github.com/Hrod-Ger)
- [Juan Aguilera](https://github.com/jaguilera95)
- [Karel Gabriel Jara](https://github.com/garikar)
- [Adrià Mateos](https://github.com/AdriMateos)

# Bibliography
- [Robot that was our inspiration](https://www.xataka.com/robotica-e-ia/pillo-es-robot-asistente-que-mira-por-tu-salud-reconoce-caras-y-dispensa-medicamentos)
- [Detect colour with OpenCV](https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/)
- [Detect colour in real time](https://github.com/aysekonus/realtimecolordetection](https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/)
- [Servo Featherwing information](https://learn.adafruit.com/adafruit-8-channel-pwm-or-servo-featherwing)
- [RPi.GPIO basics](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
