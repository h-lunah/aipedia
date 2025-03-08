"""Text formatting functions"""


def wiki_capitalize(text: str) -> str:
    """
    Capitalize the article text like Wikipedia.

    Args:
        text (str): The input text to capitalize.

    Returns:
        str: The capitalized string.
    """

    return f"{text[0].upper()}{text[1:]}"


def extract_article(text: str) -> str:
    """
    Extract everything after the first heading and its tagline.

    Args:
        text (str): The input text containing the article

    Returns:
        str: The extracted content
    """
    # Split the text into lines
    lines = text.split("\n")

    # Find the first line that starts with '#' (Markdown heading)
    heading_index = next(
        i for i, line in enumerate(lines) if line.strip().startswith("#")
    )

    # Tagline is assumed to be the next non-empty line after the heading
    tagline_index = None
    for i in range(heading_index + 1, len(lines)):
        if lines[i].strip():
            tagline_index = i
            break

    if tagline_index is None:
        return ""

    # Extract content starting from after the tagline
    extracted_content = "\n".join(lines[tagline_index + 1 :])
    return extracted_content.strip()


def extract_subtitle(text: str) -> str:
    """
    Extract the tagline (first non-empty line after the first heading).

    Args:
        text (str): The input text containing the article

    Returns:
        str: The extracted tagline
    """
    # Split the text into lines
    lines = text.split("\n")

    # Find the first line that starts with '#' (Markdown heading)
    heading_index = next(
        i for i, line in enumerate(lines) if line.strip().startswith("#")
    )

    # Tagline is assumed to be the next non-empty line after the heading
    for i in range(heading_index + 1, len(lines)):
        if lines[i].strip():
            return lines[i].strip()

    return ""
