import gym
from stable_baselines3 import PPO, A2C



game = 'CartPole-v1'
env = gym.make(game)

env.reset()

models_dir = 'models/PPO-1669389159'

model_path = f'{models_dir}/900000.zip'
model = PPO.load(model_path, env=env)

episodes = 10



for ep in range(episodes):
    obs = env.reset()
    done = False
    
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, rewards, done, info = env.step(env.action_space.sample())
        

env.close()