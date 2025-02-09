from transformers import pipeline, set_seed

def load_text_generator():
    return pipeline("text-generation", model="gpt2")

def load_summarizer():
    return pipeline("summarization", model="t5-small")

def complete_text(text_generator, prompt, max_length=50):
    set_seed(42)
    output = text_generator(prompt, max_length=max_length, num_return_sequences=1)
    return output[0]["generated_text"]

def summarize_text(summarizer, text, max_length=130, min_length=30):
    summarizer = load_summarizer()
    output = summarizer(text, max_length=max_length, min_length=min_length)
    return output[0]["summary_text"]