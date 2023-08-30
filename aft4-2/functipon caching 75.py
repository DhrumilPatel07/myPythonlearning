import time
from functools import lru_cache

n = int(input("enter how much lru cache you want:"))
@lru_cache(maxsize=n)

def somework(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now running some work")
    somework(3)
    somework(1)
    somework(6)
    somework(9)
    print("done...calling again")
    # input("enter what you want")
    somework(3)
    print("called again")