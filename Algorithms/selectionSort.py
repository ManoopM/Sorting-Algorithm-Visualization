import time
from colors import *


def selection_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size):
            if data[j] < data[min_index]:
                min_index = j

            drawData(data, [YELLOW if x == i else PURPLE if x == j else BLUE for x in
                            range(len(data))])

        if i != min_index:
            drawData(data, [GREEN if x == min_index else BLUE for x in
                            range(len(data))])
            data[i], data[min_index] = data[min_index], data[i]
            time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])