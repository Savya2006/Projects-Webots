from controller import Robot

bot = Robot()  #Instance Of Robot Class

timestep = 64  #Break Time/Time Delay

left_wheel = bot.getDevice('left_front_wheel') #getdevice: To Fetch
right_wheel = bot.getDevice('right_front_wheel')
l_steer = bot.getDevice('left_steer')
r_steer = bot.getDevice('right_steer')

left_wheel.setPosition(float('inf')) #infity: It Will Keep On Moving Continuously
right_wheel.setPosition(float('inf'))

l_steer.setPosition(0)
r_steer.setPosition(0)
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)

while bot.step(timestep) != -1:
    
    left_wheel.setVelocity(10)
    right_wheel.setVelocity(10)
    