#!/usr/bin/python3
""" MyList Class inherits from list """


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Prints the list but sorted """
        n_list = self[:]
        n_list.sort()
        print(n_list)
