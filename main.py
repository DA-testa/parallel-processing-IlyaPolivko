# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    for job in range(m):
        min_time = min(threads)
        thread_idx = threads.index(min_time)
        output.append((thread_idx, min_time))
        threads[thread_idx] += data[job]
    return output

def main():
    
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for thread_idx, start_time in result:
        print(thread_idx, start_time)



if __name__ == "__main__":
    main()
