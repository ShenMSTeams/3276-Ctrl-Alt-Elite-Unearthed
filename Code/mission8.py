from pybricks.tools import wait

async def red_8(robot):

    "Minecart Mission"

    await robot.drive.straight(870)
    await robot.drive.turn(90)
    await robot.drive.straight(100)
    await robot.arm_run_angle(speed=500, rotation_angle=350)
    await wait(500)
    await robot.drive.straight(-200)
    await robot.drive.turn(-80)
    await robot.drive.straight(-900)
    #await robot.arm_run_angle(speed=1000, rotation_angle=-670)


