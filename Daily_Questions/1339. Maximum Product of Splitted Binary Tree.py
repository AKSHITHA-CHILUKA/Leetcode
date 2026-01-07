class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(node):
            if not node:
                return 0
            
            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        total = dfs(root)

        ans = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                continue

            
            current_product = (total - node.val) * node.val
            ans = max(ans, current_product)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans % MOD
