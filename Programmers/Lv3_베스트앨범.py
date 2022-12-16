def solution(genres, plays):
    answer = []
    play_dict = {}
    index_dict = {}
    arr = []
    for i in range(len(genres)):
        play_dict[genres[i]] = 0
        index_dict[genres[i]] = {}

    for i in range(len(genres)):
        play_dict[genres[i]] += plays[i]
        index_dict[genres[i]][i] = plays[i]

    temp = {v: k for k, v in play_dict.items()}
    a = list(temp.keys())
    a.sort(reverse=True)
    print(a)
    for i in a:
        b = temp[i]
        print(b)
        print(index_dict[b].items())
        sorted(index_dict[b].items(), key=lambda x: x[1], reverse=True)
        print(index_dict[b].items())
        bb = list(index_dict[b].keys())
        print(bb)
        for i in range(2):
            if bb:
                answer.append(bb.pop())
        print(answer)
        # sorted(index_dict[genres[temp[i]]].items(), key=lambda x:x[1])

    print(a)
    print(temp[a[0]])
    # for i in range(len(play_dict)):

    print(play_dict)
    print(index_dict)
    return answer
