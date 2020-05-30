if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key in student_marks:
        if key == query_name:
            list_score = student_marks[query_name]
    sum_score = sum(list_score)
    len_score = len(list_score)
    score = sum_score/len_score
    print('%.2f' % score)
