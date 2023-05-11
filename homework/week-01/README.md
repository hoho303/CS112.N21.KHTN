# Thuật toán sắp xếp trộn (Merge Sort) kết hợp xử lý song song (Parallel Merge Sort)

## Mô tả
![alt](https://github.com/hoho303/CS112.N21.KHTN/blob/Parallel-Algorithm/merge_sort_parallel.PNG)

## Thống kê
![alt](https://github.com/hoho303/CS112.N21.KHTN/blob/Parallel-Algorithm/time_consume.PNG)

## Cách chạy
```
python MergeSort.py --size <array_size> --output <file_name> -p <number_of_process>
```
*number_of_process = 2^n*

Ví dụ: 
```
python MergeSort.py --size 1000000 --output output.txt -p 4
```

