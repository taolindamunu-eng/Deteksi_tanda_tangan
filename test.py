import cv2
import matplotlib.pyplot as plt
import pytesseract
import os

# ==========================================
# LOKASI TESSERACT
# ==========================================
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# ==========================================
# INPUT
# ==========================================
path = "SIGNATURE PRESENT/gambar(9).jpeg"
print("File ditemukan:", os.path.exists(path),":",path)
image = cv2.imread(path)
if image is None:
    print("Gambar gagal dibaca.")
    exit()

# ==========================================
# FOLDER HASIL
# ==========================================
os.makedirs("Hasil", exist_ok=True)
nama_file = os.path.splitext(
    os.path.basename(path)
)[0]

# ==========================================
# GRAYSCALE
# ==========================================
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# ==========================================
# OCR
# OCR hanya ditampilkan di terminal
# ==========================================
data = pytesseract.image_to_data(
    gray,
    config="--psm 6",
    output_type=pytesseract.Output.DICT
)

# Salinan grayscale untuk menghapus teks
gray_clean = gray.copy()
jumlah_teks = 0
print("\n" + "=" * 60)
print("                         HASIL OCR")
print("=" * 60)
print(
    f"{'No.':<6}"
    f"{'Teks':<30}"
    f"{'Confidence':>15}"
)
print("-" * 60)
for i in range(len(data["text"])):
    text = data["text"][i].strip()
    confidence = float(data["conf"][i])

    if text != "" and confidence > 30:
        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]
        jumlah_teks += 1

        # Menampilkan hasil OCR
        print(
            f"{jumlah_teks:<6}"
            f"{text:<30}"
            f"{confidence:>14.2f}%"
        )

        # Padding area teks
        padding = 3
        x1 = max(0, x - padding)
        y1 = max(0, y - padding)
        x2 = min(gray.shape[1], x + w + padding)
        y2 = min(gray.shape[0], y + h + padding)

        # Menghapus teks dari citra
        gray_clean[y1:y2, x1:x2] = 255
print("-" * 60)
print(
    f"{'Jumlah teks terdeteksi OCR:':<35}"
    f"{jumlah_teks:>20}"
)
print("=" * 60)

# ==========================================
# NORMALISASI PENCAHAYAAN / BACKGROUND
# ==========================================

# Estimasi background menggunakan Gaussian Blur
background = cv2.GaussianBlur(
    gray_clean,
    (51, 51),
    0
)

# Mengurangi pengaruh background
normalized = cv2.divide(
    gray_clean,
    background,
    scale=255
)

# Menyesuaikan kontras hasil normalisasi
normalized = cv2.normalize(
    normalized,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

# ==========================================
# GLOBAL THRESHOLD
# ==========================================
global_threshold_value = 128
_,  binary_global = cv2.threshold(
    normalized,
    global_threshold_value,
    255,
    cv2.THRESH_BINARY_INV
)

# ==========================================
# OTSU THRESHOLD
# ==========================================
otsu_threshold, binary_otsu = cv2.threshold(
    normalized,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# ==========================================
# MORPHOLOGICAL OPERATION
# ==========================================
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3, 3)
)

# ------------------------------------------
# Opening
# ------------------------------------------
opening = cv2.morphologyEx(
    binary_otsu,
    cv2.MORPH_OPEN,
    kernel
)

# ------------------------------------------
# Closing
# ------------------------------------------
closing = cv2.morphologyEx(
    opening,
    cv2.MORPH_CLOSE,
    kernel
)

# ==========================================
# HITUNG FOREGROUND
# ==========================================
foreground = cv2.countNonZero(closing)
total = closing.shape[0] * closing.shape[1]
percentage = (
    foreground / total
) * 100

# ==========================================
# DETEKSI TANDA TANGAN
# ==========================================
threshold_signature = 3.0
if percentage > threshold_signature:
    status = "SIGNATURE PRESENT"
else:
    status = "SIGNATURE ABSENT"

# ==========================================
# HASIL ANALISIS TANDA TANGAN
# ==========================================
print("\n" + "=" * 60)
print("             HASIL ANALISIS TANDA TANGAN")
print("=" * 60)
print(
    f"{'Parameter':<35}"
    f"{'Nilai':>20}"
)
print("-" * 60)
print(
    f"{'Threshold Global':<35}"
    f"{global_threshold_value:>20}"
)
print(
    f"{'Threshold Otsu':<35}"
    f"{otsu_threshold:>20.1f}"
)
print(
    f"{'Jumlah Foreground Pixel':<35}"
    f"{foreground:>20,}"
)
print(
    f"{'Total Pixel':<35}"
    f"{total:>20,}"
)
print(
    f"{'Persentase Foreground':<35}"
    f"{percentage:>19.2f}%"
)
print("-" * 60)
print(
    f"{'Status':<35}"
    f"{status:>20}"
)
print("=" * 60)

# ==========================================
# TAMPILKAN HASIL UTAMA
# ==========================================
fig = plt.figure(figsize=(16, 8))
images = [
    (
        cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        ),
        "Gambar Asli"
    ),

    (
        gray,
        "Grayscale"
    ),

    (
        binary_global,
        "Global Threshold"
    ),

    (
        binary_otsu,
        "Otsu Threshold"
    ),

    (
        opening,
        "Morphological Opening"
    ),

    (
        closing,
        "Morphological Closing"
    )
]

# ==========================================
# TAMPILKAN 6 HASIL
# ==========================================

for i, (img, title) in enumerate(images, 1):

    plt.subplot(2, 3, i)

    plt.imshow(
        img,
        cmap="gray"
    )

    plt.title(
        title,
        pad=15
    )

    plt.axis("off")


plt.subplots_adjust(
    hspace=0.4,
    wspace=0.15
)

# ==========================================
# SIMPAN HASIL
# ==========================================
output_path = os.path.abspath(
    os.path.join(
        "Hasil",
        nama_file + "_hasil.png"
    )
)
fig.savefig(
    output_path,
    dpi=150,
    bbox_inches="tight"
)
# ==========================================
# TAMPILKAN GAMBAR
# ==========================================

plt.show()

plt.close()