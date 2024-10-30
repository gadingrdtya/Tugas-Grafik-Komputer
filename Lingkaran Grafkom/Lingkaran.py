import matplotlib.pyplot as plt
import numpy as np

# Definisikan nilai a, b, dan r
a = 12  # Koordinat x dari titik tengah
b = 8   # Koordinat y dari titik tengah
r = 7   # Jari-jari lingkaran

# Hitung koordinat titik pada lingkaran
theta = np.linspace(0, 2 * np.pi, 100)  # Hasil nilai theta
x = a + r * np.cos(theta)  # Menghitung nilai x
y = b + r * np.sin(theta)  # Menghitung nilai y

# Membuat visualisasi
plt.figure(figsize=(6, 6))  # Menentukan ukuran gambar
plt.plot(x, y)  # Menggambar lingkaran
plt.scatter(a, b, color='green', label=f'Titik Pusat ({a}, {b})')  # Menampilkan titik pusat

# Menambahkan informasi tentang jari-jari
plt.plot([a, a + r], [b, b], 'k--')  # Menggambar garis jari-jari
plt.text(a + r/2, b, f'Jari-jari = {r}', color='red', ha='center', va='bottom')  # Menambahkan teks jari-jari

# Susun plot
plt.title('Gambar Persamaan Lingkaran')  # Judul grafik
plt.xlabel("X") # Sumbu X
plt.ylabel("Y") # Sumbu Y
plt.grid(True)  # Menampilkan grid
plt.axis('equal')  # Memastikan lingkaran tidak tampak oval/lonjong
plt.legend()  # Menampilkan legenda
plt.show()  # Menampilkan visualisasi