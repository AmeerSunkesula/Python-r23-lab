## ======List Operations function======
def perform_operations(lst):
# i. Addition: Append an element to the end of the list
    def addition(lst, element):
        lst.append(element)
        print(f"List after addition: {lst}")
# ii. Insertion: Insert an element at a specific index
    def insertion(lst, index, element):
        if index < 0 or index > len(lst):
            print("Index out of bounds.")
        else:
            lst.insert(index, element)
        print(f"List after insertion: {lst}")
# iii. Slicing: Get a sublist from start_index to end_index (exclusive)
    def slicing(lst, start_index, end_index):
        if start_index < 0 or end_index > len(lst) or start_index > end_index:
            print("Invalid slice indices.")
        else:
            sliced_lst = lst[start_index:end_index]
        print(f"Sliced list from index {start_index} to {end_index}: {sliced_lst}")
# Test the operations
    print("Initial list:", lst)
# Perform addition
    addition(lst, 10)
# Perform insertion
    insertion(lst, 2, 8)
# Perform slicing
    slicing(lst, 1, 4)
# ======end of the function perform_operations======    
# Example usage
my_list = [1, 2, 3, 4, 5]
perform_operations(my_list)