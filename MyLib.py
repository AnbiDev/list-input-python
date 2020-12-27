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
    
    Globals.list_sum = sum(L)
    Globals.list_avg = statistics.mean(L)
    Globals.list_med = statistics.median(L)
    Globals.list_min = min(L)
    Globals.list_max = max(L)

    print(Globals.list_sum)
    print(Globals.list_avg)
    print(Globals.list_med)
    print(Globals.list_min)
    print(Globals.list_max)

def winningChance():
    list_tahun = list(map(int, input().split(" ")))

    for tahun in list_tahun:
        if tahun > 1990 and tahun < 2020:
            if tahun % 2 == 1:
                Globals.winning_count += 1

    print(Globals.winning_count)
