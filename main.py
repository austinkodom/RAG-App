from src.retrieval import search_arxiv
from src.augmentation import combine_context
from src.generation import generate_response

def main():
    query = input("Enter your query: ").strip()
    print("\nSearching for relevant abstracts...")

    max_results = 5
    abstracts = search_arxiv(query, max_results)
    if not abstracts:
        print("No relevant abstracts found. Try another query.")
        return

    context = combine_context(query, abstracts)
    print("\nContext created...Passing to generative model...")

    print("\nGenerating Response...")
    response = generate_response(context)
    print(response)

if __name__ == "__main__":
    main()


