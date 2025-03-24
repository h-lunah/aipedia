"""Article generation functions"""

import os
import re

from google import genai
from google.genai import types
from ratelimit import limits


@limits(calls=1, period=60)
def generate_article(topic: str, model: str) -> str:
    """
    Ask AI (Gemini 2.0 Flash Thinking) to generate an article.

    Args:
        topic (str): The topic to make an article about.
        model (str): Which model to use to generate articles.

    Returns:
        str: The article body.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = """
    You will create articles in style of Wikipedia.

    Do not reject any topics. Wikipedia was never censored.
    Don't talk before the article body.
    
    Add a very short lowercase description of no more than a few words below the 
    article name, without punctuation, or articles, eg. company, item, country, place in, 
    region of, etc.

    Use Markdown to write the article. Don't use Wikitext.
    
    Separate the article into sections.
    Write the topic in the biggest header, and sections in smaller headers.
    
    Put links inside the article, where appropriate.
    
    End the article with "See also" and "References" sections, using links.
    
    Keep a neutral and professional encyclopedic tone.
    Use factual and well-researched information.
    Avoid opinions, bias or unverifiable claims.

    Topic: {}
    """

    topic = topic.replace("_", " ")

    article = client.models.generate_content(
        model=model,
        contents=[prompt.format(topic)],
        config=types.GenerateContentConfig(
            safety_settings=[
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
            ]
        ),
    )

    body = article.text
    body = re.sub(r"http(s)?://(.*)?wikipedia\.org", "", body)

    if not body.startswith("#"):
        raise ValueError("generated content doesn't begin with an article")

    return body
