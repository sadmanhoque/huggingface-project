from transformers import pipeline

print("-----------------------------")
model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("text to summarize")
print(response)
