import matplotlib.pyplot as plt
import numpy as np

# Titik Awal dan Titik Akhir
x0, y0 = 1, 2
x1, y1 = 3, 6

# Menghitung delta
dx = (x1 - x0) 
dy = (y1 - y0) 

# Inisialisasi
X = x0 
Y = y0 
tamp = [X] 
tamp2 = [Y]

# Menentukan arah pergerakan (untuk menangani garis dengan arah negatif)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1

# Parameter keputusan
if dx > dy:  # Jika slope < 1
    p = 2 * dy - dx  
    for _ in range(dx): 
        if p >= 0:
            Y += sy
            p -= 2 * dx 
        X += sx
        p += 2 * dy 
        tamp.append(X)
        tamp2.append(Y)
else:  # Jika slope >= 1
    p = 2 * dx - dy
    for _ in range(dy):
        if p >= 0:
            X += sx
            p -= 2 * dy
        Y += sy
        p += 2 * dx
        tamp.append(X)
        tamp2.append(Y)

# Menggambar garis
xpoints = np.array(tamp)
ypoints = np.array(tamp2)

plt.plot(xpoints, ypoints, '-o')
plt.title('Persamaan Garis dengan Algoritma Bresenham')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()