def cyclic_shift(numbers: list[int | float], step: int) -> None:
    new_lst = [0 for i in range(len(numbers))]
    for i in range(len(numbers)):
        new_lst[i+step] = numbers[i]
    print(new_lst)
    return None

nums = [1, 2, 3, 4, 5]
cyclic_shift(nums, -2)

