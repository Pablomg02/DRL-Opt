import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


import gymnasium as gym
import numpy as np
import os
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

path = "models/bipedal_good"
env_id = "BipedalWalker-v3"

eval_env = make_vec_env(env_id, n_envs=1)

model = PPO.load(f"{path}/best_model", env=eval_env)

obs = eval_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = eval_env.step(action)
    eval_env.render("human")