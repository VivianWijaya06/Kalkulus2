# 📘 Proyek Numerik Python

Proyek ini mencakup implementasi fungsi turunan dan integral numerik beserta studi kasus.

## ✅ Metode yang Diimplementasikan

### Turunan Numerik
- Forward Difference
- Central Difference

### Integral Numerik
- Trapezoidal (n-order)
- Simpson's 1/3

---

## 📌 Kasus A – Titik Ekstrim Lokal

### Fungsi:
f(x) = x³ − 3x² + 2

### 1. Hitung Turunan Numerik f′(x)

```python
f = lambda x: x**3 - 3*x**2 + 2
df = lambda x: central_difference(f, x)
