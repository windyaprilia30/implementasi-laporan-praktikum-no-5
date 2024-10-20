n = 50
i = 0
jumlah_ganjil = 0
while i <= n:
    if i % 2 != 0:
        jumlah_ganjil += i
    i += 1
    print(f"jumlah deret bilangan ganjil dari 1 hingga {n} adalah {jumlah_ganjil}")

