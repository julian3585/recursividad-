def Subsecuencia(arr):

    if not arr:
        return []

    LIS = [[] for _ in range(len(arr))]
    LIS[0].append(arr[0])

    for i in range(1, len(arr)):
        for S in range(i):



            if arr[S] < arr[i] and len(LIS[S]) > len(LIS[i]):
                LIS[i] = LIS[S].copy()

        LIS[i].append(arr[i])

    S = 0
    for i in range(len(arr)):
        if len(LIS[S]) < len(LIS[i]):
            S = i

    print(LIS[S])


if __name__ == '__main__':
    arr = [19, 33, 44, 55, 56, 88, 54, 12, 34]
    Subsecuencia(arr)