"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Good"] = "to be desired or approved of."
word_definitions["Bad"] = "of poor quality or a low standard."
word_definitions["Ugly"] = "unpleasant or repulsive, especially in appearance."


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["Good"],"\n")
print(word_definitions["Bad"],"\n")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word, definition) in word_definitions.items():
  print(f"The definition of '{word}' is '{definition}' \n")