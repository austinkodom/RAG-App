import unittest
from src.retrieval import search_arxiv  # Replace with the correct import path

class TestSearchArxiv(unittest.TestCase):

    def test_valid_search(self):
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
            print()

    def test_bogus_search(self):
        # A query to likely return no results.
        query = "zzzzzzzz" 
        max_results = 5

        abstracts = search_arxiv(query, max_results)

        # Check that the results are returned as a list.
        self.assertIsInstance(abstracts, list)

        # Check that the results are empty or contain no summary available.
        for abstract in abstracts:
            self.assertTrue(
                abstract == "No summary available" or abstract.strip() == ""
            )

        # Print the abstracts for viewing
        for abstract in abstracts:
            print(abstract)
            print()

if __name__ == '__main__':
    unittest.main()
