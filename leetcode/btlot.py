# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      queue = [root]
      result = []
    #   if root:
    #     result.append([root.val])
      while queue:
        # print(result, queue)
        current_level = []
        reps = len(queue)
        for _ in range(reps):
            next_element = queue.pop(0)
            if next_element and next_element.val is not None:
                current_level.append(next_element.val)
            if next_element and next_element.left:
                queue.append(next_element.left)
            if next_element and next_element.right:
                queue.append(next_element.right)
        if len(current_level) > 0:
            result.append(current_level)
      return result


