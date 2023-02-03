# Program to perform selection sort

# Function to scan the list
def scan_list(list_1, size):
    print(f"Enter the {size} elements of the array:")
    for i in range(size):
        element = int(input(f"Element [{i}]: "))
        list_1.append(element)


# Function to print the list
def print_list(list_1):
    print(list_1)


# Function to perform selection sort
def selection_sort(list_1, size):
    for i in range(size-1):
        min = i
        for j in range(i+1, size):
            if list_1[j] < list_1[min]:
                min = j
        if min != i:
            (list_1[i], list_1[min]) = (list_1[min], list_1[i])


# Driver Function
if __name__ == '__main__':
    list_1 = []
    size = int(input("Enter the number of elements of the list: "))
    scan_list(list_1, size)
    print_list(f"List: {list_1}")
    selection_sort(list_1, size)
    print_list(f"Sorted List: {list_1}")

