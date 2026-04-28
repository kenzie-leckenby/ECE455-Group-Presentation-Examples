import threading
import time
import urllib.request
import sys

# List of URLs to fetch (IO-bound work)
URLS = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com",
    "https://www.numpy.org",
    "https://www.scipy.org",
    "https://www.pandas.pydata.org",
] * 2  # 16 total requests

def fetch_url(url, results, idx):
    try:
        start = time.perf_counter()
        with urllib.request.urlopen(url, timeout=10) as response:
            size = len(response.read())
        elapsed = time.perf_counter() - start
        results[idx] = (url, size, elapsed)
    except Exception as e:
        results[idx] = (url, 0, 0)

def run_sequential(urls):
    results = [None] * len(urls)
    start = time.perf_counter()
    for i, url in enumerate(urls):
        fetch_url(url, results, i)
    total = time.perf_counter() - start
    return total, results

def run_threaded(urls):
    results = [None] * len(urls)
    threads = []
    start = time.perf_counter()
    for i, url in enumerate(urls):
        t = threading.Thread(target=fetch_url, args=(url, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    total = time.perf_counter() - start
    return total, results

if __name__ == "__main__":
    gil_status = sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else True
    print(f"GIL enabled: {gil_status}")
    print(f"Fetching {len(URLS)} URLs\n")

    print("Running sequential...")
    seq_time, seq_results = run_sequential(URLS)
    print(f"  Sequential: {seq_time:.2f}s")

    print("Running threaded...")
    thread_time, thread_results = run_threaded(URLS)
    print(f"  Threaded:   {thread_time:.2f}s")

    speedup = seq_time / thread_time
    print(f"\nSpeedup: {speedup:.2f}x faster with threads")