# pip install nltk


import nltk
from nltk.tokenize import sent_tokenize

# Download the punkt tokenizer if you haven't already
nltk.download('punkt')

def extract_important_tasks(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Assume important sentences are those containing certain keywords
    keywords = ['important', 'urgent', 'priority', 'deadline', 'critical']  # Customize as needed
    important_tasks = []
    
    # Extract sentences containing keywords
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in keywords):
            important_tasks.append(sentence)
    
    return important_tasks

# Example large text
large_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Important task: Submit the report by Friday. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
Please review the new proposal and provide your feedback. Urgent: Call the client regarding the project updates. Excepteur sint occaecat cupidatat non proident.
"""

# Extract and print important tasks as bullet points
important_tasks = extract_important_tasks(large_text)
for i, task in enumerate(important_tasks, start=1):
    print(f"• Task {i}: {task}")

