import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    # Hitung delta perubahan
    dx = x2 - x1
    dy = y2 - y1
    
    # Tentukan jumlah langkah yang lebih besar, apakah perubahan di x atau di y
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    # Kemudian Hitung increment pada tiap langkah
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Lalu buat list untuk menyimpan titik-titik garis
    x_values = [x1]
    y_values = [y1]
    
    # Inisialisasi titik awal
    x = x1
    y = y1
    
    # Iterasi untuk membuat titik-titik garis
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        x_values.append(round(x))
        y_values.append(round(y))
    
    return x_values, y_values

# Titik awal dan akhir garis
x1, y1 = 1, 2
x2, y2 = 3, 6

# Selanjutnya dapatkan titik-titik garis menggunakan algoritma DDA
x_vals, y_vals = dda(x1, y1, x2, y2)

# Plot hasil garis
plt.plot(x_vals, y_vals, marker='o')
plt.title(f"Garis antara ({x1}, {y1}) dan ({x2}, {y2}) menggunakan DDA")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()