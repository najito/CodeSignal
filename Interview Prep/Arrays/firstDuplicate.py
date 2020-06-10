function firstDuplicate(a) {
    const cache = {}
    for (let i = 0; i < a.length; i ++) {
        if (cache[a[i]] === undefined) {
            cache[a[i]] = i
        } else {
            return a[i]
        }
    }
    return -1
}
