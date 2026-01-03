from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu, run_task, StopWatch
from mission1 import red_1
from mission2 import red_2
from mission3 import red_3
from mission4 import blue_4
from mission5 import blue_5
from mission6 import blue_6
from mission7 import blue_7
from mission8 import red_8
#from lightsensor import test_sensor

hub = PrimeHub()

class self:
    hub = PrimeHub()
    hub.display.orientation(Side.RIGHT)

    # Setup the self drive base
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    drive = DriveBase(left_motor, right_motor, wheel_diameter= 62.4, axle_track=106)
    drive.settings(straight_speed=700)
    default_settings = drive.settings()
    drive.use_gyro(True)
    print (default_settings)

    color_sensorR = ColorSensor(Port.C)
    color_sensorL = ColorSensor(Port.D)


    # Setup the arm 
    # speed value is degrees/second
    L_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    R_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    #multiply angle by 3 when writing code  
    
    def align_to_line(self):
        '''
        align with the line
        '''
        for t in range(1, 200):
            valueR = await self.color_sensorR.reflection()
            valueL = await self.color_sensorL.reflection()
            valueR = (valueR-45)*100/t
            valueL = (valueL-45)*100/t
            print(valueR, valueL)
            self.left_motor.run(valueL)
            self.right_motor.run(valueR)

    def arm_run_angle(self,speed, rotation_angle):
        """
        move both the left and right motors
        """
        self.L_motor.run_angle(speed=speed, rotation_angle=rotation_angle)
        await self.R_motor.run_angle(speed=speed, rotation_angle=-rotation_angle)

    def reset_drive(self):
        """
        Reset the self drive base to the default speed and acceleration
        """
        self.drive.settings(*self.default_settings)
    
    def stop_motors(self):
        """
        Stop all motors
        """
        #wheel motors
        self.left_motor.stop()
        self.right_motor.stop()
        #attachment motors
        self.L_motor.stop()
        self.R_motor.stop()

self = self()

    
async def calibrate_arm(self):
    """
    Adjust the angle of the arm to use as zero degrees

    Pressing the left/right buttons changes the arm by one degree
    Pressing and holding the buttons scans through angles quickly after
    a one second delay
    """
    # reset the current motor angle to be zero degrees
    self.L_motor.reset_angle(0)
    self.R_motor.reset_angle(0)
    a=0
    self.hub.display.number(a)
    clock = StopWatch()
    # how long to wait while holding a button before counting additional presses
    delay = 1000
    # indicate if a button press has been handled yet
    handled = False
    while True:
        # check if any buttons are pressed
        pressed = self.hub.buttons.pressed()
        # handle a button press if not already handled or if the time delay has passed
        if pressed and not handled or clock.time() > delay:
            if Button.RIGHT in pressed:
                a = a + 1
            if Button.LEFT in pressed:
                a = a - 1
            if Button.BLUETOOTH in pressed:
                break
            # mark the button press as handled so we don't repeat it
            handled = True
            # adjust the motor angle and display
            self.hub.display.number(a)
            self.L_motor.track_target(target_angle=a)
            self.R_motor.track_target(target_angle=-a)

        # after the delay has occured while holding a button reset the clock
        # also make the delay very small to allow quickly scanning angles
        if pressed and clock.time() > delay:
            clock.reset()
            delay = 10

        # if the button has been released then reset the handled flag,
        # reset the clock, and reset to a long delay
        if not pressed:
            handled = False
            clock.reset()
            delay = 1000

    # reset the current motor angle to be zero degrees
    self.L_motor.reset_angle(0)


async def testing(self):
    #color = await color_sensor1.hsv(surface = True)
    #color = color_sensor2.hsv(surface = True)
   # while True: 
        #await wait(1000)
        #color = await color_sensor1.hsv(surface = True)
        #print(color)
        #hub.light.on(color)
        #print("Ctrl+Alt+Elite is sigma")
        #await self.R_motor.run_angle(speed=700, rotation_angle=-1000)
        await self.R_motor.run_angle(speed=700, rotation_angle=-900)
    

# Dictionary of all runs and their display character
runs = {"1" : red_1, 
        "2" : red_2,
        "3" : red_8,
        "4" : red_3,
        "5" : blue_4,
        "6" : blue_5,
        "7" : blue_6,
        "8" : blue_7,
        #"9" : blue_9,
        "C" : calibrate_arm,
        "T" : testing,
        #"L" : test_sensor
        }


def main():
    print("battery voltage: ", self.hub.battery.voltage(), "mV")
    print("battery current: ", self.hub.battery.current(), "mA")

    #wait for IMU to calibrate
    self.hub.display.icon(Icon.EMPTY)

    run_keys = sorted(runs.keys())
    n = 0
    while True:
        # rotate the keys to start with the nth item
        rotated_keys = run_keys[n:] + run_keys[:n]
        # Get the user selection on which run to launch
        selection = hub_menu(*rotated_keys)
        # get the index of the selected key in the original list
        n = run_keys.index(selection)
        # move index to the next item to run, modulo number of keys
        n = (n + 1) % len(run_keys)
    
        # Launch the selected run
        if selection in runs.keys():
            self.hub.display.icon(Icon.ARROW_UP)
            run_task(runs[selection](self))
            self.stop_motors()


main()