from cv2 import *                           #install python-opencv bindings, numpy
import matplotlib.pyplot as plt             #import matplotlib module 4 python
import matplotlib.image as img              
import time                                 #time management lib
delay_ = 2.00                               #global var to set a little delay of 2secs

def setPillColor(self, pillCapture):    #Pill color detection
    #Color detection implementation -> https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    #Or use this GitHub code instead -> https://github.com/aysekonus/realtimecolordetection
    print("Pill detected")
    print("Obtaining image attributes")
    print("Classificating pill")

def firstDoor(self):                    #Opens the first door, 1 by 1 pill
    try:
        print("Openning doors...")
        #Move X degrees mech1
        print("Waiting first pill to pass...")
        #Wait Y sexonds/miliseconds to let JUST one pill pass
        print("Closing doors...")
        #Move again -X degrees mech1
        return 1
    except:
        print("Error in firstDoor")
        return 0

def secondDoor(self):
    try:
        print("Openning doors...")
        #Move X degrees mech2
        print("Waiting the photo to be taken...")
        #Wait until the camera takes a photo
        print("Closing doors...")
        #Move again -X degrees mech2 
        return 1
    except:
        print("Error in secondDoor")
        return 0

def takePhoto(self):                    #Code from https://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python
    try:    
        # initialize the camera
        cam = VideoCapture(0)               # 0 -> index of camera
        s, img = cam.read()
        if s:                               # frame captured without any errors
            namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
            imshow("cam-test",img)
            waitKey(0)
            destroyWindow("cam-test")
            imwrite("filename.jpg",img)     #save image
        return 1
    except:
        print("Error in takePhoto")
        return 0

def placePill(self, pill):
    try:
        print("Selecting where place this pill in base its color...")
        if (pill.color == 0):
            print("Blue")
            #Move z0 degrees mech3
        elif (pill.color == 1):
            print("Red")
            #move z1 degrees mech3
        elif (pill.color == 2):
            print("Green")
            #move z2 degrees mech3
        #elif...
        else:
            print("Not matching color...")
            #move zN degrees mech3 -> 
        return 1
    except:
        print("Error nin placePill")
        return 0

def introduce1pill(self):
    print("First Pill going in...")
    if (firstDoor() != 0):
        time.sleep(delay_)              #let 2 seconds of margin between operations
        print("Say 'Cheese'...")
        if(takePhoto() !=0):
            time.sleep(delay_)
            print("Which color are you?")
            imgPill = img.imread('/img/pill.jpg')       #https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image
            if (setPillColor(imgPill) != 0):
                print("Oh, you are that color!")
                if(placePill(pill) !=0):
                    print("Ok, go ahead...")
                    if (secondDoor() != 0):
                        print("Pill in its place!")

#main
#connection with the app -> the connection status will be saved as a variable called "connection.status"
connection.status = 1               #0 is disconnected, 1 is connected
 
while(connection.status == 1):
    print("------------------------------")
    print("----------PILL-O-MATIC--------")
    print("------------------------------")
    print("00. Introduce 1 pill (DEMO)")
    print("01. Refill 1 type of pill")
    print("0.2 Refill N types of pills")

    #De momento es estático, así que se trabajará con la opción DEMO, para asegurar que mínimo se coloca una pastilla correctamente
    '''
    menuOption = input("Menu option")
    if menuOption == 0:
        introduce1pill()
    elif menuOption == 1:
        refill1Type()
    elif menuOption == 2:
        refillNTypes
    '''
    introduce1pill()