import idilioatomico    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_grammar(self): # Is the grammar being loaded?
        self.assertIsNotNone(idilioatomico.load_dict('grammar.json'))

    def test_substitutions(self): # Are substitutions being loaded?
        self.assertIsNotNone(idilioatomico.load_dict('substitutions.json'))

    def test_check_for_symbols(self): # Does the function correctly identify symbols?
        self.assertTrue(idilioatomico.check_for_symbols('FV FN'))
        self.assertFalse(idilioatomico.check_for_symbols('no symbols here'))

    def test_clean(self):
        self.assertEqual(idilioatomico.clean('you see , a eagle flies'), 'You see, an eagle flies.')

if __name__ == '__main__':
    unittest.main()
