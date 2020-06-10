def groupingDishes(dishes):
    cache = {}
    result = []
    count = 0
    for item in dishes:
        for i in range(1, len(item)):
            if item[i] in cache:
                cache[item[i]].append(item[0])
            else:
                cache[item[i]] = [item[0]]
    for key in sorted(cache):
        if len(cache[key]) == 1:
            del cache[key]
            continue
        result.append([])
        result[count].append(key)
        for item in sorted(cache[key]):
            result[count].append(item)
        count += 1
    return result