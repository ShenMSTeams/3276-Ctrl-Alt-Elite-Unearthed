async def blue_7(robot):

    "Silo"
    await robot.drive.straight(420) 
    await robot.arm_run_angle(speed=1000, rotation_angle=-700)
    await robot.arm_run_angle(speed=700, rotation_angle=600)
    await robot.arm_run_angle(speed=1000, rotation_angle=-700)
    await robot.arm_run_angle(speed=700, rotation_angle=600)
    await robot.arm_run_angle(speed=1000, rotation_angle=-700)
    await robot.arm_run_angle(speed=700, rotation_angle=600)
    await robot.arm_run_angle(speed=1000, rotation_angle=-700)
    await robot.arm_run_angle(speed=700, rotation_angle=600)
    await robot.arm_run_angle(speed=1000, rotation_angle=-700)
    await robot.arm_run_angle(speed=700, rotation_angle=600)
    await robot.drive.straight(-420)