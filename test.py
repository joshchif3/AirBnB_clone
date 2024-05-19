#!/usr/bin/python3
"""
This module contains a simple example class.
"""


class Person:
    """
    A simple class representing a person.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
    """

    def __init__(self, first_name, last_name):
        """
        Initializes a new instance of Person.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
        """
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """
        Returns the full name of the person.

        Returns:
            str: The full name of the person.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Returns a string representation of the person.

        Returns:
            str: A string representation of the person.
        """
        return (
            f"Person(first_name='{self.first_name}', "
            f"last_name='{self.last_name}')"
        )


if __name__ == "__main__":
    # Example usage
    person = Person("John", "Doe")
    print(person)
    print(person.full_name())
