import unittest
def caesar(message, shift):
    result = []
    for char in message:
        if char.isalpha():
            shift_l = ord('a') if char.islower() else ord('A')
            shift_char = chr((ord(char) - shift_l + shift) % 26 + shift_l)
            result.append(shift_char)
        else:
            result.append(char)
    return ''.join(result)
#message = input()
#shift = int(input())
#print (caesar(message,shift))
class TestCaesar(unittest.TestCase):

    def test_1(self):
        self.assertEqual(caesar("abc", 1), "bcd")
        self.assertEqual(caesar("xyz", 2), "zab")
        self.assertEqual(caesar("Hello, World!", 3), "Khoor, Zruog!")
    
    def test_negative_value(self):
        self.assertEqual(caesar("abc", -1), "zab")
        self.assertEqual(caesar("Hello, World!", -3), "Ebiil, Tloia!")

    def test_no_shift(self):
        self.assertEqual(caesar("abc", 0), "abc")
        self.assertEqual(caesar("Hello, World!", 0), "Hello, World!")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar("1234!@#$", 5), "1234!@#$")
        self.assertEqual(caesar("Hello, World! 123", 2), "Jgnnq, Yqtnf! 123")

    def test_full_circle(self):
        self.assertEqual(caesar("abc", 26), "abc")
        self.assertEqual(caesar("abc", 52), "abc")

if __name__ == '__main__':
    unittest.main()