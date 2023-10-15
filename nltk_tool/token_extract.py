import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')

# Sample large text
large_text = """
Subject: Staff Meeting Agenda - October 20, 2023

To: All Employees
From: [Your Name]
Date: October 15, 2023

Dear Team,

I hope this message finds you well. We will be having our monthly staff meeting on October 20, 2023, at 2:00 PM in the conference room. Please find the agenda for the meeting below:

Agenda:

1. Welcome and Introduction (5 minutes)
   - Brief welcome and introduction of any new team members.

2. Project Updates (15 minutes)
   - Team leads to provide updates on ongoing projects.

3. Financial Report (10 minutes)
   - Presentation of the latest financial performance and budget updates.

4. Employee Recognition (5 minutes)
   - Recognizing outstanding contributions and achievements by team members.

5. New Policies and Procedures (10 minutes)
   - Discussion of any new company policies or changes in procedures.

6. Open Floor (15 minutes)
   - An opportunity for team members to raise questions, concerns, or suggestions.

7. Upcoming Events and Announcements (5 minutes)
   - Information on upcoming company events and important announcements.

8. Adjournment (2 minutes)

If you have any additional items you would like to include in the agenda, please email me by October 18, 2023.

Your presence and participation in this meeting are highly encouraged, as it is a great opportunity to stay informed and involved in the company's activities.

Thank you, and I look forward to seeing you all on October 20th.

Best regards,
[Your Name]
"""

# Tokenize the large text into words
words = word_tokenize(large_text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join the filtered words back into a single string
cleaned_text = ' '.join(filtered_words)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the text data
tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_text])

# Get the feature names (terms)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Extract keywords with high TF-IDF scores
threshold = 0.2  # Adjust the threshold as needed
work_related_keywords = [feature for feature, score in zip(feature_names, tfidf_matrix.toarray()[0]) if score > threshold]

# Print the dynamically extracted work-related keywords
print("Dynamically extracted work-related keywords from the text:")
print(work_related_keywords)
