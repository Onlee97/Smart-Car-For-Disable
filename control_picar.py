# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

# Add new comment to expose me plzzz
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print("UP")
                GPIO.output(7,True)
                GPIO.output(11,True)
                # GPIO.output(13,False)
                # GPIO.output(15,False)
            elif char == curses.KEY_DOWN:
                print("DOWM")
                GPIO.output(7,False)
                GPIO.output(11,False)
                # GPIO.output(13,True)
                # GPIO.output(15,True)
            elif char == curses.KEY_RIGHT:
                print("RIGHT")
                GPIO.output(7,True)
                GPIO.output(11,False)
                # GPIO.output(13,False)
                # GPIO.output(15,True)
            elif char == curses.KEY_LEFT:
                print("LEFT")
                GPIO.output(7,False)
                GPIO.output(11,True)
                # GPIO.output(13,True)
                # GPIO.output(15,False)
            elif char == 10:
                GPIO.output(7,False)
                GPIO.output(11,False)
                # GPIO.output(13,False)
                # GPIO.output(15,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()