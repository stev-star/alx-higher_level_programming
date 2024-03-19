#!/usr/bin/python3

def multiple_returns(sentence):
    if not  sentence:
        return (None, None)
    else:
        return (len(sentence), sentence[0])

print(multiple_returns("Hello"))
print(multiple_returns(""))
