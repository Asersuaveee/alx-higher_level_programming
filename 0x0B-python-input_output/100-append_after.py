#!/usr/bin/python3
""" 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """add after
    """
    string = ""
    with open(filename, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            string += line
            if search_string in line:
                string += new_string
            if not line:
                break
    with open(filename, "w", encoding="utf-8") as file:
        file.write(string)
