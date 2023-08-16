import time
from colors import *


def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        anchor = data[i]
        j = i - 1
        while j >= 0 and anchor < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = anchor

        drawData(data, [YELLOW if x == i else PURPLE if x == j else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])