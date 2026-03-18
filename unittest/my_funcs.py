# Unittest 작성 실습 - 다음 함수를 작성하고 pytest로 동작함을 보이세요.
# 홀수 짝수 판별하기 - 주어진 값이 짝수이면 True, 홀수이면 False를 반환하는 함수
# 평균 구하기 - 주어진 정수 list내의 값들의 평균을 반환하는 함수
# 최댓값 구하기 - 주어진 정수 list 내의 최댓값을 반환하는 함수
# 최솟값 구하기 - 주어진 정수 list 내의 최솟값을 반환하는 함수

def is_even(n):
    return n % 2 == 0

def average(lst):
    return sum(lst) / len(lst)

def max_value(lst):
    return max(lst)

def min_value(lst):
    return min(lst)