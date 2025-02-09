from app.utils import complete_text, summarize_text
from app.utils import load_text_generator, load_summarizer

text_generator = load_text_generator()
summarizer = load_summarizer()

def test_generate_text():
    prompt = "Once upon a time"
    result = complete_text(text_generator, prompt, max_length=20)
    assert isinstance(result, str)
    assert len(result) > len(prompt)

def test_summarize_text():
    text = "A long article about something very important. It goes on and on..."
    result = summarize_text(summarizer, text, max_length=15, min_length=10)
    assert isinstance(result, str)
    assert len(result) < len(text)