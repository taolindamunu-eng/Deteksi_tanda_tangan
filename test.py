import cv2
import matplotlib.pyplot as plt

# Membaca gambar hasil crop tanda tangan
nama_gambar = cv2.imread("01_HighQuality_Enhanced.jpg")

# Mengubah gambar menjadi grayscale
hasil_grayscale = cv2.cvtColor(nama_gambar, cv2.COLOR_BGR2GRAY)

# Menampilkan hasil grayscale
plt.imshow(hasil_grayscale, cmap="gray")
plt.title("Hasil Grayscale")
plt.axis("off")
plt.show()