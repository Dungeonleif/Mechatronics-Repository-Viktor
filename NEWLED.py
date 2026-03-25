import time
from gpiozero import LED
from gpiozero import RGBLED
from time import sleep
from gpiozero import Servo
import warnings
warnings.filterwarnings('ignore')
eye_led = RGBLED(red="BOARD21", green="BOARD19", blue="BOARD23")
SERVO_PIN = "BOARD11"
yellow_led = LED("BOARD7")
orange_led = LED("BOARD5")
red_led = LED("BOARD8")

def wave(servo):
    """Move servo through min, mid, and max positions."""
    print("Moving to MIN...")
    servo.min()
    sleep(1)

    print("Moving to MID...")
    servo.mid()
    sleep(1)

    print("Moving to MAX...")
    servo.max()
    sleep(1)

    print("Back to MID...")
    servo.mid()
    sleep(1)


def traffic_light():
    while(True):
        orange_led.on()
        time.sleep(1)
        orange_led.off()
        time.sleep(1)
        yellow_led.on()
        time.sleep(1)
        yellow_led.off()
        time.sleep(1)
        red_led.on()
        time.sleep(1)
        red_led.off()
        time.sleep(1)

def extract_features(command):
    extract_features = command["features"]
    print(extract_features)
    if("eyes" in extract_features):
        print("found eyes")
        eye_features = extract_features["eyes"]
        eyes(eye_features)
    

def eyes(eye_command):
    print("eye_command")
    if("set_rgb_eye_color" in eye_command):
        print("found set eye color")
        print(eye_command["set_rgb_eye_color"])
        eye_led.color = eye_command["set_rgb_eye_color"]
        print (eye_led)

def main():
    servo = Servo(SERVO_PIN)
    wave(servo)
    print("Starting Program")
    command = {"robot": "bob", "features":{"eyes":{"set_rgb_eye_color":[.9,1,0]}}}
    extract_features(command)
    eyes(command)
    traffic_light()
    print(command)
    print("Ending Program") 
    
main()