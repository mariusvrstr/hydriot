from enum import Enum

class GPIO(Enum):
    GPIO004 = 4
    GPIO007 = 7
    GPIO008 = 8
    GPIO009 = 9 
    GPIO010 = 10
    GPIO011 = 11
    GPIO014 = 14
    GPIO015 = 15
    GPIO018 = 18
    GPIO022 = 22
    GPIO023 = 23
    GPIO024 = 24
    GPIO025 = 25   
    
class PinMapper():

    def gpio_to_wiringpi(self, gpio_pin):
        
        switcher = {
            GPIO.GPIO018:  1,
            GPIO.GPIO022:  3,
            GPIO.GPIO023:  4,
            GPIO.GPIO024:  5,
            GPIO.GPIO025:  6,
            GPIO.GPIO004:  7,
            GPIO.GPIO008:  10,
            GPIO.GPIO007:  11,
            GPIO.GPIO010:  12,
            GPIO.GPIO009:  13,
            GPIO.GPIO011:  14,
            GPIO.GPIO014:  15,
            GPIO.GPIO015:  16,
        }

        mapped = switcher.get(gpio_pin, -1)

        if mapped == -1:
             raise Exception(f"Sorry, no mapping exist for GPIO PIN [{gpio_pin}] for Wiringpi PIN")

        return mapped    

    def gpio_to_pin(self, gpio_pin):
        
        switcher = {
            GPIO.GPIO018:  12,
            GPIO.GPIO022:  15,
            GPIO.GPIO023:  16,
            GPIO.GPIO024:  18,
            GPIO.GPIO025:  22,
            GPIO.GPIO004:  7,
            GPIO.GPIO008:  24,
            GPIO.GPIO007:  26,
            GPIO.GPIO010:  19,
            GPIO.GPIO009:  21,
            GPIO.GPIO011:  23,
            GPIO.GPIO014:  8,
            GPIO.GPIO015:  10,
        }

        mapped = switcher.get(gpio_pin, -1)

        if mapped == -1:
             raise Exception(f"Sorry, no mapping exist for GPIO PIN [{gpio_pin}] to normal PIN")

        return mapped





