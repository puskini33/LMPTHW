from Stacks_DS import Stack
import unittest

"""
Author: Elena Hirjoaba
Date: 26.09.2019
"""


class TestCase(unittest.TestCase):

    def test_push(self):
        colors = Stack()
        colors.push('Pthalo Blue')
        assert colors.count() == 1
        colors.push('Ultramarine Bleu')
        assert colors.count() == 2
        colors.push('Magenta')
        assert colors.count() == 3
        colors.push('Green')
        assert colors.count() == 4
        colors.push('Red')
        assert colors.count() == 5

    def test_pop(self):
        colors = Stack()
        colors.push('Magenta')
        colors.push('Alizarin')
        colors.push('Blue')
        assert colors.pop() == 'Blue'
        assert colors.pop() == 'Alizarin'
        assert colors.pop() == 'Magenta'
        assert colors.pop() is None

    def test_top(self):
        colors = Stack()
        colors.push('Blue')
        assert colors.top_node() == 'Blue'
        colors.pop()
        assert colors.top_node() is None

    def test_dump(self):
        colors = Stack()
        colors.push('Magenta')
        colors.push('Alizarin')
        colors.dump('before Blue')
        colors.push('Blue')
        colors.dump('after Blue')


if __name__ == '__main__':
    unittest.main(verbosity=2)
