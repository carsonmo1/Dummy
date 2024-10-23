def count_token_in_corpus(token, file_path="corpus.txt"):
    """Counts how many times a token appears in the text file."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text.lower().split().count(token.lower())
    except FileNotFoundError:
        return 0  # Handle case where file doesn't exist