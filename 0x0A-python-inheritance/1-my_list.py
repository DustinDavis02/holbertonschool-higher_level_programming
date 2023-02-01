#!/usr/bin/python3
"""This contains class MyList"""


class MyList(list):
    """custom class called list, inherited from built-in list class."""

    def print_sorted(self):
        """Prints sorted format"""

        new_list = self.copy()
        sorted_list = sorted(new_list)
        print(sorted_list)
        return sorted_list