import nltk

# Sample text (replace this with your actual text)
text = """
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

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

keywords = ['10', '15', '20', '2023', 'agenda', 'announcements', 'company', 'events', 'financial', 'introduction', 'meeting', 'members', 'minutes', 'name', 'new', 'october', 'opportunity', 'please', 'policies', 'procedures', 'staff', 'team', 'upcoming', 'updates', 'welcome']


# Extract work tasks using NLTK
work_tasks = []
for sentence in sentences:
    if any(keyword in sentence.lower() for keyword in keywords):
        work_tasks.append(sentence)

# Print the extracted work tasks
for task in work_tasks:
    print(task)
    print("---------------------")

