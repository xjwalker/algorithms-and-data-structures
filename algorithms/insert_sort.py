"""
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an 
unsorted list into its correct position in a sorted portion of the list. 
It is like sorting playing cards in your hands. You split the cards into two groups: 
the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group 
and put it in the right place in the sorted group.

We start with the second element of the array as the first element is assumed to be sorted.
Compare the second element with the first element if the second element is smaller then swap them.
Move to the third element, compare it with the first two elements, and put it in its correct position
Repeat until the entire array is sorted
"""
def insert_sort(left: list, right: int, index):
    if len(left) > 1:
        response =  insert_sort(left[:index - 1], left[index - 1], index - 1)
        if response[0] > right:
            return [right] + response
        for i, num in enumerate(response):
            if num >= right:
                return response[:i] + [right] + response[i:]
    else:
        if left[0] > right:
            return [right] + left
        for i, num in left: 
            if num <= right: 
                return left[:i] + [right] + left[i:]

def insert_sort_2(elements):
    for i in range(len(elements) - 1):
        for j in range(i, 0, -1):
            if elements[j] < elements[j-1]:
                elements[j-1], elements[j] = elements[j], elements[j-1]

    return elements

def regular_insert_sort(elements):
    for index in range(1, len(elements)):
        key = elements[index]
        j = index - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j-=1
        elements[j + 1] = key
    return elements


def main():
    elements = [90,32,1,2,4,54,3,24]
    size = len(elements) - 1
    # sorted_elements = insert_sort(elements[:size], elements[size], size)
    sorted_elements = regular_insert_sort(elements)
    print("sorted", sorted_elements)
    # resutl = insert_sort_2(elements)
    # print("r", resutl)


if __name__ == "__main__":
    main()