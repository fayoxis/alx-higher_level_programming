#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score_weight_pairs = [(score * weight, weight) for score, weight in my_list]
    total_score = sum(score for score, _ in score_weight_pairs)
    total_weight = sum(weight for _, weight in score_weight_pairs)

    return total_score / total_weight
