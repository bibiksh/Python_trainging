#coding=cp949
#에베베ㅂ벱베ㅔ베베ㅔ베벱ㅂ베베베ㅔㅂㅂ베벱ㅂㅂ베
#ㅅㄱ
#사과
#사고
#실과
#시기
#실기
"""
3
10 20 30
30 40 50
50 60 70
"""
#===================
"""
[['10', '20', '30'], ['30', '40', '50'], ['50', '60', '70']]
"""
n=int(input())
#===============================================================================
# nlist=[]
# for i in range(n):
#     #a=list(input().split())
#     a=list(map(str,input().split()))
#     #print(a)
#     nlist.append(a)
#     
#===============================================================================
    
mlist=[input().split() for i in range(n)]
print(mlist)