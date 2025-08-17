import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random
import matplotlib.pyplot as plt

# Define the DQN (Deep Q-Network) architecture
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )

    def forward(self, x):
        return self.network(x)

# Define the Agent class
class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.state_dim = state_dim
        self.action_dim = action_dim
        
        # DQN network
        self.dqn = DQN(state_dim, action_dim)
        self.target_dqn = DQN(state_dim, action_dim)
        self.target_dqn.load_state_dict(self.dqn.state_dict())
        
        self.optimizer = optim.Adam(self.dqn.parameters(), lr=0.001)
        self.memory = deque(maxlen=10000)
        
        # Hyperparameters
        self.batch_size = 64
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.target_update = 10
        self.training_step = 0

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.action_dim)
        
        state = torch.FloatTensor(state).unsqueeze(0)
        q_values = self.dqn(state)
        return q_values.argmax().item()

    def train(self):
        if len(self.memory) < self.batch_size:
            return
        
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        current_q_values = self.dqn(states).gather(1, actions.unsqueeze(1))
        next_q_values = self.target_dqn(next_states).max(1)[0].detach()
        target_q_values = rewards + (1 - dones) * self.gamma * next_q_values
        
        loss = nn.MSELoss()(current_q_values.squeeze(), target_q_values)
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Update epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
        # Update target network
        self.training_step += 1
        if self.training_step % self.target_update == 0:
            self.target_dqn.load_state_dict(self.dqn.state_dict())

# Training loop
def train_agent():
    env = gym.make('CartPole-v1', render_mode='human')
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    
    agent = DQNAgent(state_dim, action_dim)
    episodes = 500
    scores = []
    
    for episode in range(episodes):
        state, _ = env.reset()
        score = 0
        done = False
        truncated = False
        
        while not (done or truncated):
            action = agent.act(state)
            next_state, reward, done, truncated, _ = env.step(action)
            
            # Custom reward function
            x, x_dot, theta, theta_dot = next_state
            r1 = (2.4 - abs(x)) / 2.4 - 0.8  # x_threshold is typically 2.4
            r2 = (0.2095 - abs(theta)) / 0.2095 - 0.5  # theta_threshold is typically 12 degrees (0.2095 radians)
            reward = r1 + r2
            
            agent.remember(state, action, reward, next_state, done)
            agent.train()
            
            state = next_state
            score += reward
            
        scores.append(score)
        
        # Print episode stats
        if (episode + 1) % 10 == 0:
            avg_score = np.mean(scores[-10:])
            print(f"Episode: {episode + 1}, Average Score: {avg_score:.2f}, Epsilon: {agent.epsilon:.2f}")
    
    env.close()
    return scores

if __name__ == "__main__":
    scores = train_agent()
    
    # Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(scores)
    plt.title('Training Progress')
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.show()
