class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1)) # each node is root of own subtree

        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node]) # set root for node as root of subtree
            return root[node] # found root of subtree

        for node1, node2 in edges: 
            root1, root2 = find_root(node1), find_root(node2)

            if root1 == root2:
                return [node1, node2] # both nodes are already in same subtree
 
            root[root2] = root1 # found new connection between nodes / subtrees
            # root[root1] = root2 also works            
