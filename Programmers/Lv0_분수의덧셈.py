import fractions


def solution(denum1, num1, denum2, num2):
    a = num1 * num2
    b = denum1 * num2 + denum2 * num1
    temp = fractions.Fraction(a, b)
    c = temp.numerator
    d = temp.denominator
    answer = [d, c]

    return answer
