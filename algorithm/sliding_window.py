def sliding_window(A, N, K):
    """
    尺取り法: 右端を必ず追加して、条件を壊したら左端を縮める型
    例: 和が K 以下の最長区間
    """

    left = 0
    current = 0
    ans = 0

    for right in range(N):
        current += A[right]

        while current > K:
            current -= A[left]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


from collections import deque


def sliding_window(A, N, K):
    """
    queueを使った尺取法
    例: 和が K 以下の最長区間
    """

    q = deque()
    total = 0
    ans = 0

    for x in A:
        q.append(x)
        total += x

        while q and total > K:
            total -= q.popleft()

        ans = max(ans, len(q))
