import unittest
import main


class RegexEngineTestCase(unittest.TestCase):
    def test_compare_strings_true(self):
        self.assertTrue(main.compare_strings('apple', 'apple'))
        self.assertTrue(main.compare_strings('^app', 'apple'))
        self.assertTrue(main.compare_strings('le$', 'apple'))
        self.assertTrue(main.compare_strings('^a', 'apple'))
        self.assertTrue(main.compare_strings('.$', 'apple'))
        self.assertTrue(main.compare_strings('apple$', 'apple'))
        self.assertTrue(main.compare_strings('^apple', 'apple'))
        self.assertTrue(main.compare_strings('^apple$', 'apple'))

    def test_compare_strings_false(self):
        self.assertFalse(main.compare_strings('^apple$', 'apple pie'))
        self.assertFalse(main.compare_strings('^apple$', 'tasty apple'))
        self.assertFalse(main.compare_strings('^le', 'apple'))
        self.assertFalse(main.compare_strings('app$', 'apple'))

    def test_compare_with_question_marks(self):
        self.assertTrue(main.compare_strings('colou?r', 'color'))
        self.assertTrue(main.compare_strings('colou?r', 'colour'))
        self.assertFalse(main.compare_strings('colou?r', 'colouur'))

    def test_compare_with_asterisks(self):
        self.assertTrue(main.compare_strings('colou*r', 'color'))
        self.assertTrue(main.compare_strings('colou*r', 'colour'))
        self.assertFalse(main.compare_strings('col.*r$', 'colors'))
        self.assertTrue(main.compare_strings('colou*r', 'colouur'))
        self.assertTrue(main.compare_strings('col.*r', 'color'))
        self.assertTrue(main.compare_strings('col.*r', 'colour'))
        self.assertTrue(main.compare_strings('col.*r', 'colr'))
        self.assertTrue(main.compare_strings('col.*r', 'collar'))

    def test_with_escape(self):
        self.assertTrue(main.compare_strings('\.$', 'end.'))
        self.assertTrue(main.compare_strings('3\+3', '3+3=6'))
        self.assertTrue(main.compare_strings('\?', 'Is this working?'))
        self.assertTrue(main.compare_strings('\\', '\\'))
        self.assertFalse(main.compare_strings('colou\?r', 'color'))
        self.assertFalse(main.compare_strings('colou\?r', 'colour'))


if __name__ == '__main__':
    unittest.main()
