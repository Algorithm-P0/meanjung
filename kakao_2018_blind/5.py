from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0
    if cacheSize == 0:
        time = 5*len(cities)
    else:
        for c in cities:
            c = c.lower()
            if c in cache:
                cache.remove(c)
                cache.append(c)
                time += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(c)
                    time += 5
                else:
                    cache.popleft()
                    cache.append(c)
                    time += 5
    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))