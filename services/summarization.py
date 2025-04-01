import cohere
import os

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def summarize_text(text):
    try:
        response = co.summarize(
            text=text,
            length='medium',
            format='paragraph',
            model='summarize-xlarge',
        )
        return response.summary
    except Exception as e:
        return f"Error in summarization: {str(e)}"
