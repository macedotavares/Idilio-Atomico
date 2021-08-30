import idilioatomico    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_grammar(self):
        self.assertIsNotNone(idilioatomico.load_dict('grammar.json'))

    def test_substitutions(self):
        self.assertIsNotNone(idilioatomico.load_dict('substitutions.json'))

if __name__ == '__main__':
    unittest.main()
