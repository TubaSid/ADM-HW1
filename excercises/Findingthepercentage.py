if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = raw_input()
    sum=0
    sn=len(student_marks[query_name])
    for i in range(sn):
        sum+=student_marks[query_name][i]
    avg="{:.2f}".format(sum/sn)
    print(avg)
