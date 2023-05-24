def create_an_empty_list():
    return []

#contains a function "create_a_list()" that creates and returns a list of length 4.
def create_a_list():
    return [1, 2, 3, 4]

#contains a function "add_element_to_end_of_list" that adds an element to the end of a list. 
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

#contains a function "add_element_to_start_of_list" that adds an element to the start of a list.
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

#contains a function "remove_element_from_end_of_list()" that removes an element from the end of a list.
def remove_element_from_end_of_list(l):
    l.pop()
    return l

#contains a function "remove_element_from_start_of_list()" that removes an element from the start of a list.
def remove_element_from_start_of_list(l):
    del (l[0])
    return l

#contains a function "retrieve_first_element_from_list()" that retrieves the first element from a list.
def retrieve_first_element_from_list(l):
    return l[0]

#contains a function "retrieve_element_from_index()" that takes a list and an index as arguments and returns the list's element at that index. 
def retrieve_element_from_index(l, index):
    return l[index]

#contains a function "retrieve_last_element_from_list()" that retrieves the last element from a list
def retrieve_last_element_from_list(l):
    return l[-1]
