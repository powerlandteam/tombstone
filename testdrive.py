#!/usr/bin/env python
##import rospy
##from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time
import Adafruit_MCP4725

RIGHT_FORWARD = 13       #   Purple
LEFT_FORWARD = 12        #   Red

RIGHT_REVERSE = 5    #   Blue
LEFT_REVERSE = 8     #   Green

RIGHT_BRAKE = 16   #   Yellow
LEFT_BRAKE = 15  #   Orange


# Create a DAC instance.
dac1 = Adafruit_MCP4725.MCP4725()


dac1 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_REVERSE, GPIO.OUT)
GPIO.setup(LEFT_REVERSE, GPIO.OUT)
GPIO.setup(RIGHT_BRAKE, GPIO.OUT)
GPIO.setup(LEFT_BRAKE, GPIO.OUT)

##def stop():
##    GPIO.output(RIGHT_BRAKE, GPIO.HIGH)
##    GPIO.output(LEFT_BRAKE, GPIO.HIGH)
##    GPIO.output(RIGHT_FORWARD, GPIO.LOW) 
##    GPIO.output(LET_FORWARD, GPIO.LOW)
##    GPIO.output(RIGHT_REVERSE, GPIO.LOW)
##    GPIO.output(LEFT_REVERSE, GPIO.LOW)
##    dac1.set_voltage(0)
##def forward():
while True:
    GPIO.output(RIGHT_BRAKE, GPIO.LOW)
    GPIO.output(LEFT_BRAKE, GPIO.LOW)
    GPIO.output(RIGHT_FORWARD, GPIO.HIGH) 
    GPIO.output(LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_REVERSE, GPIO.LOW)
    GPIO.output(LEFT_REVERSE, GPIO.LOW)
    dac1.set_voltage(3092)
    
##def backward():
##    GPIO.output(RIGHT_BRAKE, GPIO.LOW)
##    GPIO.output(LEFT_BRAKE, GPIO.LOW)
##    GPIO.output(RIGHT_FORWARD, GPIO.LOW) 
##    GPIO.output(LET_FORWARD, GPIO.LOW)
##    GPIO.output(RIGHT_REVERSE, GPIO.HIGH)
##    GPIO.output(LEFT_REVERSE, GPIO.HIGH)
##    dac1.set_voltage(2096)
##
##def left(turn):
##    GPIO.output(RIGHT_BRAKE, GPIO.LOW)
##    GPIO.output(LEFT_BRAKE, GPIO.HIGH)
##    GPIO.output(RIGHT_FORWARD, GPIO.HIGH) 
##    GPIO.output(LET_FORWARD, GPIO.LOW)
##    GPIO.output(RIGHT_REVERSE, GPIO.LOW)
##    GPIO.output(LEFT_REVERSE, GPIO.LOW)
##    dac1.set_voltage(2096)
##
##
##    
##def right(turn):
##    GPIO.output(RIGHT_BRAKE, GPIO.HIGH)
##    GPIO.output(LEFT_BRAKE, GPIO.LOW)
##    GPIO.output(RIGHT_FORWARD, GPIO.LOW) 
##    GPIO.output(LET_FORWARD, GPIO.HIGH)
##    GPIO.output(RIGHT_REVERSE, GPIO.LOW)
##    GPIO.output(LEFT_REVERSE, GPIO.LOW)
##    dac1.set_voltage(2096)
##
##def callback(data):
##    linear = data.linear.x
##    angular = data.angular.z
##    #print(str(linear)+"\t"+str(angular))
##    if (linear == 0.0 and angular == 0.0):
##        stop()
##    elif (linear > 0.0 and angular == 0.0):
##        forward()
##    elif (linear < 0.0 and angular == 0.0):
##        backward()
##    elif (linear == 0.0 and angular > 0.0):
##        left()
##    elif (linear == 0.0 and angular < 0.0):
##        right()
##    else:
##        stop()
##        
##def listener():
##    rospy.init_node('cmdvel_listener', anonymous=False)
##    rospy.Subscriber("/cmd_vel", Twist, callback)
##    rospy.spin()
##
##if __name__== '__main__':
##    print('Tortoisebot Differential Drive Initialized')
##    listener()


