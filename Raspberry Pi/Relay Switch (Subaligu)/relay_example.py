import RPi.GPIO as GPIO
import time

# IMPORTANT: In this example I had to connect my relay switch to the 3.3v power (Quite common) and swap LOW/HIG

relay_pin_pos = 16 # Which PIN is used on the Pi
is_low_volt_relay = True # Use this when connected to 3.3V source (If it does switch off use this and switch to 3.3V)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(relay_pin_pos, GPIO.OUT) # GPIO Assign mode

try:
    while True:
        GPIO.output(relay_pin_pos, GPIO.HIGH if is_low_volt_relay else GPIO.LOW) # OFF
        print("Switched off")
        time.sleep(5)

        GPIO.output(relay_pin_pos, GPIO.LOW if is_low_volt_relay else GPIO.HIGH) # ON
        print("Switched on")
        time.sleep(5)      

except KeyboardInterrupt:
    GPIO.cleanup()