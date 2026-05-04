from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time



def on_comm_error(e): print(e); os._exit(1)

global done 
      
def on_comm_error(error):
    print(error)
    os._exit(1)    # sortie forcée malgré les coroutines

def Indecis(node_id):
    
    print("Indecis")
    
    # Lecture des capteurs de proximité horizontau
    prox = th_1[node_id]["prox.horizontal"]

    # Moyennes des capteurs gauche / droite
    gauche=(prox[0]+prox[1])/2.0
    centre=(prox[2])
    droite=(prox[3]+prox[4])/2.0
       
    print(f"gauche ={gauche} centre ={centre} droite ={droite}")

    # Si aucun obstacle proche → avancer
    if gauche < 500 or centre < 500 and droite < 500: 
        th_1[node_id]["motor.left.target"]  = 200
        th_1[node_id]["motor.right.target"] = 200

    else:
    # Sinon → reculer
        th_1[node_id]["motor.left.target"]  = -200
        th_1[node_id]["motor.right.target"] = -200   

     
    
def obstine(node_id):
    global done
    print("obstine")
    
    # Lecture des capteurs de proximité horizontau
    prox1 = th_2[node_id]["prox.horizontal"]

   
    gauche1=(prox1[0]+prox1[1])/2.0
    centre1=(prox1[2])
    droite1=(prox1[3]+prox1[4])/2.0
    arriere= (prox1[5]+prox1[6])/2.0
   
    # Si obstacle devant → reculer   
    print(f"gauche ={gauche1} centre ={centre1} droite ={droite1}")

    if gauche1 > 500 or centre1 > 500 or droite1 >500: 
        th_2[node_id]["motor.left.target"]  = -200
        th_2[node_id]["motor.right.target"] = -200

    # Si obstacle derrière → avancer
    elif arriere > 500 :
        th_2[node_id]["motor.left.target"]  = 200
        th_2[node_id]["motor.right.target"] = 200   

def ar_rep(node_id):
    global done
    print("obstine")

    prox2 = th_3[node_id]["prox.horizontal"]

    gauche2=(prox2[0]+prox2[1])/2.0
    centre2=(prox2[2])
    droite2=(prox2[3]+prox2[4])/2.0
    arriere2= (prox2[5]+prox2[6])/2.0
   
        
    print(f"gauche ={gauche2} centre ={centre2} droite ={droite2}")
    
    # Si obstacle derrière → avancer
    if  arriere2>500: 
        th_3[node_id]["motor.left.target"]  = 200
        th_3[node_id]["motor.right.target"] = 200
    # Sinon → s'arrêter
    else :
        th_3[node_id]["motor.left.target"]  = 0
        th_3[node_id]["motor.right.target"] = 0   
   

# Détection automatique des ports série
thymio_serial_ports = ThymioSerialPort.get_ports()
# Connexion robot 1
serial_port=thymio_serial_ports[0].device
th_1= Thymio(use_tcp=False, serial_port=serial_port,
         refreshing_coverage={"prox.horizontal", "button.center","prox.ground.delta","acc"})
# Connexion robot 2
serial_port_1=thymio_serial_ports[1].device
th_2= Thymio(use_tcp=False, serial_port=serial_port_1,
         refreshing_coverage={"prox.horizontal", "button.center","prox.ground.delta","acc"})
# Connexion robot 3 
serial_port2=thymio_serial_ports[2].device
th_3= Thymio(use_tcp=False, serial_port=serial_port2,
         refreshing_coverage={"prox.horizontal", "button.center","prox.ground.delta","acc"})
# Assignation des handlers d'erreur
th_1.on_comm_error = on_comm_error 
th_2.on_comm_error = on_comm_error 
th_3.on_comm_error = on_comm_error 
# Connexion physique
th_1.connect()
th_2.connect()
th_3.connect()
# Récupération des identifiants des robots
id1 = th_1.first_node()
id2 = th_2.first_node()
id3= th_3.first_node()




done =False
# Chaque robot surveille ses capteurs et appelle sa fonction
th_1.set_variable_observer(id1, Indecis)
th_2.set_variable_observer(id2, obstine)
th_3.set_variable_observer(id3, ar_rep)

    

while not done: # attendre que tous soient done
    time.sleep(0.1) # boucle principale

#dECONNEXION: 
th_1.disconnect() 
th_2.disconnect()  
th_3.disconnect()   

   
