import sys
from typing import List, Set, Deque, Dict
from collections import deque

#takes a number of requests in caches with capacity k.
def fifo(k: int, requests: List[int]) -> int:
    cache: Set[int] = set() #cache will be a set
    q: Deque[int] = deque()    #to keep track of whats in cache use a doubleended queue
    num_misses = 0

    for req in requests:
        if req in cache:
            continue
        else:
            num_misses+=1
        if(len(cache) < k):
            cache.add(req);
            q.append(req);
        else:
            old_ele = q.popleft();
            cache.remove(old_ele);
            cache.add(req);
            q.append(req);

    return num_misses


def lru(k:int, requests: List[int]) -> int:
    cache: Set[int] = set();
    last_time : Dict[int, int] = {} #makes a dictionary where the key is the ID and the value is the access

    num_misses = 0;

    for time, req in enumerate(requests):
        if req in cache:
            last_time[req] = time;
            continue
        else:
            num_misses+=1;
        if(len(cache) < k):
            cache.add(req);
            last_time[req] = time;
        else:
            least = min(cache, key=lambda x: last_time[x]) #picks the least recently used.
            cache.remove(least)
            last_time.pop(least, None)
            cache.add(req)
            last_time[req] = time

    return num_misses;

def main():
    if(len(sys.argv)) != 2:
        print("Needs to have following format: main.py <input_file>")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        line_one = file.readline().split()
        k = int(line_one[0])
        m = int(line_one[1])
        requests = list(map(int,file.readline().split()))

    num_fifo_miss = fifo(k, requests)
    num_lru_miss = lru(k, requests)

    print("FIFO :", num_fifo_miss)
    print("LRU :", num_lru_miss)

if __name__ == "__main__":
    main()



