import gymnasium as gym
import numpy as np
import matplotlib.pyplot as	plt
from time import sleep
    
env = gym.make('CartPole-v1', render_mode='human')
state,	_ = env.reset()
# Watch random actions
for _ in range(1000):
    action = env.action_space.sample()    #Random action
    state, reward, terminated, truncated, _	= env.step(action)
    if terminated or truncated:
        print('The cartpole has tipped over!')
        sleep(2)
        state,	_ = env.reset()
env.close()

# Think About It:	What happens when you run this code? Why does the pole fall so quickly?
# The pole falls quickly(within 0.5sec) everytime. The reason is that the direction of the car is chosen randomly, not changing with the movement of the pole. The car needs strategies to change its moving direction to keep the pole balanced. For example, if the pole is about to fall to the left, the cart moves to the left; if it is about to fall to the right, the movement direction is the opposite.