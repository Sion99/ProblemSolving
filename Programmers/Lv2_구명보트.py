def solution(people, limit):
    answer = 0
    people.sort()
    temp = 0
    boat = 1
    min = people[0]
    temp = people
    for i in range(len(temp)):
        print(people[0])
        if min + temp[i] > limit:
            people.pop(temp[i])
            print(people)
    people.sort()
    print(people)
    # for i in range(len(people)):
    #     for j in range(len(people), i, -1):
    #         if temp + j < limit:
    #             temp +
    # for i in people:
    #     if temp + i < limit:
    #         temp += i
    #     elif temp + i == limit:
    #         boat += 1
    #         temp = 0
    #     else:
    #         boat += 1
    #         temp = i
    answer = boat

    return answer


# people = [70, 50, 80, 50]
people = [10, 20, 30, 40, 50, 60, 90, 91, 92, 93, 94, 95, 99]
limit = 100
print(solution(people, limit))
