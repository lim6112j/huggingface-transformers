from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier(
    ["I've benn waiting for a Hugginface course my whole life.", "I hate this"])
print(result)
