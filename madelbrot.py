import numpy as np
from js import document
import matplotlib.pyplot as plt
from matplotlib import cm

def mandelbrot(h, w, max_iter, x_min=-2, x_max=1, y_min=-1.5, y_max=1.5):
    x = np.linspace(x_min, x_max, w)
    y = np.linspace(y_min, y_max, h)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    z = np.zeros_like(c, dtype=np.complex128)
    output = np.zeros(c.shape, dtype=np.int32)

    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] * z[mask] + c[mask]
        output[mask] += 1
        output[~mask] = max_iter

    return output

def draw_mandelbrot(resolution=400, max_iter=100):
    # Generate Mandelbrot set
    mandel = mandelbrot(resolution, resolution, max_iter)
    
    # Create a plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(mandel, cmap='inferno', extent=[-2, 1, -1.5, 1.5])
    ax.axis('off')
    
    # Display on canvas
    canvas = document.getElementById('mandelbrot-canvas')
    plt.canvas.draw()
    canvas_data = plt.canvas.tostring_rgb()
    canvas.width = resolution
    canvas.height = resolution
    ctx = canvas.getContext('2d')
    img = document.createElement('img')
    img.src = f'data:image/png;base64,{canvas_data}'
    img.onload = lambda: ctx.drawImage(img, 0, 0, resolution, resolution)
    plt.close(fig)

# Initial render
draw_mandelbrot()