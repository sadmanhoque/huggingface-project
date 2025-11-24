from transformers import pipeline

import sys
print(sys.executable)
print("-----------------------------")
model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("text to summarize")
print(response)