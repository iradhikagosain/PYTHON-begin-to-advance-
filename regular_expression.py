#Regular expressions (regex) are powerful tools for pattern matching in strings.
#  Python's re module provides support for regex.

import re
text="python is quite a good and useful language and i like it tooo And love it"

# Search for a pattern
match=re.search("useful",text)
if match:
    print("match found")
    print("start index:",match.start())
    print("end index",match.end())

# Find all occurrences of a pattern
matches=re.findall("and",text,re.IGNORECASE)
print("matches:",matches)

# Replace all occurrences of a pattern
new_text=re.sub("python","C++",text)
print("new_text:",new_text)


# Compile a regex for efficiency (if used multiple times)
pattern = re.compile(r"\b\w+\b")  # Matches whole words
words = pattern.findall(text)
print("Words:", words)