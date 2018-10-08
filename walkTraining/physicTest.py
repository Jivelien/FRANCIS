import pybullet
import time

def reset(step):
    pybullet.resetSimulation()
    pybullet.setGravity(0,0,-9.780318)
    pybullet.setRealTimeSimulation(1)
    pybullet.setTimeStep(step)

def plane():
    plane=pybullet.loadURDF("plane.urdf")

def francis(fixed):
    FRANCIS = pybullet.loadURDF("FRANCIS.urdf",useFixedBase=fixed)

def startSim():
    physicsClient = pybullet.connect(pybullet.GUI) #or p.DIRECT for non-graphical version
    reset(0.0001)
    francis(1)

def stopSim():
    pybullet.disconnect()
    
startSim()

for i in range(100):
    pybullet.setJointMotorControlArray(FRANCIS, range(1), pybullet.POSITION_CONTROL,targetPositions=[i*0.01] * 1)
    time.sleep(0.01)