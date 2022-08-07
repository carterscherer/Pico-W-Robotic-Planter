#############################################################################
#                                                                           #
#    M A I N       MOTHER HOME TECH                     RUN ON SOL 1.0.0    #
#                                                                           #
#############################################################################

# This program will be saved on the PICO W 
# This program will run after boot.py and will hold all the callable anvil functions from the UI


# A C T I V E  I M P O R T S
import anvil.pico
import uasyncio as a
from machine import Pin, PWM
from utime import sleep
import anvil.server

# modules for data table UIs
import plotly.express as px
import numpy as np

# import board
# import simpleio



# R E M O V E D
# import adafruit_hcsr04
# sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


# This is an example Anvil Uplink script for the Pico W.
# See https://anvil.works/pico for more information

UPLINK_KEY = "<Enter your Anvil Server Key here>"

WetHands = '0 A3 1 32;4 E4 1 32;8 A4 1 32;12 B4 1 32;16 C#5 1 32;20 B4 1 32;24 A4 1 32;28 E4 1 32;32 D4 1 32;36 F#4 1 32;40 C#5 1 32;44 E5 1 32;48 C#5 1 32;52 A4 1 32;64 A3 1 32;68 E4 1 32;72 A4 1 32;76 B4 1 32;80 C#5 1 32;84 B4 1 32;88 A4 1 32;92 E4 1 32;96 D4 1 32;100 F#4 1 32;104 C#5 1 32;108 E5 1 32;112 C#5 1 32;116 A4 1 32;128 A3 1 32;132 E4 1 32;136 A4 1 32;140 B4 1 32;144 C#5 1 32;148 B4 1 32;152 A4 1 32;156 E4 1 32;160 D4 1 32;164 F#4 1 32;168 C#5 1 32;172 E5 1 32;176 C#5 1 32;180 A4 1 32;128 G#5 1 32;152 A5 1 32;160 F#5 1 32;184 E5 1 32;192 G#5 1 32;188 F#5 1 32;192 A3 1 32;196 E4 1 32;200 A4 1 32;204 B4 1 32;208 C#5 1 32;212 B4 1 32;216 A4 1 32;220 E4 1 32;224 D4 1 32;228 F#4 1 32;232 C#5 1 32;236 E5 1 32;240 C#5 1 32;244 A5 1 32;216 B5 1 32;220 C#6 1 32;228 F#5 1 32;248 C#6 1 32;252 E6 1 32;256 G6 1 32;256 G3 1 32;260 B3 1 32;264 D4 1 32;268 F#4 1 32;272 A4 1 32;268 F#6 1 32;244 A4 1 32;272 D6 1 32;276 F#4 1 32;280 D4 1 32;284 B3 1 32;288 G3 1 32;292 B3 1 32;296 D4 1 32;300 F#4 1 32;304 A4 1 32;280 A5 1 32;284 B5 1 32;320 G6 1 32;320 G3 1 32;324 B3 1 32;328 D4 1 32;332 F#4 1 32;328 F#6 1 32;336 D6 1 32;344 A5 1 32;348 B5 1 32;340 F#4 1 32;344 D4 1 32;348 B3 1 32;352 G3 1 32;356 B3 1 32;360 D4 1 32;364 F#4 1 32;368 A4 1 32;336 A4 1 32;376 A5 1 32;384 E5 1 32;384 A3 1 32;388 E4 1 32;392 A4 1 32;396 B4 1 32;400 C#5 1 32;404 B4 1 32;408 A4 1 32;412 E4 1 32;416 A3 1 32;432 C#5 1 32;436 E5 1 32;440 A5 1 32;444 C#6 1 32;460 B3 1 32;464 D4 1 32;468 F#4 1 32;472 A4 1 32;476 C#5 1 32;459 F#5 1 32;459 B5 1 32;459 D6 1 32;472 C#6 1 32;476 A5 1 32;484 E5 1 32;484 E6 1 32;488 F#6 1 32;488 F#5 1 32;492 B3 1 32;496 D4 1 32;500 F#4 1 32;504 A4 1 32;508 C#5 1 32;496 D6 1 32;516 B5 1 32;520 C#6 1 32;524 D6 1 32;532 C#6 1 32;536 D6 1 32;544 F#6 1 32;555 C#6 8 32;524 G3 1 32;528 B3 1 32;532 D4 1 32;536 F#4 1 32;540 A4 1 32;555 A5 8 32;555 E5 8 32;555 A4 9 32;556 E4 8 32;556 C#4 8 32;556 A3 8 32;572 B5 1 32;576 A5 1 32;580 B5 1 32;580 E3 1 32;584 G#3 1 32;588 B3 1 32;592 E4 1 32;596 G#4 1 32;600 E4 1 32;604 B3 1 32;608 G#3 1 32;612 E3 1 32;616 G#3 1 32;620 B3 1 32;624 E4 1 32;628 G#4 1 32;632 E4 1 32;636 A3 1 32;644 G3 1 32;648 B3 1 32;652 D4 1 32;656 F#4 1 32;644 G6 1 32;648 F#6 1 32;652 E6 1 32;656 D6 1 32;660 E6 1 32;664 D6 1 32;668 E6 1 32;672 F#6 1 32;660 A4 1 32;664 F#4 1 32;668 D4 1 32;672 B3 1 32;676 A3 1 32;680 C#4 1 32;684 E4 1 32;688 A4 1 32;692 C#5 1 32;696 A4 1 32;700 E4 1 32;680 E6 1 32;692 A6 1 32;704 C#4 1 32;708 E3 1 32;712 G#3 1 32;716 B3 1 32;720 E4 1 32;724 G#4 1 32;708 G#6 1 32;712 E6 1 32;716 B5 1 32;720 G#5 1 32;724 E5 1 32;738 E3 1 32;742 G#3 1 32;746 B3 1 32;750 E4 1 32;754 G#4 1 32;738 B5 1 32;742 G#5 1 32;746 E5 1 32;750 B4 1 32;766 E3 1 32;770 G#3 1 32;774 B3 1 32;778 E4 1 32;782 B3 1 32;794 E3 1 32;798 G#3 1 32;802 B3 1 32;806 E4 1 32;810 E4 1 32;818 A5 1 32;826 E5 1 32;826 A3 1 32;830 E4 1 32;834 A4 1 32;838 B4 1 32;842 C#5 1 32;846 B4 1 32;850 A4 1 32;854 E4 1 32;858 D4 1 32;862 F#4 1 32;866 C#5 1 32;870 E5 1 32;874 C#5 1 32;878 A4 1 32;882 A5 1 32;890 A5 1 32;890 A3 1 32;894 E4 1 32;898 A4 1 32;902 B4 1 32;906 C#5 1 32;910 B4 1 32;914 A4 1 32;918 E4 1 32;922 D4 1 32;926 F#4 1 32;930 C#5 1 32;934 E5 1 32;938 C#5 1 32;942 A4 1 32;420 C#4 1 32;424 E4 1 32;428 A4 1 32;953 A3 1 32;953 G#5 1 32;957 E4 1 32;961 A4 1 32;965 B4 1 32;969 C#5 1 32;974 B4 1 32;979 A4 1 32;985 E4 1 32;995 A5 1 32;995 A3 1 32;995 C#4 1 32;995 E4 1 32;995 A4 1 32;995 C#5 1 32;995 E5 1 32;1015 B7 1 5'


