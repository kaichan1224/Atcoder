from collections import deque,defaultdict
def solve_puzlze(start_state):
    connect = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
    start = ''.join(map(str,start_state))
    goal = '123456780'#正解の順番
    state_dictinary = defaultdict(int)
    state_dictinary[start] = 0
    q = deque()
    q.append((start,0))#マスの状態、手数
    while q:
        now,cnt = q.popleft()
        if now==goal:
            return cnt 
        zero_location = now.index(str(0))
        for nxt in connect[zero_location]:
            l = list(now)
            l[nxt],l[zero_location] = l[zero_location],l[nxt]
            tmp = ''.join(l)
            if tmp not in state_dictinary:
                q.append((tmp,cnt+1))
                state_dictinary[tmp] = 1
start = [8,6,7,2,5,4,3,0,1]
print(solve_puzlze(start))
