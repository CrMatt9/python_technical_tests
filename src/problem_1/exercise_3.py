def add_mod_9_to_the_beginning_of_number(number):
    assert number > 100
    # Calculate the sum of digits modulo 9
    mod_9 = number % 9

    # If the sum is 0 or 9, set it to 9
    if mod_9 == 0:
        mod_9 = 9

    # Concatenate the calculated sum to the left of the original number
    return int(str(mod_9) + str(number))
