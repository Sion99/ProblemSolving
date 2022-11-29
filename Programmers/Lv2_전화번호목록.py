# 11/29
# startswith()이라는 메소드를 알게 되었던 문제
# 이중 for문은 굉장히 비효율적이라
# 한번 정렬한 뒤에 바로 다음칸을 비교하는 식으로 진행했다


def solution(phone_book):
    answer = True
    # 하나의 배열 원소가 다른 원소의 시작부분이면 false
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
        else:
            i += 1

    return answer
