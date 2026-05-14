import time
import random
import math
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import ScalarFormatter, LogFormatterExponent

sys.setrecursionlimit(1000000)

RULARI_MICI = 1000
PRAG_MICI   = 1000


def bubble_sort(lista, timp_start):
    n = len(lista)
    for i in range(n):
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        already_sorted = True
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                already_sorted = False
        if already_sorted:
            break
    return lista

def shaker_sort(lista, timp_start):
    start = 0
    end   = len(lista) - 1
    while start < end:
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        swapped = False
        for i in range(start, end):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
        if not swapped:
            break
        start += 1
    return lista

def insertion_sort(lista, timp_start):
    for i in range(1, len(lista)):
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        key_item = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key_item:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key_item
    return lista

def selection_sort(lista, timp_start):
    for i in range(len(lista)):
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def shell_sort(lista, timp_start):
    n   = len(lista)
    gap = n // 2
    while gap > 0:
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista

def merge_sort(lista, timp_start):
    if time.time() - timp_start > 10:
        return "TIMEOUT"
    if len(lista) <= 1:
        return lista
    mid     = len(lista) // 2
    stanga  = merge_sort(lista[:mid], timp_start)
    dreapta = merge_sort(lista[mid:], timp_start)
    if stanga == "TIMEOUT" or dreapta == "TIMEOUT":
        return "TIMEOUT"
    rezultat = []
    i = j = 0
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i]); i += 1
        else:
            rezultat.append(dreapta[j]); j += 1
    rezultat += stanga[i:]
    rezultat += dreapta[j:]
    return rezultat

def quick_sort(lista, timp_start):
    if time.time() - timp_start > 10:
        return "TIMEOUT"
    if len(lista) <= 1:
        return lista
    pivot  = lista[len(lista) // 2]
    mici   = [x for x in lista if x < pivot]
    egale  = [x for x in lista if x == pivot]
    mari   = [x for x in lista if x > pivot]
    st = quick_sort(mici, timp_start)
    dr = quick_sort(mari, timp_start)
    if st == "TIMEOUT" or dr == "TIMEOUT":
        return "TIMEOUT"
    return st + egale + dr

def heapify(lista, n, i, timp_start):
    if time.time() - timp_start > 10:
        return False
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2
    if left < n and lista[left] > lista[largest]:
        largest = left
    if right < n and lista[right] > lista[largest]:
        largest = right
    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest, timp_start)
    return True

def heap_sort(lista, timp_start):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        if not heapify(lista, n, i, timp_start):
            return "TIMEOUT"
    for i in range(n - 1, 0, -1):
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        lista[0], lista[i] = lista[i], lista[0]
        if not heapify(lista, i, 0, timp_start):
            return "TIMEOUT"
    return lista

def counting_sort_for_radix(lista, exp):
    n      = len(lista)
    output = [0] * n
    count  = [0] * 10
    for i in range(n):
        index = lista[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = lista[i] // exp
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista, timp_start):
    if len(lista) == 0:
        return lista
    maxim = max(lista)
    exp   = 1
    while maxim // exp > 0:
        if time.time() - timp_start > 10:
            return "TIMEOUT"
        counting_sort_for_radix(lista, exp)
        exp *= 10
    return lista

def tim_sort(lista, timp_start):
    if time.time() - timp_start > 10:
        return "TIMEOUT"
    lista.sort()
    return lista




