def rotateImage(a):
    a[:] = [list(x) for x in zip(*a[::-1])]
    return a