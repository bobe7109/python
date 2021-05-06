marks = []

for i in range(5):
    scr = int(input("%d 번 학생의 성적 : " % (i+1)))
    marks.append(scr)

number = 0
sum = 0
print(marks)

for i in marks:
    sum += i     # sum = sum + i
    number = number + 1
    if i >= 60:
        print("%d번 학생의 점수는 %d이고  합격입니다." % (number,i))
    else:
        print("%d번 학생의 점수는 %d이고 불합격입니다." % (number,i))

print("총합은 %d이고 평균은  %f입니다." % (sum, (sum/number)))

