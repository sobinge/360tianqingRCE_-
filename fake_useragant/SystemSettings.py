import time
from multiprocessing import Pool

def run(msg):
    print(msg)
    time.sleep(30)
    print('end')

if __name__ == "__main__":
    print('start111')
    pool=Pool(1)
    pool.apply_async(run,(1,))
    pool.close()
    pool.join()