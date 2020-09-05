def solution(answers):
    students_pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    students_score = []
    score = 0
    winner = []
    max_score = 0

    for student_pattern in students_pattern:
        k = 0
        score = 0

        for answer in answers:

            if k == len(student_pattern):
                k = 0

            if answer == student_pattern[k]:
                score = score + 1

            k = k + 1

        students_score.append(score)

    max_score = max(students_score)

    for i in range(len(students_score)):

        if students_score[i] == max_score:
            winner.append(i + 1)

    answer = winner

    return answer
