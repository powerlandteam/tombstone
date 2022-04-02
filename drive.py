
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD    
import Adafruit_MCP4725
import time

lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.message('Circuit Digest')
time.sleep(2.0)
lcd.message('\nDAC using Rpi')
time.sleep(5.0)
lcd.clear()
dac = Adafruit_MCP4725.MCP4725(address=0x60)

while True:
    for x in range(0,4097,150):
        
        print(x)
        dac.set_voltage(x)
        lcd.cursor_pos = (0,0)
        lcd.message("DAC Value: " + str(x))
        voltage = x/4096.0*5.0
        lcd.message("\nAnalogVolt: %.2f" % voltage)
        time.sleep(2)
        lcd.clear()


leftEn = 12			#	Purple
rightEn = 13		#	Red

leftBackward = 5	#	Blue
leftForward = 6		#	Green
rightForward = 16	#	Yellow
rightBackward = 20	#	Orange

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(leftEn, GPIO.OUT)
GPIO.setup(rightEn, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

pwmL = GPIO.PWM(leftEn, 100)
pwmL.start(0)
pwmR = GPIO.PWM(rightEn, 100)
pwmR.start(0)

def stop():
    print('stopping')
    pwmL.ChangeDutyCycle(0)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.HIGH)
    pwmR.ChangeDutyCycle(0)
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.HIGH)

def forward():
    print('going forward')
    pwmL.ChangeDutyCycle(100)
    pwmR.ChangeDutyCycle(100)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.LOW)
    GPIO.output(rightBackward, GPIO.LOW)

def backward():
    print('going backward')
    pwmL.ChangeDutyCycle(100)
    pwmR.ChangeDutyCycle(100)
    GPIO.output(leftForward, GPIO.LOW)
    GPIO.output(rightForward, GPIO.LOW)
    GPIO.output(leftBackward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.HIGH)

def left(turn):
    print('turning left')
    pwmL.ChangeDutyCycle(100)
    pwmR.ChangeDutyCycle(100)
    GPIO.output(leftForward, GPIO.LOW)
    GPIO.output(leftBackward, GPIO.HIGH)
    GPIO.output(rightForward, GPIO.HIGH)
    GPIO.output(rightBackward, GPIO.LOW)

def right(turn):
    print('turning right')
    pwmL.ChangeDutyCycle(100)
    pwmR.ChangeDutyCycle(100)
    GPIO.output(leftForward, GPIO.HIGH)
    GPIO.output(leftBackward, GPIO.LOW)
    GPIO.output(rightForward, GPIO.LOW)
    GPIO.output(rightBackward, GPIO.HIGH)

def callback(data):
    linear = data.linear.x
    angular = data.angular.z
    #print(str(linear)+"\t"+str(angular))
    if (linear == 0.0 and angular == 0.0):
        stop()
    elif (linear > 0.0 and angular == 0.0):
        forward()
    elif (linear < 0.0 and angular == 0.0):
        backward()
    elif (linear == 0.0 and angular > 0.0):
        left()
    elif (linear == 0.0 and angular < 0.0):
        right()
    else:
        stop()
        
def listener():
    rospy.init_node('cmdvel_listener', anonymous=False)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__== '__main__':
    print('Tortoisebot Differential Drive Initialized')
    listener()
© 2022 GitHub, Inc.
Terms
P
