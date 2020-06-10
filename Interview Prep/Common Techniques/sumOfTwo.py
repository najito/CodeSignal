def sumOfTwo(a, b, v):
    cache = {}
    for item in a:
        cache[v - item] = True;
    for item in b:
        if item in cache:
            return True;
    return False