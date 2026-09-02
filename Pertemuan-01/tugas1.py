h = float(input("Masukkan koordinat pusat h: "))
k = float(input("Masukkan koordinat pusat k: "))
r = float(input("Masukkan jari-jari lingkaran: "))
x = float(input("Masukkan koordinat titik x: "))
y = float(input("Masukkan koordinat titik y: "))

D = (x - h) * (x - h) + (y - k) * (y - k)
r2 = r * r

if D < r2:
    print("Titik berada di dalam lingkaran")
elif D == r2:
    print("Titik berada tepat pada lingkaran")
else:
    print("Titik berada di luar lingkaran")