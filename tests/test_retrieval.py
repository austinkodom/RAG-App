import unittest
from src.retrieval import search_arxiv  # Replace with the correct import path

class TestSearchArxiv(unittest.TestCase):

    def test_search_arxiv(self):
        query = "machine learning"
        max_results = 3

        # Run the search function
        abstracts = search_arxiv(query, max_results)

        # Check if the results are returned as a list
        self.assertIsInstance(abstracts, list)

        # Ensure we have the expected number of results
        self.assertLessEqual(len(abstracts), max_results)

        # Check that each result is a non-empty string
        for abstract in abstracts:
            self.assertIsInstance(abstract, str)
            self.assertGreater(len(abstract), 0)

        # Print the abstracts for viewing
        for abstract in abstracts:
            print(abstract)

if __name__ == '__main__':
    unittest.main()
