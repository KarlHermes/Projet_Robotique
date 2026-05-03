"""epuck_go_forwad controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


TIME_STEP = 64
WHEEL_RADIUS = 0.0205 # rayon roues e-puck en m

# create the Robot instance.
robot = Robot()


leftMotor = robot.getDevice('motor.left')
rightMotor = robot.getDevice('motor.right')
leftMotor.setPosition(40.0)
rightMotor.setPosition(40.0)
leftSensor = robot.getDevice('motor.left.position')
rightSensor = robot.getDevice('motor.right.position')
leftSensor.enable(TIME_STEP)
rightSensor.enable(TIME_STEP)
print("Démarrage de la simulation ...")

# Initialisation
initial_left = 0.0
initial_right = 0.0
initialized = False
final_distance = 0.0


# get the time step of the current world.
#timestep = int(robot.getBasicTimeStep())


# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()


 left_pos = leftSensor.getValue()
 right_pos = rightSensor.getValue()
 if not initialized:
     initial_left = left_pos
     initial_right = right_pos
     initialized = True
     continue
 # Vérifie si le mouvement est terminé (proche de la cible 10.0)
 if abs(left_pos - 40.0) < 0.01 and abs(right_pos - 40.0) < 0.01:
 # Calcul de la distance parcourue
     delta_left = left_pos - initial_left
     delta_right = right_pos - initial_right
     avg_rotation = (delta_left + delta_right) / 2.0
     print("Angle:",avg_rotation)
     print("WHEEL_RADIUS:",WHEEL_RADIUS)
     final_distance = avg_rotation * WHEEL_RADIUS
     print(f"Distance totale parcourue 25: {final_distance:.3f} m")
     break # quitte la boucle
  
# Affichage final
   

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
 pass

# Enter here exit cleanup code.
