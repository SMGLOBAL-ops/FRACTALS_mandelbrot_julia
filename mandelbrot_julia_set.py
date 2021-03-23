import numpy as np
import matplotlib.pyplot as plt
# size of fractal image plotted
min_x,max_x,min_y,max_y = -2,2,-1.2,1.2
width, height = 800,600
max_iter = 256
# Create a list of complex values in the plane
im,re = np.ogrid[min_y:max_y:height*1j,min_x:max_x:width*1j] 
c = (re + 1j*im).flatten()

# variables to store z and if the complex point
# is in the fractal set or not. Also to keep track of points 
# that have not yet diverged. 

fractal_set = np.zeros_like(c) + max_iter
live, = np.indices(c.shape)

# selecting desired fractal image
# Mandelbrot set
# Julia set: the initial values of z to be equal to the values of c , the complex plane.

pattern = int(input("select [1: Mandelbrot Set, 2: Julia Set] " + "\n"))

if (pattern == 1):
    z = np.zeros_like(c)
elif (pattern == 2):
    z = np.array(c)

for i in range(max_iter): 
    a = 2.98
    if (pattern == 1):
       # z = np.zeros_like(c)
        # z <- z^2 + c
        z[live] = z[live]**2 + c[live]
    elif (pattern == 2):
       # z = np.array(c)
        z[live] = z[live]**2 + 0.7885*np.exp(1j*a)
        
# Test if |z| > 5. If it is, c is *not* in the set
    escaped = abs(z[live]) > 5.0
    fractal_set[live[escaped]] = i
    # Ignore points that we already know are not in the set
    live = live[~escaped]
Z = abs(fractal_set.reshape((height, width)))
plt.axis('off')
plt.imshow(Z,cmap='jet',interpolation = 'bilinear',origin='lower') 
plt.show()

