import gym
from stable_baselines3 import A2C ,PPO
import os
import time


models_dir = f'models/A2C-{int(time.time())}'
logdir = f'logs/A2C-{int(time.time())}'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
if not os.path.exists(logdir):
    os.makedirs(logdir)


game = 'CartPole-v1' 
env = gym.make(game)

env.reset()

model = A2C('MlpPolicy', env, verbose = 1, tensorboard_log = logdir)

TIMESTEPS = 10000
for i in range(1,100):
    model.learn(total_timesteps = TIMESTEPS, reset_num_timesteps= False, tb_log_name='A2C')
    model.save(f"{models_dir}/{TIMESTEPS*i}")

# episodes = 10



# for ep in range(episodes):
#     obs = env.reset()
#     done = False
    
#     while not done:
#         env.render()
#         obs, rewards, done, info = env.step(env.action_space.sample())
        

env.close()