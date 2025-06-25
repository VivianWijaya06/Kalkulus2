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
```


## 📌 Kasus B – Integral Tentu

### Fungsi dan Interval

- Fungsi:  
  \( f(x) = \sin(x) \)

- Interval:  
  \[ a = 0, \quad b = \frac{\pi}{2} \]

### 🧮 Metode Numerik yang Digunakan

1. **Metode Trapesium**
2. **Metode Simpson 1/3**

### 🔢 Hasil Perhitungan

```
Trapezoidal rule: 0.99783342
Simpson's rule:   1.00000339
Exact result:     1.0
```

### 📉 Error (Selisih terhadap solusi eksak)

- **Trapesium**:  
  \( |0.99783342 - 1.0| = 2.17 \times 10^{-3} \)

- **Simpson**:  
  \( |1.00000339 - 1.0| = 3.39 \times 10^{-6} \)

### 📊 Kesimpulan

- **Simpson's Rule** memberikan hasil yang lebih akurat dibandingkan dengan metode Trapesium untuk fungsi \( \sin(x) \) pada interval \([0, \frac{\pi}{2}]\).
- Error yang sangat kecil pada Simpson menunjukkan keunggulan metode ini untuk fungsi yang halus dan kontinu.
