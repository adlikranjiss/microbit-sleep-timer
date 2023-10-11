start = 0
elapsed = 0
sleephour = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global elapsed
    elapsed = input.running_time() - start
    basic.show_number(Math.idiv(elapsed, 1000))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global sleephour
    sleephour = 28800
    if elapsed >= sleephour:
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
