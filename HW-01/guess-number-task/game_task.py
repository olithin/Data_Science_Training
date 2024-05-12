"""
Number Guessing Game.
The computer guesses the number by itself.
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """ Random guess of number
    :param number:Predicted number. Defaults to 1.
    :return: Number of attempts
    """
    count = 0
    max_num = 101
    min_num = 1

    while True:
        count += 1
        predict_number = min_num + (max_num - min_num)//2
        if number == predict_number:
            break
        elif number > predict_number:
            min_num = predict_number
        else:
            max_num = predict_number
    return count


def score_game(random_predict) -> int:
    """
    How many attempts do we guess
    :param random_predict:
    :return: Mean number of attempts
    """

    count_ls = []
    #np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))
    print(f"The algorithm is able to guess the number in an average of: {score} attempts")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)

#%%
