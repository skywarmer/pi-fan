import RPi.GPIO as GPIO

led_pin = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, True)
