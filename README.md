# Signature Detection

Mini project ini merupakan sistem sederhana untuk mendeteksi keberadaan tanda tangan kepala sekolah pada citra dokumen.

Sistem menggunakan metode pengolahan citra dengan tahapan cropping, grayscale, thresholding, morphological operation, dan perhitungan jumlah piksel foreground.

## Metode

Tahapan yang digunakan dalam program:

1. Crop area tanda tangan kepala sekolah.
2. Konversi citra menjadi grayscale.
3. OCR cleaning untuk menghilangkan area teks.
4. Global threshold.
5. Adaptive threshold.
6. Morphological opening.
7. Morphological closing.
8. Menghitung jumlah piksel foreground.
9. Menghitung persentase foreground.
10. Menentukan hasil:
   - `SIGNATURE PRESENT`
   - `SIGNATURE ABSENT`

## Dataset

Dataset terdiri dari:

- 9 citra tanpa tanda tangan (`SIGNATURE ABSENT`)
- 9 citra dengan tanda tangan (`SIGNATURE PRESENT`)

Total terdapat 18 citra yang digunakan untuk pengujian.

## Requirements

Program membutuhkan:

- Python 3.x
- OpenCV
- NumPy
- Pytesseract
- Tesseract OCR

## Instalasi

Install library Python dengan perintah:

```bash
pip install opencv-python numpy pytesseract

## Cara Menjalankan Program

1. Pastikan Python 3.x dan Tesseract OCR sudah terinstall.

2. Install library yang diperlukan:
   pip install opencv-python numpy pytesseract

3. Buka file test.py dan tentukan gambar yang ingin diuji pada bagian:
   IMAGE_PATH = r"SIGNATURE ABSENT\gambar 1.jpg"

4. Untuk menguji gambar dengan tanda tangan, gunakan:
   IMAGE_PATH = r"SIGNATURE PRESENT\gambar(1).jpeg"

5. Jalankan program melalui terminal:
   python test.py

6. Program akan menampilkan hasil analisis pada terminal dan visualisasi
   tahapan pengolahan citra.

7. Hasil visualisasi akan disimpan pada folder:
   Hasil/