# We use the LED to indicate server calls and responses.
led = Pin("LED", Pin.OUT, value=1)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PINs
green = Pin(8, Pin.OUT)
pump = Pin(9, Pin.OUT)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PIEZO
buzzerPIN = 6
BuzzerObj = PWM(Pin(buzzerPIN))


def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    buzzerPinObject.duty_u16(int(65536*0.2))
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty_u16(int(65536*0))
    sleep(silence_duration)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ATTEMPT TO SHOW LIVE ULTRASONIC DATA IN UI

# SCATTER PLOTLY
# @anvil.server.callable
# def tankData_INACTIVE():
#     data = px.data.iris()
#     fig = px.scatter(data, x="tank", y="water_level", color="species", trendline="ols")
#     return fig

# PLOTLY
@anvil.server.callable
def tankData():
  x = np.arange(0.0, 5.0, 0.02)
  y = np.exp(-x) * np.cos(2*np.pi*x)
  
  return x, y


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - soundOne():
@anvil.pico.callable(is_async=True)
async def soundOne():
    # Main loop will go through each tone in order up and down.
    for i in range(2):
        buzzer(BuzzerObj,587,0.5,1) # D (RE)
        green.toggle()
        await a.sleep_ms(1001)
        buzzer(BuzzerObj,587,0.5,0) # O F F

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - sonicUltra():
@anvil.pico.callable(is_async=True)
async def sonicUltra():

    print(f"hey i am measuring: {}")

    # initilize pins for echo / trig on ultrasonic distance sensor    
    trig = Pin(7, Pin.OUT)
    echo = Pin(10, Pin.IN, Pin.PULL_DOWN)

    # comment for cont run
    # while True:
    for i in range(2):
        trig.value(0)
        time.sleep(0.1)
        trig.value(1)
        time.sleep_us(2)
        trig.value(0)
        while echo.value()==0:
            pulse_start = time.ticks_us()
        while echo.value()==1:
            pulse_end = time.ticks_us()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17165 / 1000000
        distance = round(distance, 0)
        print ('Distance:',"{:.0f}".format(distance),'cm')
        time.sleep(1)
    return distance
        



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - pico_fn(n):
@anvil.pico.callable(is_async=True)
async def pico_fn(n):
    # Output will go to the Pico W serial port
    print(f"Called local function with argument: {n}")

    # Blink the LED and then double the argument and return it.
    for i in range(10):
        led.toggle()
        await a.sleep_ms(50)
    return n * 2


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - notify():
@anvil.pico.callable(is_async=True)
async def notify():
    # Output will go to the Pico W serial port
    
    

    # Blink the LED and then double the argument and return it.
    for i in range(1):
        
        pump.value(1)
        green.toggle()
        await a.sleep_ms(5000)
        pump.value(0)



        green.value(1)
        await a.sleep_ms(10)
        green.value(0)
        


# Connect the Anvil Uplink. In MicroPython, this call will block forever.

anvil.pico.connect(UPLINK_KEY)     
anvil.server.wait_forever()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - whatLevel():
@anvil.pico.callable(is_async=True)
async def whatLevel():
    # Output will go to the Pico W serial port
	
	tankLevel = sonar.distance

	while True:
    	try:
        	print((tankLevel,))
			await a.sleep_ms(2000)
    	except RuntimeError:
        	print("Retrying!")
    	time.sleep(0.1)

	return tankLevel


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - WetMine():
@anvil.pico.callable(is_async=True)
async def WetMine():
One buzzer on pin 0
    mySong = music(WetHands, pins=[Pin(6)])

    Four buzzers
    mySong = music(song, pins=[Pin(0),Pin(1),Pin(2),Pin(3)])

    for i in range(10):
        print(mySong.tick())
        sleep(0.04)

