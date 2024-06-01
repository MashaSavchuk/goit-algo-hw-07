class BinaryTree:
    class Node:
        def __init__(self, key, data=None, left_node=None, right_node=None):
            self.key = key
            self.data = data
            self.left_node = left_node
            self.right_node = right_node

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.root = None

    def add(self, key, data=Node):
        def _add(key, data, node):
            if node is None:
                return BinaryTree.Node(key, data)
            if node.key == key:
                node.data = data
            if node.key > key:
                node.left_node = _add(key, data, node.left_node)
            else:
                node.right_node = _add(key, data, node.right_node)
            return node

        self.root = _add(key, data, self.root)

    def get(self, key):
        def _get(key, node):
            if node is None:
                return None
            if node.key == key:
                return node.data
            if node.key > key:
                return _get(key, node.left_node)
            else:
                return _get(key, node.right_node)

        return _get(key, self.root)

    # Task 1: Find the biggest node

    def find_biggest_node(self):
        def _find_biggest_node(node):
            if node.right_node is None:
                return node.key
            return _find_biggest_node(node.right_node)

        return _find_biggest_node(self.root)

    # Task 2: Find the smallest node
    # Для знаходження найменшого значення в двійковому дереві пошуку (BST) або AVL-дереві, потрібно знайти найлівіший вузол. 
    # Це тому, що в BST значення у лівому піддереві завжди менше ніж у корені та правому піддереві.

    def find_smallest_node(self):
        def _find_smallest_node(node):
            if node.left_node is None:
                return node.key
            return _find_smallest_node(node.left_node)

        return _find_smallest_node(self.root)

    # Task 3: Find the sum of all nodes
    # Для знаходження суми всіх значень у двійковому дереві пошуку (BST) або AVL-дереві, 
    # потрібно рекурсивно обійти всі вузли та підсумувати їх значення.

    def sum(self):
        def _sum(node):
            if node is None:
                return 0
            return _sum(node.left_node) + node.key + _sum(node.right_node)

        return _sum(self.root)
    
    # Helper method to display the tree
    def __str__(self):
        def bfs(node_list):
            result = ""
            if len(node_list) == 0:
                return result
            next_level = []
            for node in node_list:
                if node is not None:
                    result += str(node.key) + "\t"
                    next_level.append(node.left_node)
                    next_level.append(node.right_node)
            result += "\n" + bfs(next_level)
            return result

        return bfs([self.root])

# Test the BinaryTree class
b_tree = BinaryTree()

b_tree.add(6, "Pear")
b_tree.add(3, "Apple")
b_tree.add(0, "Plum")  # The smallest key
b_tree.add(5, "Orange")
b_tree.add(9, "Lemon")
b_tree.add(7, "Cherry")
b_tree.add(16, "Apricot")  # The biggest key

# Test output
print("Show tree", b_tree, sep="\n")
print("The sum of the keys of the vertices:", b_tree.sum())  # 36
print("Binary smallest node:", b_tree.find_smallest_node())  # 0
print("Binary biggest node:", b_tree.find_biggest_node())  # 12


class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = ' ' * level * 4
        print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Test the Comment class
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
