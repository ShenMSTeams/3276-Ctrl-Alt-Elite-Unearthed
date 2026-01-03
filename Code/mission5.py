from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

async def blue_5(robot):
    '''
    Forge mission
 
    '''
    await robot.drive.straight(725)
    await robot.drive.turn(35)
    await robot.drive.straight(30)
    await robot.align_to_line()
    await robot.L_motor.run_angle(speed=700, rotation_angle=-200)
    robot.L_motor.run_angle(speed=700, rotation_angle=250)
    await robot.drive.straight(-50)
    await robot.drive.turn(-45)
    await robot.drive.straight(70)
    await robot.L_motor.run_angle(speed=300, rotation_angle=-160)
    await robot.drive.straight(-70)
    robot.L_motor.run_angle(speed=700, rotation_angle=160)
    await robot.drive.turn(-90)
    await robot.drive.straight(-500)
    await robot.drive.straight(10)
    await robot.drive.turn(75)
    await robot.drive.straight(50)
    await robot.L_motor.run_angle(speed=700, rotation_angle=-230)
    await robot.drive.straight(50)
    await robot.L_motor.run_angle(speed=700, rotation_angle=230)
    await robot.drive.straight(-100)
    robot.L_motor.run_angle(speed=700, rotation_angle=-400)
    await robot.drive.turn(-65)
    await robot.drive.straight(-100)