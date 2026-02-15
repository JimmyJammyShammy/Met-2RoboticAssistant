"""
Python translation of your Arduino robot control logic.
Target platform: Raspberry Pi (RPi.GPIO)

Notes:
- Replace pin numbers with your Raspberry Pi BCM pin numbers.
- Arduino A0/A1/etc do not exist on Raspberry Pi.
- LCD code is left as a placeholder because Pi LCD wiring varies (I2C backpack is most common).
"""

import time
import RPi.GPIO as GPIO

# ---------------- PIN MAP (Raspberry Pi BCM EXAMPLE) ----------------
# IMPORTANT: These are NOT Arduino pin numbers.
# You must map your wiring to Raspberry Pi BCM GPIO numbers.

# LCD (placeholder, depends on LCD interface)
LCD_RS = None
LCD_E  = None
LCD_D4 = None
LCD_D5 = None
LCD_D6 = None
LCD_D7 = None

# Ultrasonic single-wire ping pin
PING_SIG = 7   # Example BCM pin, change to your wiring

# Buttons (use pull-up)
BTN1 = 8
BTN2 = 9
BTN3 = 10
BTN4 = 12

# LED
LED_PIN = 0    # Example BCM pin, change to your wiring

# Motors (PWM capable pins recommended)
MOTOR1_PIN = 3
MOTOR2_PIN = 5
MOTOR3_PIN = 6
MOTOR4_PIN = 11

# ---------------- SETTINGS ----------------
stopThresholdCm = 20.0
mode = 0  # 0=Idle, 1=Fast, 2=Slow, 3=Stop, 4=Demo

# PWM frequency (typical DC motor driver PWM range)
PWM_FREQ = 1000  # Hz

# Will hold PWM objects
motor_pwm = {}

# ---------------- HELPER FUNCTIONS ----------------
def init_output_if_valid(pin: int):
    if pin is None:
        return
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def clamp(val, lo, hi):
    return max(lo, min(hi, val))

def set_motor_if_valid(pin: int, value: int):
    """
    Arduino analogWrite: 0..255
    In RPi.GPIO PWM: duty cycle is 0..100
    """
    if pin is None:
        return
    value = clamp(int(value), 0, 255)
    duty = (value / 255.0) * 100.0

    pwm = motor_pwm.get(pin)
    if pwm is None:
        # If PWM not started for some reason, start it
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, PWM_FREQ)
        pwm.start(0)
        motor_pwm[pin] = pwm

    pwm.ChangeDutyCycle(duty)

def stop_all_motors():
    for pin in (MOTOR1_PIN, MOTOR2_PIN, MOTOR3_PIN, MOTOR4_PIN):
        set_motor_if_valid(pin, 0)

def read_distance_cm_single_pin():
    """
    Equivalent to your Arduino Ping))) single pin approach:
    1) drive pin LOW briefly
    2) pulse HIGH briefly (trigger)
    3) switch to input and measure echo high time

    Returns:
      distance in cm (float), or -1.0 on timeout/failure
    """
    if PING_SIG is None:
        return -1.0

    # 1) Trigger pulse
    GPIO.setup(PING_SIG, GPIO.OUT)
    GPIO.output(PING_SIG, GPIO.LOW)
    time.sleep(0.000002)  # 2 us

    GPIO.output(PING_SIG, GPIO.HIGH)
    time.sleep(0.000005)  # 5 us
    GPIO.output(PING_SIG, GPIO.LOW)

    # 2) Listen for echo
    GPIO.setup(PING_SIG, GPIO.IN)

    timeout_s = 0.03  # 30 ms like Arduino 30000 us
    start_wait = time.time()

    # Wait for pin to go HIGH
    while GPIO.input(PING_SIG) == 0:
        if time.time() - start_wait > timeout_s:
            return -1.0

    echo_start = time.time()

    # Wait for pin to go LOW
    while GPIO.input(PING_SIG) == 1:
        if time.time() - echo_start > timeout_s:
            return -1.0

    echo_end = time.time()
    duration_s = echo_end - echo_start

    # Convert echo duration to distance
    # Speed of sound ~343 m/s = 34300 cm/s
    # Distance = (time * speed) / 2
    distance_cm = (duration_s * 34300.0) / 2.0
    return distance_cm

def buttons_read_mode():
    """
    INPUT_PULLUP logic:
    Pressed => GPIO.LOW
    """
    if GPIO.input(BTN1) == GPIO.LOW:
        return 1  # Fast
    if GPIO.input(BTN2) == GPIO.LOW:
        return 2  # Slow
    if GPIO.input(BTN3) == GPIO.LOW:
        return 3  # Stop
    if GPIO.input(BTN4) == GPIO.LOW:
        return 4  # Demo
    return 0

# ---------------- SETUP ----------------
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # LED
    init_output_if_valid(LED_PIN)

    # Buttons with pull-ups
    for b in (BTN1, BTN2, BTN3, BTN4):
        GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Motors PWM init
    for pin in (MOTOR1_PIN, MOTOR2_PIN, MOTOR3_PIN, MOTOR4_PIN):
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, PWM_FREQ)
        pwm.start(0)
        motor_pwm[pin] = pwm

    stop_all_motors()

# ---------------- MAIN LOOP LOGIC (EXAMPLE) ----------------
def run_fast():
    # Example speeds (tune to match your Arduino sketch)
    for pin in (MOTOR1_PIN, MOTOR2_PIN, MOTOR3_PIN, MOTOR4_PIN):
        set_motor_if_valid(pin, 255)

def run_slow():
    for pin in (MOTOR1_PIN, MOTOR2_PIN, MOTOR3_PIN, MOTOR4_PIN):
        set_motor_if_valid(pin, 120)

def demo_mode_step(t):
    # Simple demo pattern placeholder
    phase = int(t) % 4
    if phase == 0:
        run_fast()
    elif phase == 1:
        run_slow()
    elif phase == 2:
        stop_all_motors()
    else:
        run_slow()

def loop():
    global mode

    while True:
        # Update mode based on buttons
        mode = buttons_read_mode()

        # Read distance
        dist = read_distance_cm_single_pin()

        # Obstacle safety
        if dist > 0 and dist < stopThresholdCm:
            GPIO.output(LED_PIN, GPIO.HIGH)
            stop_all_motors()
            # In Arduino you might also set mode = 3
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

            if mode == 0:
                stop_all_motors()
            elif mode == 1:
                run_fast()
            elif mode == 2:
                run_slow()
            elif mode == 3:
                stop_all_motors()
            elif mode == 4:
                demo_mode_step(time.time())

        time.sleep(0.05)  # loop delay like Arduino

# ---------------- CLEANUP ----------------
def cleanup():
    stop_all_motors()
    for pwm in motor_pwm.values():
        pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
