import requests
import xml.etree.ElementTree as ET

def search_arxiv(query, max_results=5):
    """
    Search arXiv.org for research abstracts matching the query.

    Arguments:
        query (str): The search term to query arXiv.
        max_results (int): The maximum number of results to retrieve.

    Returns:
        list: A list of abstracts (strings) from the search results.
    """

    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }

    try:
        response = requests.get(base_url, params=params)

        # Raise an HTTP error if the response is 4xx-5xx
        response.raise_for_status()

        root = ET.fromstring(response.content)
            
        # Defining a variable to explicitly reference the namespace
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}

        abstracts = []
        for entry in root.findall('atom:entry', namespace):
            summary = entry.find("atom:summary", namespace)
            if summary is not None:
                abstracts.append(summary.text.strip())
            else:
                abstracts.append("No summary available")

        return abstracts

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to arXiv: {e}")
        return []

    except ET.ParseError as e:
        print(f"An error occurred while parsing the arXiv response: {e}")
        return []

