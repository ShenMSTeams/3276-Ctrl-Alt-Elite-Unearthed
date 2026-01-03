async def blue_6(robot):

    "Tip The Scales mission"
    
    await robot.drive.straight(230)
    await robot.drive.turn(-90)
    await robot.drive.straight(445)
    await robot.drive.turn (90)
    await robot.drive.straight(75)
    robot.drive.settings(straight_speed=100)
    await robot.drive.straight(-75)
    robot.reset_drive()
    await robot.drive.turn (-90)
    await robot.drive.straight(-650)
