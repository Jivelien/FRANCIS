import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI) #or p.DIRECT for non-graphical version
p.setGravity(0,0,-9.780318)
planeId = p.loadURDF("./plane.urdf")

cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("duck_vhacd.urdf",cubeStartPos, cubeStartOrientation)

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
    

cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)


# p.disconnect()
