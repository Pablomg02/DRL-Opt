import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


import gymnasium as gym
import numpy as np
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
import torch.nn as nn

import highway_env


num_cpu = 8  # Number of processes to use
test_num_cpu = 1
path = "models"

net_arch = [128, 128]
activation_fn = nn.Tanh
total_timesteps = 500000

"""
gamma = 0.995
learning_rate = 0.000268
ent_coef = 0.001
batch_size = 512
clip_range = 0.3
gae_lambda = 0.98
max_grad_norm = 5.0
n_epochs = 20
n_steps = 32
vf_coef = 0.754843
"""



env_id = "Acrobot-v1"

if __name__ == "__main__":


    vec_env = make_vec_env(env_id, n_envs=num_cpu)

    eval_env = make_vec_env(env_id, n_envs=1)

    eval_callback = EvalCallback(eval_env, best_model_save_path=path,
                                log_path=path, eval_freq=20000 // num_cpu,
                                n_eval_episodes=7, deterministic=True,
                                render=False)

    model = PPO("MlpPolicy", vec_env, verbose=0, tensorboard_log=path)

    model.learn(total_timesteps=total_timesteps, progress_bar=True, callback=eval_callback, tb_log_name="TB_LOG")
    #model.learn(total_timesteps=total_timesteps, progress_bar=True,)

    mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=30)

    print(f"mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")

    