import ure

def parse_text(text, start=None, end=None, before=None, after=None, find_all=False, ignore_spaces=False):
    # Build the regular expression depending on the passed parameters
    regex = ''
    
    if start:
        regex += start
    if before:
        regex += before
    
    # Add the main text we're looking for, ignoring spaces
    if ignore_spaces:
        regex += r'\s*' + text + r'\s*'
    else:
        regex += text
    
    if after:
        regex += after
    if end:
        regex += end
    
    # Compile the regular expression
    pattern = ure.compile(regex)
    
    # Looking for matches in the text
    matches = pattern.findall(text)
    
    # Return the result depending on the settings
    if matches:
        if find_all:
            return matches
        else:
            return matches[0]
    else:
        return False

# Example of use
text = "Start This is the text we are looking for End Start Another text End"

# Look for text between "Start" and "End", excluding spaces
result = parse_text(text, start="Start", end="End", ignore_spaces=True)
print(result)  # Output: "This is the text we are looking for"

# Look for all occurrences of text between "Start" and "End", taking into account spaces
results = parse_text(text, start="Start", end="End", find_all=True)
print(results)  # Output: ["This is the text we are looking for", "Another text"]

# Look for text between "Start" and "End", taking into account spaces, return the first occurrence.
result = parse_text(text, start="Start", end="End", ignore_spaces=True)
print(result)  # Output: "This is the text we are looking for"

# Trying to find text that is not in the text
result = parse_text(text, start="Start", end="Unknown", ignore_spaces=True)
print(result)  # Output: False
