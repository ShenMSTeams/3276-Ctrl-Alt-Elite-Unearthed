from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

async def test_sensor(robot):
    '''
    light sensor testing
    '''
    #await robot.drive.straight(100)
    #await robot.drive.turn(90)
    #await robot.drive. straight(400)
    await robot.drive.straight(725)
    await robot.drive.turn(35)
    await robot.drive.straight(30)
    # call light sensor here
    for t in range(1, 200):
        valueR = await robot.color_sensorR.reflection()
        valueL = await robot.color_sensorL.reflection()
        valueR = (valueR-45)*100/t
        valueL = (valueL-45)*100/t
       # if valueR < 0:
        #    valueR = 0
        #if valueL < 0:
        #    valueL = 0
        print(valueR, valueL)
        robot.left_motor.run(valueL)
        robot.right_motor.run(valueR)