try:
    num_list = input("Пожалуйста, введите последовательность чисел через пробел.\n")
    lead_num = int(input("Пожалуйста, введите желаемое целое число.\n"))

    numbers = list(map(int, str.split(num_list)))
    numbers_sorted = sorted(numbers)                  # если будет время сюда вставить велосипед

except ValueError:
    print("Введённые данные не удовлетворяют условиям.")


def binary_search(nums, lead, left, right):
    if left > right:
        return False
    mid = (right + left) // 2
    if nums[mid] == lead:
        return mid
    elif lead < nums[mid]:
        return binary_search(nums, lead, left, mid - 1)
    else:
        return binary_search(nums, lead, mid + 1, right)


print("Отсортированный список: ", numbers_sorted)
print("Индекс введенного числа в списке: ", binary_search(numbers_sorted, lead_num, 0, len(numbers_sorted) - 1))