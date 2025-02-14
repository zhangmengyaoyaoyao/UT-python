import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=1.0, epsilon_decay=0.995):
        self.q_table = {}
        self.lr = learning_rate  # How quickly the agent learns from new experiences
        self.gamma = discount_factor  # How much the agent values future rewards
        self.epsilon = epsilon  # How often the agent explores vs exploits
        self.epsilon_decay = epsilon_decay  # How quickly exploration decreases

    def discretize_state(self, state):
        # Convert continuous state to discrete state
        discrete_state = tuple(np.round(state, decimals=1))
        return discrete_state

    def get_action(self, state):
        discrete_state = self.discretize_state(state)
        # Exploration: random action
        if np.random.random() < self.epsilon:
            return np.random.choice([0, 1])
        # Exploitation: best known action
        if discrete_state not in self.q_table:
            return 0
        return np.argmax(self.q_table[discrete_state])

    def learn(self, state, action, reward, next_state, done):
        discrete_state = self.discretize_state(state)
        discrete_next_state = self.discretize_state(next_state)

        # Initialize Q-values if state is new
        if discrete_state not in self.q_table:
            self.q_table[discrete_state] = [0, 0]
        if discrete_next_state not in self.q_table:
            self.q_table[discrete_next_state] = [0, 0]

        # Q-learning update
        old_value = self.q_table[discrete_state][action]
        next_max = np.max(self.q_table[discrete_next_state])
        new_value = (1 - self.lr) * old_value + self.lr * (reward + self.gamma * next_max)
        self.q_table[discrete_state][action] = new_value

        # Decay exploration rate
        if done:
            self.epsilon *= self.epsilon_decay

def train_and_plot(agent, episodes=100):
    env = gym.make('CartPole-v1')
    rewards = []

    for episode in range(episodes):
        state, _ = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

        rewards.append(total_reward)
        if episode % 10 == 0:
            print(f'Episode {episode}, Score: {total_reward}, Epsilon: {agent.epsilon:.2f}')

    env.close()
    return rewards

# Train the agent with default parameters
agent = QLearningAgent()
rewards = train_and_plot(agent)

# Plot the results
plt.plot(rewards)
plt.title('Learning Progress')
plt.xlabel('Episode')
plt.ylabel('Score')
# plt.show()
plt.savefig('learning_progress.png')