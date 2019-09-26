import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

for i in range(5):
	servo.ChangeDutyCycle(bottom)
	time.sleep(1.0)

	servo.ChangeDutyCycle(middle)
	time.sleep(1.0)

	servo.ChangeDutyCycle(top)
	time.sleep(1.0)

def setservo(x):
    pulse = ((top-bottom)*(x+90)/180)+bottom
    servo.ChangeDutyCycle(pulse)
    time.sleep(1.0)




