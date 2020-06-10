def containsCloseNums(nums, k):
    cache = {}
    for i in range(len(nums)):
        if nums[i] in cache:
            if abs(cache[nums[i]] - i) <= k:
                return True
            cache[nums[i]] = i
        else:
            cache[nums[i]] = i
    return False