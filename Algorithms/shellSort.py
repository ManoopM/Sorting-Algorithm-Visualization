import time
from colors import *


def shell_sort(data, drawData, timeTick):
    size = len(data)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = data[i]
            j = i
            while j >= gap and data[j-gap] > anchor:
                data[j] = data[j - gap]
                j -= gap
            data[j] = anchor

            drawData(data, [LIGHT_GREEN if x == gap else YELLOW if x == i else PURPLE if x == j else BLUE for x in range(len(data))])
        gap = gap//2

        # drawData(data, [YELLOW if x == j else PURPLE if x == j else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

