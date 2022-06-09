input.onButtonPressed(Button.A, function () {
    if (30 <= input.temperature()) {
        basic.showNumber(input.temperature())
        basic.showString("hot")
    } else if (15 <= input.temperature() && 20 > input.temperature()) {
        basic.showNumber(input.temperature())
        basic.showString("cool")
    } else if (20 <= input.temperature() && 30 > input.temperature()) {
        basic.showNumber(input.temperature())
        basic.showString("warm")
    } else if (15 > input.temperature()) {
        basic.showNumber(input.temperature())
        basic.showString("cold")
    } else {
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (45 < input.compassHeading() && 135 >= input.compassHeading()) {
        basic.showString("east")
    } else if (135 < input.compassHeading() && 225 >= input.compassHeading()) {
        basic.showString("south")
    } else if (225 < input.compassHeading() && 315 >= input.compassHeading()) {
        basic.showString("west")
    } else if (315 < input.compassHeading() || 45 >= input.compassHeading()) {
        basic.showString("north")
    } else {
        basic.clearScreen()
    }
})
