from multiprocessing import Pool
import time, random
import argparse

def mergeWrap(tupl):
    # tupl = (arr1, arr2)
    arr1, arr2 = tupl
    return merge(arr1,arr2)

def merge(left, right):
    i = 0
    j = 0
    res = []

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    
    while(i<len(left)):
        res.append(left[i])
        i+=1
    
    while(j<len(right)):
        res.append(right[j])
        j+=1

    return res

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))

def linspace(a,b,nsteps):
    # Chia khoang [a,b] thanh nsteps diem, nsteps-1 khoang
    ssize = float(b-a)/(nsteps-1)
    return [a + i*ssize for i in range(nsteps)]

def mergeSortParallel(arr, numproc):

    # Mang chua cac diem chia
    endpoints = [int(x) for x in linspace(0, len(arr), numproc+1)]

    # Chia mang
    args = [arr[endpoints[i]:endpoints[i+1]] for i in range(numproc)]

	# Tao Pool
    pool = Pool(processes = numproc)
    sortedsublists = pool.map(mergeSort, args)

	# Sap xep tung mang con
    while len(sortedsublists) > 1:
        # Lay cap mang con de tron
        args = [(sortedsublists[i], sortedsublists[i+1]) for i in range(0, len(sortedsublists), 2)]
        sortedsublists = pool.map(mergeWrap, args)

    return sortedsublists[0]

def writeToFile(strTime, filename):
    with open(filename, 'a') as f:
        f.write(strTime)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--size", type=int, default=1000000, \
                        help="Number of elements in array")
    parser.add_argument("-f", "--output", type=str, default="results.txt", \
                        help="File to write results to")
    parser.add_argument("-p", "--processes", type=int, default=4, \
                        help="Number of processes to use")
    args = parser.parse_args()
    return args

def main():
    args = parseArgs()

    N = args.size
    fname = args.output
    nproc = args.processes

    strTime = "Array size: " + str(N) + "\n"
    strTime += "Number of processes: " + str(nproc) + "\n"
    
    arr = [random.randint(0,100) for i in range(N)]
    start = time.time()
    arr = mergeSort(arr)
    end = time.time()
    print("Time taken for serial merge sort: ", end-start)
    strTime += "Time taken for serial merge sort: " + str(end-start) + "\n"

    time.sleep(1)

    start = time.time()
    arr = mergeSortParallel(arr, nproc)
    end = time.time()
    print("Time taken for parallel merge sort: ", end-start)
    strTime += "Time taken for parallel merge sort: " + str(end-start) + "\n\n"

    writeToFile(strTime, fname)

if __name__ == '__main__':
    main()