def on_button_pressed_a():
    basic.show_number(input.temperature())
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
