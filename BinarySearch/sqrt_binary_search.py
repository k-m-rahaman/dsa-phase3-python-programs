def sqrt_binary_search(x):
    left, right = 0, x
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            ans = mid
            left = mid + 1

        else:
            right = mid - 1

    return ans


print(sqrt_binary_search(17))