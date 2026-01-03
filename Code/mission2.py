async def red_2(robot):
    '''Map reveal mission'''
    await robot.drive.straight(710)
    await robot.drive.turn(-36)
    robot.drive.settings(straight_speed=100)
    await robot.drive.straight(170)
    robot.drive.settings(straight_speed=700)
    await robot.drive.straight(-150)
    await robot.drive.turn(35)
    await robot.drive.straight(-725/2)
    await robot.drive.turn(25)
    await robot.drive.straight(-725/2)