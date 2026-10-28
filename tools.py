from smolagents import tool

@tool
def get_word_count(text: str) -> int:
    """
    Counts the number of words in a piece of text.

    Args:
        text: The text whose words should be counted.
    """
    return len(text.split())