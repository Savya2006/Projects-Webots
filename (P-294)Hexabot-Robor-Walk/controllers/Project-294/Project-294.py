from controller import Robot
import math
timestep=32

robot=Robot()

motorRPC =robot.getDevice("RPC")
motorRPF=robot.getDevice("RPF")
motorRMC= robot.getDevice("RMC")
motorRMF= robot.getDevice("RMF")
motorRAC= robot.getDevice("RAC")
motorRAF= robot.getDevice("RAF")

motorLPC= robot.getDevice("LPC")
motorLPF= robot.getDevice("LPF")
motorLMC= robot.getDevice("LMC")
motorLMF= robot.getDevice("LMF")
motorLAC= robot.getDevice("LAC")
motorLAF= robot.getDevice("LAF")

# frequency [Hz]
f = 0.5;

#y= a * sin(bx+c)+d
def getY(a, p, d):
    time = robot.getTime()
    return  a * math.sin(2.0 * math.pi * f * time + p) + d

while robot.step(timestep) != -1:
    time = robot.getTime();
    
    motorRPC.setPosition(getY(0.25,0,-0.6))
    motorRPF.setPosition(getY(0.2,2,0.8))
    
    motorRMC.setPosition(getY(-0.25,0,0))
    motorRMF.setPosition(getY(-0.2,2,0.8))
    
    motorRAC.setPosition(getY(0.25,0,0.6))
    motorRAF.setPosition(getY(0.2,2,0.8))
    
    motorLPC.setPosition(getY(0.25,0,0.6))
    motorLPF.setPosition(getY(-0.2,2,0.8))
    
    motorLMC.setPosition(getY(-0.25,0,0))
    motorLMF.setPosition(getY(0.2,2,0.8))
    
    motorLAC.setPosition(getY(0.25,0,-0.6))
    motorLAF.setPosition(getY(-0.2,2,0.8))
    
