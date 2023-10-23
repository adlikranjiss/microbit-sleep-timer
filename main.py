start = 0
elapsed = 0
sleephour = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global elapsed
    elapsed = Math.idiv(input.running_time() - start, 1000)
    basic.show_number(elapsed)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global sleephour
    sleephour = 5
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
    if elapsed < sleephour:
        basic.show_string("You need this much more hours of sleep:")
        basic.show_string("" + str((sleephour - elapsed) / 1))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
