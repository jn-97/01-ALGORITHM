# https://www.acmicpc.net/problem/2846
# import sys  

# sys.stdin = open("2_오르막길.txt")

T = int(input()) 
list_ = list(map(int, input().split())) 
cnt = 0 # 오르막길의 크기
tmp = 0 # 오르막길이 끝난 후 크기

for i in range(len(list_)-1): 
    if list_[i] < list_[i+1]: # 오르막길이면 cnt변수에 오르막길의 크기 담음
        cnt += list_[i+1] - list_[i]

    elif list_[i] >= list_[i+1]: # 내리막길이고
        if cnt > tmp: # 현재의 오르막길 > 전에 저장한 오르막길 크기
            tmp = cnt # tmp변수에 오르막길의 크기를 새로 갱신
            cnt = 0 # cnt는 초기화
        else: # 전에 저장한 오르막길의 크기가 더 크다면
            cnt = 0 # cnt만 초기화
if tmp > cnt: # 마지막으로 가장 최근의 오르막길 크기를 비교해서 더 큰 값을 가지는 변수 출력
    print(tmp)
else:
    print(cnt)