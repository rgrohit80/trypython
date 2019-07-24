class newNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" "),
        inorder(root.right)

def search(root, key):
    if root is None or root.val == key:
        return root
    elif key < root.val:
        return search(root.left, key)
    elif key > root.val:
        return search(root.right, key)


def deleteNode(root, key):
    temp = root
    while temp.right:
        temp = temp.right
    dnode = search(root, key)
    dnode.val = dnode.left.val
    print(dnode.left.val, dnode.val)
    del dnode.left







def insert(root, key):
    q = []
    q.append(root)
    while (len(q)):
        root = q[0]
        q.pop()
        if (not root.left):
            root.left = newNode(key)
            break
        else:
            q.append(root.left)
        if (not root.right):
            root.right = newNode(key)
            break
        else:
            q.append(root.right)


# def printPostorder(root):
#     if root:
#         printPostorder(root.left)
#         printPostorder(root.right)
#         print(root.val),
#
#
# def printPreorder(root):
#     if root:
#         print(root.val),
#         printPreorder(root.left)
#         printPreorder(root.right)

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(20)
    root.right = newNode(30)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    deleteNode(root, 10)
    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
