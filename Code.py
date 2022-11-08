#Libraries
#To communicate with the GPIO pins
import RPi.GPIO as GPIO

#time variable required for ultrasonic sensor to calculate distance
import time

#setup the GPIO as  a GPIO Board
GPIO.setup(GPIO.BOARD)

#not to print warnings
GPIO.setwarnings(False)

#Global variables for the board 
TRIG_PIN =14
ECHO_PIN = 15
LED = 12

#Setting up the variables as a output and input
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

#This is for defining the frequency for led pwm
LED_PWM = GPIO.PWM(LED,125) 
#pwm object and starting with duty cycle at 0 
#initial their is no glow
LED_PWM.start(0)

#distance variable
distance = 0
Maximum_distance = 40


#This below function is for calculating the distance of the object from the sensor
def Distance_Calculate():

    #Calculating the distance of object is done by sending a pulse
    GPIO.output(TRIG_PIN,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN,False)

    while GPIO.input(ECHO_PIN) == 0:
        start = time.time()

    while GPIO.input(ECHO_PIN)==1:
        stop = time.time()
    
    #total duration is time taken by pulse to travel from sensor to object and object to sensor in a loop
    Totalduration = stop - start

    #and finally distance is calculated by multipolying the duration to speed of sound in air
    distance = (Totalduration*34300)/2
    time.sleep(0.01)
    return distance

try:
    while True:

        distance = Distance_Calculate()
        print(distance)

        #if distance is smaller or equal to maximum distance glowing of led will start
        if distance<= Maximum_distance:
            LED_PWM.ChangeDutyCycle(Maximum_distance - (distance))

        else:
            LED_PWM.ChangeDutyCycle(0)

except KeyboardInterrupt:
    GPIO.cleanup()
          
        


