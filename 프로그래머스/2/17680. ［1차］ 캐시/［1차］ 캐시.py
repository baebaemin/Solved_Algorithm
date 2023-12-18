from collections import deque

def solution(cacheSize, cities):
    DB = deque()
    time = 0
    
    for temp_city in cities:
        city = temp_city.lower()
        if city not in DB:
            DB.appendleft(city)
            time += 5
        else: # DB 안에 city가 있다면
            DB.remove(city)
            DB.appendleft(city)
            time += 1
        if len(DB) > cacheSize:
            DB.pop()
    return time