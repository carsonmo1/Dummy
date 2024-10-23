from .counter import count_token_in_corpus

def report_count(token, file_path="corpus.txt"):
    """Generates and prints the result using the token count."""
    count = count_token_in_corpus(token, file_path)
    print(f"The term '{token}' shows up in the corpus {count} times.")