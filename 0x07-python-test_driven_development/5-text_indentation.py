#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """prints with 2 new lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    checks = "?.:"
    newstr = ""
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while (i < len(text)):
        newstr += text[i]
        if text[i] == '\n' or text[i] in checks:
            if text[i] in checks:
                newstr += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(newstr, end="")
