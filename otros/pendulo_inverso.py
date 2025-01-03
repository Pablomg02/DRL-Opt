import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


import os
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

eval_env = make_vec_env("CartPole-v1", n_envs=1)
model = PPO.load("models/cartpole/best_model", env=eval_env)

obs = eval_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = eval_env.step(action)
    eval_env.render("human")