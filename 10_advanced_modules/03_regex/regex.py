import re

text = "My email is dimah.code@gmail.com and my backup is contact_dimah@yahoo.com"

# Find all email addresses in the text
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Found emails:", emails)

# Check if a string starts with 'My'
if re.match(r"^My", text):
    print("The text starts with 'My'")

# Replace all emails with a placeholder
hidden_text = re.sub(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[hidden email]", text
)
print("Hidden text:", hidden_text)

# Split the text by spaces
words = re.split(r"\s+", text)
print("Split words:", words)
