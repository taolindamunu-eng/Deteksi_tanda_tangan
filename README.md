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
