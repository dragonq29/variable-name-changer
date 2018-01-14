# -*- coding: utf-8 -*-


class StringChanger:

    strings_array = []
    def __init__(self, input_strings_array):
        self.__change_to_variable_strings(input_strings_array)

    def __change_to_variable_strings(input_string_array):

        for input_string in input_string_array:
            input_string = input_string.split("[^A-Za-z0-9]+")


