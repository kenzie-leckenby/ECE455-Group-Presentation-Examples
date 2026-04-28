import threading
import time
import math
import sys

def cpu_heavy(n):
    """CPU-bound task: sum of square roots"""
    return sum(math.sqrt(i) for i in range(n))

def run_sequential(tasks):
    start = time.perf_counter()
    results = [cpu_heavy(n) for n in tasks]
    return time.perf_counter() - start

def run_threaded(tasks):
    threads = []
    results = [None] * len(tasks)

    def worker(idx, n):
        results[idx] = cpu_heavy(n)

    start = time.perf_counter()
    for i, n in enumerate(tasks):
        t = threading.Thread(target=worker, args=(i, n))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start

if __name__ == "__main__":
    gil_enabled = sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else True
    cores = 4
    tasks = [2_000_000] * cores

    print(f"Python version:  {sys.version}")
    print(f"GIL enabled:     {gil_enabled}")
    print(f"Tasks:           {len(tasks)} threads × 2,000,000 iterations\n")

    print("Running sequential...")
    seq_time = run_sequential(tasks)
    print(f"  Sequential: {seq_time:.2f}s")

    print("Running threaded...")
    thread_time = run_threaded(tasks)
    print(f"  Threaded:   {thread_time:.2f}s")

    speedup = seq_time / thread_time
    print(f"\nSpeedup: {speedup:.2f}x")