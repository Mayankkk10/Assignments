def max_subarray_with_constraint(resources, constraint):
    def helper(left, right):
        if left > right:
            return (0, -1, -1)  # sum, start, end

        if left == right:
            return (resources[left], left, right) if resources[left] <= constraint else (0, -1, -1)

        mid = (left + right) // 2
        left_sum, left_start, left_end = helper(left, mid)
        right_sum, right_start, right_end = helper(mid + 1, right)

        max_cross_sum = 0
        cross_start = cross_end = -1
        temp_sum = 0

        l = mid
        left_part = []
        while l >= left:
            temp_sum += resources[l]
            left_part.append((temp_sum, l))
            l -= 1

        r = mid + 1
        temp_sum = 0
        right_part = []
        while r <= right:
            temp_sum += resources[r]
            right_part.append((temp_sum, r))
            r += 1

        for l_sum, l_idx in left_part:
            for r_sum, r_idx in right_part:
                total = l_sum + r_sum
                if total <= constraint and total > max_cross_sum:
                    max_cross_sum = total
                    cross_start = l_idx
                    cross_end = r_idx

        candidates = [
            (left_sum, left_start, left_end),
            (right_sum, right_start, right_end),
            (max_cross_sum, cross_start, cross_end)
        ]
        return max(candidates, key=lambda x: x[0])

    total_sum, start, end = helper(0, len(resources) - 1)
    return resources[start:end + 1] if start != -1 else []

test_cases = [
    ([2, 1, 3, 4], 5),
    ([2, 2, 2, 2], 4),
    ([1, 5, 2, 3], 5),
    ([6, 7, 8], 5),
    ([1, 2, 3, 2, 1], 5),
    ([1, 1, 1, 1, 1], 4),
    ([4, 2, 3, 1], 5),
    ([], 10),
    ([1, 2, 3], 0),
    (list(range(1, 100001)), 10**9)
]

for i, (resources, constraint) in enumerate(test_cases, 1):
    result = max_subarray_with_constraint(resources, constraint)
    print(f"Test {i}: {result} → sum = {sum(result)}")