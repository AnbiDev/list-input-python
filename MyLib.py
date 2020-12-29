import Globals
import math
import statistics

def loopListOutput():
    while True:
        angka = int(input())
        if angka != 0:
            Globals.list_output.append(angka)
        else:
            break
    print(Globals.list_output) 

def calculateList():
    L = list(map(int, input().split(" ")))
    print(L)
    
    Globals.angka_sum = sum(L)
    Globals.angka_avg = statistics.mean(L)
    Globals.angka_med = statistics.median(L)
    Globals.angka_min = min(L)
    Globals.angka_max = max(L)

    print(Globals.angka_sum)
    print(Globals.angka_avg)
    print(Globals.angka_med)
    print(Globals.angka_min)
    print(Globals.angka_max)

def winningChance():
    list_tahun = list(map(int, input().split(" ")))

    for tahun in list_tahun:
        if tahun > 1990 and tahun < 2020:
            if tahun % 2 == 1:
                Globals.winning_count += 1

    print(Globals.winning_count)
