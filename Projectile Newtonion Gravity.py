import numpy as np ###numeric python
import matplotlib.pyplot as plt ###matlab style plotting
import scipy.integrate as sci ##integration toolbox

##Constant parameters
G = 6.6742e-11  ##Gravitational constant (SI Units)
mass = .64 ##kg

##Different planets
Rplanet = 6357e3 #m        Earth
mplanet = 5.972e24 #kg     Earth
##Rplanet = 6051e3 #m      Venus
##mplanet = 4.867e24 #kg   Venus
##Rplanet = (142984/2) #m  Jupiter
##mplanet = 1898e24        Jupiter

##Gravitational acceleration model

def gravity(z):
    global Rplanet, mplanet

    r = np.sqrt(z**2)

    if r < Rplanet:
        accel = 0
    else:
        accel = G*mplanet/(r**3)*r

    return accel

def Derivatives(state,t):
    global mass

    #state vector
    z = state[0]
    zdot = state[1]

    ##Gravity Force
    gravityF = -gravity(z)*mass

    ##Thrust Force
    thrustF = 0

    ##Aerodynamics
    aeroF = 0


    Forces = gravityF + aeroF +  thrustF

    zddot = Forces/mass

    statedot = np.asarray([zdot,zddot])

    return statedot



###Simulation###

##Test Surface gravity
print('Surface Gravity (m/s^2) =',gravity(Rplanet))

#initial conditions
z0 = Rplanet ##m
zdot0 = 25*331.0 #m/s
stateinitial = np.asarray([z0, zdot0])
t = np.linspace(0,345,1000)

##Numerical integration 
stateout = sci.odeint(Derivatives,stateinitial,t)


##Final numbers
zFinal = stateout[:,0]
altitude = zFinal - Rplanet
zdotFinal = stateout[:,1]


##PLOT##

##Altitude
plt.plot(t,altitude)
plt.xlabel('Time (sec)')
plt.ylabel('altitude (m)')
plt.grid()


##Velocity
plt.figure()
plt.plot(t,zdotFinal)
plt.xlabel('Time (sec)')
plt.ylabel('Normal Speed (m/s)')
plt.grid


plt.show()


    




