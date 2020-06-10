def areFollowingPatterns(strings, patterns):
    cache = {}
    cache2 = {}
    for i in range(len(strings)):
        if strings[i] in cache:
            if cache[strings[i]] != patterns[i]:
                return False
        else:
            cache[strings[i]] = patterns[i]
    for i in range(len(patterns)):
        if patterns[i] in cache2:
            if cache2[patterns[i]] != strings[i]:
                return False
        else:
            cache2[patterns[i]] = strings[i]
    return True