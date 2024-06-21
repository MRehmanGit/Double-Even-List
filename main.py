def double_even_numbers(lst):
    # Created an empty list to store the results
    final_list = []

    # Iterating over each element in the input list
    for everyElement in lst:
        # Checking if the element is even
        if everyElement % 2 == 0:
            # Doubles the even element and add it to the final list
            final_list.append(everyElement * 2)
        else:
            # If the element is odd, add it to the final list as is
            final_list.append(everyElement)

    # Returning the resulting list
    return final_list

# Testing a list of integers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the new list where all the even numbers are doubled
print("New list where all the even numbers are doubled: ", double_even_numbers(my_list))
