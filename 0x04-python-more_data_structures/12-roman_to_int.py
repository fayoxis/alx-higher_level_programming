def roman_to_int(roman_string):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    total = 0
    prev_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        current_value = roman_values.get(roman_string[i], 0)

        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value

        prev_value = current_value

    return total
