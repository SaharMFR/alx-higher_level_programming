#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        returns = len(sentence), sentence[0]
    else:
        returns = len(sentence), None
    return returns
