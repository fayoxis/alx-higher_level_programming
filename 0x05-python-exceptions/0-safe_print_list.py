#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_count = 0
    try:
        while my_list[element_count] and element_count < x:
            print(my_list[element_count], end="")
            element_count += 1
    except (IndexError, TypeError):
        pass
    finally:
        print()
        return element_count
