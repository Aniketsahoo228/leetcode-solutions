from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        # iterative DFS from root 0: Euler tour + parents
        timer = 0
        stack = [(0, 0, False)]
        while stack:
            node, par, done = stack.pop()
            if done:
                tout[node] = timer - 1
                continue
            up[0][node] = par
            tin[node] = timer
            timer += 1
            stack.append((node, par, True))
            for nxt in adj[node]:
                if nxt != par:
                    depth[nxt] = depth[node] + 1
                    stack.append((nxt, node, False))

        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return up[0][a]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def add(i: int, x: int) -> None:
            i += 1
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i

        def prefix(i: int) -> int:
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def range_xor(l: int, r: int, x: int) -> None:
            add(l, x)
            add(r + 1, x)

        chars = [1 << (ord(c) - 97) for c in s]
        for w in range(n):
            range_xor(tin[w], tout[w], chars[w])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), 1 << (ord(parts[2]) - 97)
                delta = chars[u] ^ c
                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = prefix(tin[u]) ^ prefix(tin[v]) ^ chars[l]
                ans.append(mask & (mask - 1) == 0)
        return ans
        