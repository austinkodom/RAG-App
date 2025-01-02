def combine_context(query, abstracts):
    """
    Combine the user's query with the retrieved abstracts to form a context.

    Arguments:
        query (str): The user's query.
        abstracts (list): List of abstracts retrieved from arXiv.

    Returns:
        str: A single string combining the query and the abstracts.
    """

    if not abstracts:
        context = "No relevant information was found."
    else:
        # Join the abstracts into a large string.
        context = " ".join(abstracts)

    # Combine the query with the context to create the final input.
    return f"Question: {query}\nContext: {context}"
