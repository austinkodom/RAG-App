import unittest
from src.augmentation import combine_context

class TestCombineContext(unittest.TestCase):
    def test_with_valid_abstracts(self):
        query = "This is a test query."
        abstracts = [
            "This is a returned test abstract.",
            "This is also a returned test abstract.",
            "This is yet again another returned test abstract",
        ]

        result = combine_context(query, abstracts)
        self.assertIn("Question: This is a test query.", result)
        self.assertIn("Context: This is a returned test abstract.", result)

        # Print the result for viewing.
        print(f"{result}\n\n")
        print()

    def test_with_empty_abstracts(self):
        query = "Some bogus query."
        abstracts = []
        result = combine_context(query, abstracts)
        self.assertEqual(result, "Question: Some bogus query.\nContext: No relevant information was found.")

        # Print the result for viewing.
        print(f"{result}\n\n")

if __name__ == "__main__":
    unittest.main()
