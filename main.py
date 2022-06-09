def on_button_pressed_a():
    if 30 <= input.temperature():
        basic.show_number(input.temperature())
        basic.show_string("hot")
    elif 15 <= input.temperature() and 20 > input.temperature():
        basic.show_number(input.temperature())
        basic.show_string("cool")
    elif 20 <= input.temperature() and 30 > input.temperature():
        basic.show_number(input.temperature())
        basic.show_string("warm")
    elif 15 > input.temperature():
        basic.show_number(input.temperature())
        basic.show_string("cold")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if 45 < input.compass_heading() and 135 >= input.compass_heading():
        basic.show_string("east")
    elif 135 < input.compass_heading() and 225 >= input.compass_heading():
        basic.show_string("south")
    elif 225 < input.compass_heading() and 315 >= input.compass_heading():
        basic.show_string("west")
    elif 315 < input.compass_heading() or 45 >= input.compass_heading():
        basic.show_string("north")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
