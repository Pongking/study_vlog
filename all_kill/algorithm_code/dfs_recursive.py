'''
选择起始节点 并将其标记为已访问。
检查当前节点是否为目标节点（看具体题目要求）。
如果当前节点 是目标节点，则直接返回结果。
如果当前节点 不是目标节点，则遍历当前节点 的所有未访问邻接节点。
对每个未访问的邻接节点 从节点 出发继续进行深度优先搜索（递归）。
如果节点 没有未访问的相邻节点，回溯到上一个节点，继续搜索其他路径。
重复 步骤，直到遍历完整个图或找到目标节点为止。
'''


class Solution:
    def dfs_recursive(self,graph,u,visited):
        print(u)
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                self.dfs_recursive(graph,v,visited)
    def dfs_stack(self,graph,u):
        print(u)
        visited,stack=set(),[]
        stack.append([u,0])
        visited.add(u)
        while stack:
            u,i=stack.pop()
            if i<len(graph[u]):
                v=graph[u][i]
                stack.append([u,i+1])
                if v not in visited:
                    print(v)
                    stack.append([v,0])
                    visited.add(v)

graph={
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

visited=set()
# Solution().dfs_recursive(graph,"A",visited)
Solution().dfs_stack(graph,"A")