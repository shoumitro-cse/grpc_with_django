import nltk

# Sample text (replace this with your actual text)
text = """
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

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

keywords = ['brief', 'challenges', 'completed', 'faced', 'include', 'issues', 'list', 'members', 'name', 'note', 'number', 'overview', 'period', 'progress', 'project', 'provide', 'raised', 'tasks', 'team', 'work']


# Extract work tasks using NLTK
work_tasks = []
for sentence in sentences:
    if any(keyword in sentence.lower() for keyword in keywords):
        work_tasks.append(sentence)

# Print the extracted work tasks
for task in work_tasks:
    print(task)
    print("---------------------")

