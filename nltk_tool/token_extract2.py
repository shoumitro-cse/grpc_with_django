import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
nltk.download('stopwords')


# Sample large text (replace this with your actual text)
large_text = """
**Work Note: [Date]**

**To:** [Recipient's Name/Department]
**From:** [Your Name/Position]
**Subject:** Work Update and Progress Report

---

**I. Introduction:**

I hope this note finds you in good health and high spirits. This work note aims to provide a comprehensive overview of the progress made, challenges faced, and future plans in our ongoing projects and tasks. Your attention to the following points is highly appreciated.

---

**II. Project Updates:**

1. **Project Name/Number:** [Project Name/Number]
   - **Progress:** [Brief overview of the project's current status, including milestones achieved and tasks completed.]
   - **Challenges:** [Outline any challenges faced, such as resource constraints, technical difficulties, or external factors.]

2. **Project Name/Number:** [Project Name/Number]
   - **Progress:** [Brief overview of the project's current status, including milestones achieved and tasks completed.]
   - **Challenges:** [Outline any challenges faced, such as resource constraints, technical difficulties, or external factors.]

[Continue this section for all ongoing projects, providing concise updates and challenges.]

---

**III. Task Accomplishments:**

- [List down specific tasks completed since the last work note. Include any notable achievements or improvements.]

---

**IV. Upcoming Tasks:**

- [Enumerate tasks that are planned for the upcoming period. Include deadlines, responsibilities, and any dependencies.]

---

**V. Issues and Concerns:**

- **Issues Raised:** [List any issues that have been raised during the reporting period. Provide a brief description of each issue.]
- **Proposed Solutions:** [Suggest potential solutions or actions that can be taken to address the raised issues.]

---

**VI. Team Update:**

- **New Team Members:** [List any new team members who joined during the reporting period. Provide a brief introduction.]
- **Team Challenges:** [Highlight any challenges faced by the team as a whole. These might include communication issues, collaboration problems, or workload concerns.]
- **Recognition and Appreciation:** [Acknowledge outstanding contributions made by team members. This fosters a positive work environment.]

---

**VII. Conclusion:**

In conclusion, the team has been working diligently to meet our project goals. Despite challenges faced, we are confident in our ability to overcome them and achieve successful outcomes. Your support and understanding are invaluable in this process. If you have any questions or require further details on any of the points mentioned in this work note, please do not hesitate to contact me.

Thank you for your time and consideration.

Warm regards,

[Your Full Name]
[Your Position]
[Your Email Address]
[Your Phone Number]
[Organization Name]

"""
# Tokenize the text into words
words = word_tokenize(large_text)

# Remove stopwords and convert to lowercase
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Calculate word frequencies
word_freq = FreqDist(filtered_words)

# Determine the most significant words using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([' '.join(filtered_words)])
feature_names = tfidf.get_feature_names_out()

# Set a threshold for TF-IDF scores (adjust as needed)
threshold = 0.1

# Extract work-related words based on TF-IDF scores
work_related_words = [feature for feature, score in zip(feature_names, tfidf_matrix.toarray()[0]) if score > threshold]

# Print the dynamically extracted work-related words
print("Dynamically extracted work-related words from the text:")
print(work_related_words)
