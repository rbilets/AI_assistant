from random import randint


def read_answers(file):
    """
    Function to read and choose a single answer
    from the file
    :param file: str
    :return: str
    """
    answers = []
    with open(f"/Users/roman/Desktop/AI_assistant/answers/{file}", encoding='utf-8', mode='r') as rf:
        line = rf.readline().rstrip()
        while line:
            answers.append(line)
            line = rf.readline().rstrip()

    phrase_ind = randint(0, len(answers) - 1)
    return answers[phrase_ind]


if __name__ == '__main__':
    print(read_answers('boyfriend.txt'))
