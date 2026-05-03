"""controler_parano1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
mL = robot.getDevice('motor.left')
mR = robot.getDevice('motor.right')
mL.setPosition(float('inf'))
mR.setPosition(float('inf'))
mL.setVelocity(0.0)
mR.setVelocity(0.0)

ds = []
for i in range(7):
 d = robot.getDevice('prox.horizontal.'+str(i))
 d.enable(timestep)
 ds.append(d)

#Led 
led = robot.getDevice('leds.top')
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    vals = [ds[i].getValue() for i in range(7)]
    
    
    gauche = (vals[0] + vals[1]) / 2.0
    centre = vals[2]
    droite = (vals[3] + vals[4]) / 2.0
    vitesse_max=9
    k=vitesse_max/3950
    print("Capteur Timide1")
    print("Gauche:",gauche) 
    print("droite:",droite) 
    print("centre:",centre )
    
    # Process sensor data here.
    if gauche > 1500 and centre >1500 and droite >1500: 
        mL.setVelocity(0.0) 
        mR.setVelocity(0.0) 
        led.set(0xFF0000) # rouge
    
    else: 
    # --- MODULATION DE VITESSE --- 
    
        if gauche > droite and gauche > centre:
            # obstacle surtout à gauche → tourner à droite
            if gauche<1500 :
                vitesse = vitesse_max-k*gauche
                mL.setVelocity(-vitesse/2)
                mR.setVelocity(vitesse)
                led.set(0x00FF00) # vert
            else:
                mL.setVelocity(0.0)
                mR.setVelocity(0.0)
                led.set(0xFF0000) # rouge
            
        elif droite > gauche and droite > centre:
        # obstacle surtout à droite → tourner à gauche
            if droite <1500 :
                vitesse = vitesse_max-k*droite
                mL.setVelocity(vitesse)
                mR.setVelocity(-vitesse/2)
                led.set(0x00FF00) # vert
            else:
                mL.setVelocity(0.0)
                mR.setVelocity(0.0)
                led.set(0xFF0000) # rouge
            
        elif centre > gauche and centre > droite:
        # obstacle surtout devant → reculer ou tourner
            if centre<1500 :
                vitesse = vitesse_max-k*centre
                mL.setVelocity(vitesse)
                mR.setVelocity(vitesse)
                led.set(0x00FF00) # vert
            else :
                mL.setVelocity(0.0)
                mR.setVelocity(0.0)
                led.set(0xFF0000) # rouge
        
        else :
            vitesse = vitesse_max-k*((droite*2.0 + gauche*2.0+ centre))/3.0
            mL.setVelocity(vitesse)
            mL.setVelocity(vitesse)
            led.set(0x00FF00) # vert
                
        
        # rien de dominant → avancer
        
        
        
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        pass
        
        # Enter here exit cleanup code.
        