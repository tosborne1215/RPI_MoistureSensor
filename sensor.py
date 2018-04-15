
# This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import RPi.GPIO as GPIO
import time  # This is the time library, we need this so we can use the sleep function


def callback(channel):
    if GPIO.input(channel):
        print("LED off")
    else:
        print("LED on")


# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while True:
    # This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
    time.sleep(0.1)
