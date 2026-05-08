def first_occurrence(arr, x):
    left, right = 0, len(arr)-1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            result = mid
            right = mid - 1

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return result


def last_occurrence(arr, x):
    left, right = 0, len(arr)-1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            result = mid
            left = mid + 1

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return result


arr = [1,2,2,2,3,4]
print(first_occurrence(arr, 2))
print(last_occurrence(arr, 2))