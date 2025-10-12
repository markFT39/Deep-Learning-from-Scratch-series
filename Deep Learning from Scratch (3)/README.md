# Deep Learning from Scratch (3) - DeZero and Advanced Deep Learning

This directory contains my code implementations and notes based on **"Deep Learning from Scratch 3"** by Goki Saito.  
This book focuses on building a deep learning framework called **DeZero** from scratch and exploring advanced concepts such as **automatic differentiation**, **higher-order gradients**, and **neural network construction**.  
It also introduces practical extensions including **GPU acceleration**, **model serialization**, and **modern network architectures (CNNs, RNNs)**.

📎 Related Link: [Repository](https://github.com/markFT39/Deep-Learning-from-Scratch-series)

---

## 📁 Contents
- **Chapter 1**: Automatic Differentiation (Stages 1–10)  
- **Chapter 2**: Writing Clear & Pythonic Code (Stages 11–24)  
- **Chapter 3**: Higher-Order Differentiation (Stages 25–36)  
- **Chapter 4**: Building Neural Networks from Scratch (Stages 37–51)  
- **Chapter 5**: DeZero Challenges and Practical Features (Stages 52–60, including GPU support, model saving/restoration, CNNs, RNNs)

---

## 💡 What I Learned (highlights)
- Implementing **automatic differentiation** and understanding computational graphs.  
- Designing a flexible and readable deep learning framework (**DeZero**) using object-oriented Python.  
- Extending differentiation to **higher-order derivatives** for advanced gradient methods.  
- Building full neural networks from core mathematical operations without external libraries.  
- Adding **GPU computation** support via CuPy integration.  
- Implementing practical deep learning models including **CNNs** and **RNNs**.  
- Building tools for **model saving, loading, and visualization** to support experimentation.

---

## 🛠 How to Run (examples)
Clone the repo and run chapter scripts inside the Book 3 folder:

```bash
git clone https://github.com/markFT39/Deep-Learning-from-Scratch-series.git
cd "Deep Learning from Scratch (3)"

# Example: Automatic Differentiation
cd ./steps
python step10.py

# Example: Higher-Order Differentiation
cd ./steps
python step30.py

# Example: Neural Network Implementation
cd ./steps
python step45.py
