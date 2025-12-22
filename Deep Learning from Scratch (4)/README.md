# Deep Learning from Scratch (4) – Reinforcement Learning

This directory contains my code implementations and notes based on **"Deep Learning from Scratch (4)"** by Goki Saito.  
This book focuses on **reinforcement learning (RL)** fundamentals and key algorithms.  
All implementations use only NumPy and Python (no high-level DL framework) to explore RL from first principles.

📎 Related Link: [Repository](https://github.com/markFT39/Deep-Learning-from-Scratch-series)

---

## 📁 Contents
- **Chapter 1**: Bandit Problems  
- **Chapter 2**: Markov Decision Processes (MDP)  
- **Chapter 3**: Bellman Equations  
- **Chapter 4**: Dynamic Programming (policy evaluation, policy/value iteration)  
- **Chapter 5**: Monte Carlo Methods  
- **Chapter 6**: Temporal-Difference (TD) Methods (SARSA, Q-learning, etc.)  
- **Chapter 7**: Neural Networks and Q-learning  
- **Chapter 8**: Deep Q-Network (DQN) - implementation, core techniques, extensions  
- **Chapter 9**: Policy Gradient Methods (REINFORCE, Actor-Critic, etc.)  
- **Chapter 10**: One Step Further - DQN extensions (Rainbow, Noisy), case studies, challenges & possibilities  

*(Chapters may be updated as I progress through the book.)*

---

## 💡 What I Learned (highlights)
- Understanding the **reinforcement learning framework**: agent ↔ environment ↔ reward ↔ policy.  
- Implementing **bandit problems** and basic **exploration strategies**.  
- Formalizing **Markov Decision Processes (MDP)** and deriving **Bellman equations**.  
- Applying **dynamic programming**: policy evaluation, policy iteration, value iteration.  
- Learning and comparing **Monte Carlo methods** and **Temporal-Difference (TD) methods**.  
- Integrating **neural networks** into **Q-learning** for larger state/action spaces.  
- Building a **Deep Q-Network (DQN)** from scratch — **experience replay**, **target networks**, and extensions.  
- Exploring **policy gradient** and **Actor-Critic methods** for policy optimization.  
- Reviewing advanced RL topics: **Double DQN**, **Dueling Networks**, **Prioritized Replay**, and **continuous control** scenarios.  

---

## 🛠 How to Run (examples)
Clone the repo and execute chapter scripts inside the Book 4 folder:

```bash
git clone https://github.com/markFT39/Deep-Learning-from-Scratch-series.git
cd "Deep Learning from Scratch (4)"

# Example: Chapter 1
cd ./Ch01
python bandit.py

# Example: Chapter 4
cd ./Ch04
python dp.py

# Example: Chapter 8
cd ./Ch08
python dqn.py


