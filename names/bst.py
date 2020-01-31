class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case
        if self.value == target:
            return True

        if self.value < target and self.right:
            return self.right.contains(target)

        elif self.value < target and self.left:
            return self.left.contains(target)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        left_max = None
        right_max = None
        if self.left:
            left_max = self.left.get_max()
            if left_max > max_val:
                max_val = left_max
            if self.right:
                right_max = self.right.get_max()
                if right_max > max_val:
                    max_val = right_max
            return max_val
