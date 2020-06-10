def containsDuplicates(a):
    cache = {}
    for item in a:
        if item in cache:
            return True;
        else:
            cache[item] = True
    return False