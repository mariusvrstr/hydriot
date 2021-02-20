import RPi.GPIO as GPIO
import time

# IMPORTANT: In this example I had to connect my relay switch to the 3.3v power (Quite common) and swap LOW/HIG

relay_pin_pos = 16 # Which PIN is used on the Pi
is_high = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(relay_pin_pos, GPIO.OUT) # GPIO Assign mode

try:
    while True:
        GPIO.output(relay_pin_pos, GPIO.HIGH) # OFF
        print("Switched off")
        time.sleep(5)

        GPIO.output(relay_pin_pos, GPIO.LOW) # ON
        print("Switched on")
        time.sleep(5)      

except KeyboardInterrupt:
    GPIO.cleanup()