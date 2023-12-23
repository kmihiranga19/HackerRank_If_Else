if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for a in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for student_mark in student_marks:
        if student_mark == query_name:
            total = sum(student_marks[name])
            answer = total / 3
            formated_answer = f"{answer:.2f}"
            print(formated_answer)