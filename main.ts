let start = 0
let elapsed = 0
let sleephour = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start = input.runningTime()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    elapsed = input.runningTime() - start
    basic.showNumber(Math.idiv(elapsed, 1000))
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    sleephour = 28800
    if (elapsed >= sleephour) {
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    
    if (elapsed < sleephour) {
        basic.showString("You need this much more hours of sleep:")
        basic.showString("" + ("" + (sleephour - elapsed) / 1))
    }
    
})
