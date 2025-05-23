"""
Bubble sort is the simplest sorting algorithm.
It's easy to understand the way it goes through each element in the array
and then compares it to all until a lower item is found, and then it gets swapped
to continue searching for the next element.
This until all elements are passed over and every element it's in the right correct place.

Time & space complexity: O(n^2)
"""

def bubble_sort(elements: list) -> list:
    for i in range(len(elements) - 1):
        for j in range(len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements

def main():
    unsorted_elements = [90, 32, 1, 2, 4, 543, 3, 24, 43, 0]
    sorted_elements = bubble_sort(unsorted_elements)
    print(sorted_elements)
    assert sorted_elements == [0, 1, 2, 3, 4, 24, 32, 43, 90, 543]

if __name__ == '__main__':
    main()
