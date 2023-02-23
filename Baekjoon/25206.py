sum = 0
sum2 = 0
grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
          'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for i in range(20):
    scores = input().split()
    if scores[2] != 'P':
        sum += grades[scores[2]] * float(scores[1])
        sum2 += float(scores[1])

sum /= sum2
print(sum)
