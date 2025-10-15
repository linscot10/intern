def second_largest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two distinct elements.")

    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        raise ValueError("List must contain at least two distinct values.")

    unique_nums.sort(reverse=True)
    return unique_nums[1]
