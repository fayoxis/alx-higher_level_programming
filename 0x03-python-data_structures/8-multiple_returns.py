#!/usr/bin/python3


def multiple_returns(sentence):
    s_len = len(sentence)
    f_char = sentence[0] if s_len > 0 else None
    return (s_len, f_char)
