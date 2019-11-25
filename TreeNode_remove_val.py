# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def find_node_and_parent(self, root, key):
        parent = None
        while root and root.val != key:
            parent = root
            if key < root.val:
                root = root.left
            else:
                root = root.right

        return root, parent

    def set_parent_child(self, parent, child, new_child):
        if parent.left is child:
            parent.left = new_child
        else:
            parent.right = new_child

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        node, parent = self.find_node_and_parent(root, key)
        if not node:
            return root  # didn't find the node

        # node has no children or 1 child
        if not node.left or not node.right:
            next = node.left or node.right
        # node has both children: find successor
        else:
            next_parent = node  # keep track of successor's parent
            next = node.right  # go one step right (we know there is a right child)
            while next.left:  # then go left while there is a left child
                next_parent = next
                next = next.left

            # "splice out" the successor; it may have a right child
            self.set_parent_child(next_parent, next, next.right)

            # replace node w/successor
            next.left = node.left
            next.right = node.right

        if not parent:  # we're deleting the root
            return next
        self.set_parent_child(parent, node, next)
        return root


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            key = int(line)

            ret = Solution().deleteNode(root, key)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
