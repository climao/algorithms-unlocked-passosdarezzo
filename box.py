# -*- coding: utf-8 -*-

class Box:
    '''
    Creates a box around the text.

    >>> my_box = Box()
    >>> my_box.add_text_line('Prefiro morrer do que perder a vida!')
    >>> my_box.print_box()
    '''

    # Class Variables
    heavy_box_chars = {'top_left_corner' : u'\u250f',
                       'top_right_corner' : u'\u2513',
                       'bottom_left_corner' : u'\u2517',
                       'bottom_right_corner' : u'\u251b',
                       'horizontal_line' : u'\u2501',
                       'vertical_line' : u'\u2503',
                       'space' : ' '}

    light_box_chars = {'top_left_corner' : u'\u250c',
                       'top_right_corner' : u'\u2510',
                       'bottom_left_corner' : u'\u2514',
                       'bottom_right_corner' : u'\u2502',
                       'horizontal_line' : u'\u2500',
                       'vertical_line' : u'\u2502',
                       'space' : ' '}

    simple_box_chars = {'top_left_corner' : u'\u2552',
                        'top_right_corner' : u'\u2555',
                        'bottom_left_corner' : u'\u2558',
                        'bottom_right_corner' : u'\u255b',
                        'horizontal_line' : u'\u2550',
                        'vertical_line' : u'\u2502',
                        'space' : ' '}

    def __init__(self, max_width=40):
      # Instance Variables
      self.lines = []
      self.max_width = max_width
      self.bigger_line = 0

    def add_text_line(self, text):
      '''
      Adds a text line to the text showed inside the box.

      >>> my_box.add_text_line('Prefiro morrer do que perder a vida!')
      '''
      if self.bigger_line < len(text):
        self.bigger_line = len(text)

      self.lines.append(text)

    def print_box(self):
        '''
        Prints the text with box.

        >>> my_box.print_box()
        '''
        max_line = self.max_width - 2
        off_set = 0
        ne = self.simple_box_chars

        print ne['top_left_corner'] + max_line * ne['horizontal_line'] + ne['top_right_corner']

        for i in self.lines:
            print ne['vertical_line'] + i + (max_line - len(i)) * ne['space'] + ne['vertical_line']

        print ne['bottom_left_corner'] + max_line * ne['horizontal_line']  + ne['bottom_right_corner']
