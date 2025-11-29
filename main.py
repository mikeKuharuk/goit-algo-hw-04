import random
import timeit


def get_sample_data():
    return random.sample(range(0,1000),100)


def method_timsort():
    random_ints = get_sample_data()
    sorted_random_ints = sorted(random_ints)

def method_insertion():
    random_ints = get_sample_data()

    for i in range(1, len(random_ints)):
        key = random_ints[i]
        j = i-1
        while j >=0 and key < random_ints[j] :
                random_ints[j+1] = random_ints[j]
                j -= 1
        random_ints[j+1] = key
    return random_ints

def method_merge():
    random_ints = get_sample_data()
    merge_sort(random_ints)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def main():
    print("Starting calculation")
    time_method_sorted = timeit.timeit(method_timsort)
    time_method_insertion = timeit.timeit(method_insertion)
    time_method_merge = timeit.timeit(method_merge)

    print(f"\nTimsort method Time: {time_method_sorted}"
          f"\nInsertion method Time: {time_method_insertion}"
          f"\nMerge method Time: {time_method_merge}")


if __name__ == '__main__':
    main()
