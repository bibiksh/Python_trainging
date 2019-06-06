#coding=cp949
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("Welcome to the 윤년")
else:
    print("Welcome to the 평년")
