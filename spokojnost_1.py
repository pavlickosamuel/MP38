with open('spokojnost_1.txt', 'r') as fr:
    hlasy = [r.strip() for r in fr if r.strip()]

print("Celkový počet vyjadrení:", len(hlasy))

h = {}      
h_n = {}    

for riadok in hlasy:
    cas, text = riadok.split()
    hodina = int(cas.split(":")[0])
    if hodina not in h:
        h[hodina] = 0
        h_n[hodina] = 0
    if text == "áno":
        h[hodina] += 1
    else:
        h_n[hodina] += 1

naj_s = max(h, key=h.get)
naj_n = max(h_n, key=h_n.get)
print("Najviac spokojných:", naj_s, "hod. -", h[naj_s])
print("Najviac nespokojných:", naj_n, "hod. -", h_n[naj_n])

print("Percentá spokojnosti:")
for hodina in sorted(h):
    spolu = h[hodina] + h_n[hodina]
    perc = h[hodina] / spolu * 100
    print(hodina, "hod. -", round(perc, 1), "%")