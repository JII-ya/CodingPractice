def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    best = 0
    def dfs(cur_k, cnt):
        nonlocal best
        if cnt > best:
            best = cnt

        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and cur_k >= need:
                visited[i] = True
                dfs(cur_k - cost, cnt + 1)
                visited[i] = False
    dfs(k, 0)
    return best