def genereaza_date(n, tip):
    lista_rezultat = []
    if tip == "Aleatoare":
        for i in range(n):
            lista_rezultat.append(random.randint(0, 1000000))
    elif tip == "Sortate":
        for i in range(n):
            lista_rezultat.append(i)
    elif tip == "Invers":
        for i in range(n, 0, -1):
            lista_rezultat.append(i)
    elif tip == "Aproape":
        for i in range(n):
            lista_rezultat.append(i)
        numar_schimbari = max(1, n // 20)
        for _ in range(numar_schimbari):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            lista_rezultat[a], lista_rezultat[b] = lista_rezultat[b], lista_rezultat[a]
    else:
        for i in range(n):
            lista_rezultat.append(random.randint(0, 10))
    return lista_rezultat




def masoara(func, orig):
    n = len(orig)
    if n < PRAG_MICI:
        timpi = []
        for _ in range(RULARI_MICI):
            copie = orig[:]
            t1 = time.time()
            rezultat = func(copie, time.time())
            dt = time.time() - t1
            if rezultat == "TIMEOUT":
                return "TIMEOUT"
            timpi.append(dt)
        return sum(timpi) / len(timpi)
    else:
        copie = orig[:]
        t1 = time.time()
        rezultat = func(copie, t1)
        dt = time.time() - t1
        if rezultat == "TIMEOUT":
            return "TIMEOUT"
        return dt



def genereaza_grafic(date_grafic, algoritmi, titlu, nume_fisier):
    plt.figure(figsize=(12, 8))
    for algo in algoritmi:
        nume    = algo[0]
        culoare = algo[2]
        if len(date_grafic[nume]["x"]) > 0:
            plt.plot(
                date_grafic[nume]["x"],
                date_grafic[nume]["y"],
                label=nume,
                color=culoare,
                marker='o',
                linewidth=2
            )
    plt.xscale('log')
    plt.yscale('log')
    plt.gca().xaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: {
            10: '10', 20: '20', 50: '50',
            100: '100', 1000: '1K', 10000: '10K',
            100000: '100K', 1000000: '1M'
        }.get(int(x), str(int(x))))
    )
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda y, _: f'{y:.6f}' if y < 0.0001 else
                                       f'{y:.5f}' if y < 0.001  else
                                       f'{y:.4f}' if y < 0.01   else
                                       f'{y:.3f}')
    )
    plt.title(titlu, fontsize=14)
    plt.xlabel("Numar elemente", fontsize=12)
    plt.ylabel("Timp mediu (secunde)", fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(nume_fisier, dpi=300)
    plt.close()
    print(f"Grafic salvat: {nume_fisier}")



def experiment():
    dimensiuni   = [10, 20, 50, 100, 1000, 10000, 100000, 1000000]
    tipuri_liste = ["Aleatoare", "Sortate", "Invers", "Aproape", "Plate"]

    algoritmi = [
        ("Bubble",   bubble_sort,    "#e6194b"),
        ("Shaker",   shaker_sort,    "#f58231"),
        ("Insertie", insertion_sort, "#cccc00"),
        ("Selectie", selection_sort, "#3cb44b"),
        ("Shell",    shell_sort,     "#00b4d8"),
        ("Merge",    merge_sort,     "#4363d8"),
        ("Quick",    quick_sort,     "#911eb4"),
        ("Heap",     heap_sort,      "#f032e6"),
        ("Radix",    radix_sort,     "#a05000"),
        ("TimSort",  tim_sort,       "#000000"),
    ]

    date_per_tip = {}
    for tip in tipuri_liste:
        date_per_tip[tip] = {}
        for algo in algoritmi:
            date_per_tip[tip][algo[0]] = {"x": [], "y": [], "col": algo[2]}

    print("\n" + "=" * 145)
    sir_header = f"{'N (Marime)':<12} | {'Tip Lista':<12} | "
    for algo in algoritmi:
        sir_header += f"{algo[0]:<9} | "
    print(sir_header)
    print("-" * 145)

    for n in dimensiuni:
        for tip in tipuri_liste:
            orig       = genereaza_date(n, tip)
            rand_timpi = []
            for algo in algoritmi:
                nume = algo[0]
                func = algo[1]
                dt   = masoara(func, orig)
                if dt == "TIMEOUT":
                    rand_timpi.append("TIMEOUT")
                else:
                    rand_timpi.append(f"{dt:.6f}")
                    date_per_tip[tip][nume]["x"].append(n)
                    date_per_tip[tip][nume]["y"].append(dt)
            sir_rand = f"{str(n):<12} | {tip:<12} | "
            for t in rand_timpi:
                sir_rand += f"{t:<9} | "
            print(sir_rand)
        print("-" * 145)

    prefix = "lap_"
    titluri = {
        "Aleatoare": "Algoritmi de Sortare - Date Aleatoare (Average Case)",
        "Sortate":   "Algoritmi de Sortare - Date Sortate (Best Case)",
        "Invers":    "Algoritmi de Sortare - Date Invers Sortate (Worst Case)",
        "Aproape":   "Algoritmi de Sortare - Date Aproape Sortate",
        "Plate":     "Algoritmi de Sortare - Date Plate (Valori Repetate)",
    }
    for tip in tipuri_liste:
        genereaza_grafic(
            date_per_tip[tip],
            algoritmi,
            titluri[tip],
            f"{prefix}{tip.lower()}.png"
        )

    print("\nGata! Fisiere generate.")


if __name__ == "__main__":
    experiment()