#!/usr/bin/python3

def best_score(a_dict):
    max_score = 0
    best_player = None
    if isinstance(a_dict, dict):
        for player, score in a_dict.items():
            if score > max_score:
                max_score = score
                best_player = player
    return best_player
