myVariable = 0
message1 = Event()
ResetArm = Event()

def when_started1():
    global myVariable, message1, ResetArm
    IntakeMotor.set_velocity(100, PERCENT)
    FiringMotorGroup.set_velocity(100, PERCENT)
    DiscPushMotor.set_velocity(100, PERCENT)
    EndgameMotor.set_velocity(50, PERCENT)
    EndgameMotor.set_stopping(HOLD)

def onevent_controller_1buttonB_pressed_0():
    global myVariable, message1, ResetArm
    EndgameMotor.spin_for(FORWARD, 1, TURNS, wait=True)
    while not not controller_1.buttonB.pressing():
        wait(5, MSEC)
    EndgameMotor.set_stopping(HOLD)
    EndgameMotor.stop()

def onevent_controller_1buttonR2_pressed_0():
    global myVariable, message1, ResetArm
    IntakeMotor.spin(REVERSE)
    while not not controller_1.buttonR2.pressing():
        wait(5, MSEC)
    IntakeMotor.stop()

def onauton_autonomous_0():
    global myVariable, message1, ResetArm
    DiscPushMotor.set_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    DiscPushMotor.spin_for(REVERSE, 70, DEGREES, wait=True)
    EndgameMotor.set_stopping(HOLD)

def onevent_controller_1buttonR1_pressed_0():
    global myVariable, message1, ResetArm
    IntakeMotor.spin(FORWARD)
    while not not controller_1.buttonR1.pressing():
        wait(5, MSEC)
    IntakeMotor.stop()

def onevent_controller_1buttonL1_pressed_0():
    global myVariable, message1, ResetArm
    FiringMotorGroup.spin(FORWARD)
    while not not controller_1.buttonL1.pressing(): # Button Stop mechanism 
        wait(5, MSEC)
    FiringMotorGroup.set_stopping(HOLD)
    FiringMotorGroup.stop()

def onevent_controller_1buttonL2_pressed_0():
    global myVariable, message1, ResetArm
    FiringMotorGroup.spin(REVERSE)
    while not not controller_1.buttonL2.pressing():
        wait(5, MSEC)
    FiringMotorGroup.set_stopping(HOLD)
    FiringMotorGroup.stop()

def onevent_controller_1buttonDown_pressed_0():
    global myVariable, message1, ResetArm
    DiscPushMotor.spin(REVERSE)
    while not not controller_1.buttonDown.pressing():
        wait(5, MSEC)
    DiscPushMotor.stop()

def onevent_controller_1buttonUp_pressed_0():
    global myVariable, message1, ResetArm
    DiscPushMotor.spin(FORWARD)
    while not not controller_1.buttonUp.pressing():
        wait(5, MSEC)
    DiscPushMotor.stop()

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.buttonB.pressed(onevent_controller_1buttonB_pressed_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
