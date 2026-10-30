import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[(node, run)] = min cost to reach node with this run length
        dist = {(0, 1): 0}          # node 0's own label counts as run = 1
        heap = [(0, 0, 1)]          # (cost, node, run)

        while heap:
            d, u, run = heapq.heappop(heap)

            if u == n - 1:
                return d            # first time we reach the target is the cheapest

            if d > dist.get((u, run), float('inf')):
                continue            # outdated entry

            for v, w in adj[u]:
                new_run = run + 1 if labels[v] == labels[u] else 1

                if new_run > k:
                    continue        # too many identical characters in a row

                nd = d + w
                if nd < dist.get((v, new_run), float('inf')):
                    dist[(v, new_run)] = nd
                    heapq.heappush(heap, (nd, v, new_run))

        return -1