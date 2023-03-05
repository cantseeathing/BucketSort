import math


def insertion_sort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


def bucket_sort(customList):
    number_of_buckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(number_of_buckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil((j * number_of_buckets) / maxValue)
        arr[index_b - 1].append(j)
    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


ex = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(bucket_sort(customList=ex))
