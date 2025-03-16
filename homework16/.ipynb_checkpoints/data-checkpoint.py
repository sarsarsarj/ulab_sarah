# Call this in a jupyter notebook!
# %pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

import torch
import numpy as np

# Underlying Pattern we are trying to find 
x_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)

pattern = np.sin(X) + np.cos(Y)

# Actual data that we will be using
# Defining the dataset dimensions
N, D_in, H, D_out = 1000, 2, 50, 1

# Creating the input data
x = torch.randn(N, D_in) * 3.1415
y = (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1)

noise = torch.randn(N, D_out) * 0.1
y += noise

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()