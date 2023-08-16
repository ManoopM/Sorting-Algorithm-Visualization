import time
from colors import *


def partition(data, start, end):
    i = (start - 1)
    x = data[end]

    for j in range(start, end):
        if data[j] <= x:
            # increment index of smaller element
            i = i + 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[end] = data[end], data[i + 1]

    return ((i + 1))


def quick_sort(data, start, end, drawData, timeTick):
    # Create an auxiliary stack
    size = end - start + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(data, start, end)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > start:
            top = top + 1
            stack[top] = start
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < end:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end

        drawData(data, [BLUE for x in range(len(data))])