async def red_1(robot):
    '''
    surface brushing mission
    '''
    await robot.drive.straight(650)
    await robot.drive.turn(-45)
    await robot.drive.straight(-10)
    await robot.drive.turn(-45)
    await robot.drive. straight(140)
    #at surface brushing
    await robot.R_motor.run_angle(speed=700, rotation_angle=-700)
    await robot.R_motor.run_angle(speed=700, rotation_angle=600)
    #picked up the brush
    await robot.drive.straight(-150)
    await robot.drive.straight(50)
    await robot.drive.turn (90)
    await robot.drive.straight (-360)
    await robot.drive.turn (45)
    await robot.drive.straight (120)
    #droping the brush
    await robot.R_motor.run_angle(speed=700, rotation_angle=380)
    await robot.drive.straight (-450)