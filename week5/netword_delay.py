class Solution(object):
    # def __init__(self):
    #     self.dic = {}
    #     self.record = []
    
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = collections.defaultdict(dict)
        for edge in times:
            u, v, c = edge
            edges[u][v] = c

        visited = {K}
        heap = [(0, K)] # heap to find smallest/shortest path
        
        while heap: # return cost when visited set has all vs, use greed y each step
            pre_cost, u = heapq.heappop(heap)
            visited.add(u)
            if len(visited) == N:
                return pre_cost
            nexts = edges[u]
            if not nexts:
                continue
            for v in edges[u]:
                if v in visited:
                    continue
                heapq.heappush(heap, (edges[u][v] + pre_cost, v))
        return -1