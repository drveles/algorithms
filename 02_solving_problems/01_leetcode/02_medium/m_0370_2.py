'''
370. Range Addition
Предположим, что у вас есть массив длиной n, инициализированный всеми нулями, и вам задано k операций обновления.

Каждая операция представлена в виде триплета: [startIndex, endIndex, inc], который увеличивает каждый элемент подмассива A[startIndex ... endIndex] (startIndex и endIndex включительно) с увеличением.

Возвращает измененный массив после выполнения всех k операций.
'''
from itertools import accumulate 

def main(len, ranges):
    result = [0] * len
    prefix = [0]
    
    for start, end, step in ranges:
        result[start] += step
        if  end + 1 < len:
            result[end + 1] -= step

    print(list(accumulate(result)))

if __name__ == "__main__":
    main(5, [[1,3,2],[2,4,3],[0,2,-2]]) # [-2,0,3,5,3]