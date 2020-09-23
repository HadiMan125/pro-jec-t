def on_forever():
    for index in range(4):
        basic.show_leds("""
            . # . # .
            . . # . .
            . . # . .
            # . . . #
            . # # # .
            """)
        basic.pause(3000)
        basic.show_string("Hello MaMa and Dad!")
        basic.pause(1000)
basic.forever(on_forever)
