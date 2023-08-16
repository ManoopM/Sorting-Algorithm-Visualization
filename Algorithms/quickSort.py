import time
from colors import *


def partition(data, start, end):
    pivot_index = start
    pivot = data[pivot_index]

    start = pivot_index + 1
    end = len(data) - 1

    while start < end:
        while start < len(data) and data[start] <= pivot :
            start += 1

        while data[end] > pivot:
            end -= 1

        if start < end:
            data[start], data[end] = data[end], data[start]

    data[pivot_index], data[end] = data[end], data[pivot_index]

    return end


def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pi = partition(data, start, end)
        quick_sort(data, start, pi-1, drawData, timeTick)
        quick_sort(data, pi+1, end, drawData, timeTick)

        drawData(data, [YELLOW if x == start else PURPLE if x == end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])