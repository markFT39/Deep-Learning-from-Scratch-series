# Deep Learning from Scratch (5) – Generative Models

This directory contains my code implementations and notes based on **"Deep Learning from Scratch (5)"** by Goki Saito.  
This book focuses on **generative modeling**, starting from classical probabilistic models and extending to modern deep generative models such as **VAEs and diffusion models**.  

All implementations are built step by step using **NumPy and Python**, emphasizing mathematical intuition and algorithmic understanding rather than relying on high-level frameworks.

📎 Related Link: [Repository](https://github.com/markFT39/Deep-Learning-from-Scratch-series)

---

## 📁 Contents
- **Chapter 1**: Normal Distributions  
- **Chapter 2**: Maximum Likelihood Estimation (MLE)  
- **Chapter 3**: Multivariate Normal Distributions  
- **Chapter 4**: Mixture of Gaussians (GMM)  
- **Chapter 5**: Expectation-Maximization (EM) Algorithm  
- **Chapter 6**: Neural Networks for Generative Models  
- **Chapter 7**: Variational Autoencoders (VAE)  
- **Chapter 8**: Diffusion Models - Theory  
- **Chapter 9**: Diffusion Models - Implementation  
- **Chapter 10**: Diffusion Models - Applications  

*(Chapters may be updated as I progress through the book.)*

---

## 💡 What I Learned (highlights)
- Modeling data distributions using **probability theory** and Gaussian distributions.  
- Estimating model parameters through **Maximum Likelihood Estimation (MLE)**.  
- Extending univariate models to **multivariate Gaussian distributions**.  
- Understanding and implementing **Gaussian Mixture Models (GMMs)**.  
- Applying the **Expectation-Maximization (EM)** algorithm for latent variable models.  
- Connecting classical probabilistic models with **neural network-based generative models**.  
- Implementing **Variational Autoencoders (VAEs)** from scratch and understanding the role of latent variables and KL divergence.  
- Learning the theoretical foundations of **diffusion models** (forward noising process and reverse denoising process).  
- Building diffusion models step by step and applying them to **data and image generation tasks**.  
- Understanding why diffusion models have become a core technique in modern generative AI.

---

## 🛠 How to Run (examples)
Clone the repo and execute chapter scripts inside the Book 5 folder:

```bash
git clone https://github.com/markFT39/Deep-Learning-from-Scratch-series.git
cd "Deep Learning from Scratch (5)"

# Example: Chapter 1
cd ./step01
python norm_dist.py

# Example: Chapter 5
cd ./step05
python em.py

# Example: Chapter 7
cd ./step07
python vae.py

# Example: Chapter 9
cd ./step09
python diffusion_model.py

