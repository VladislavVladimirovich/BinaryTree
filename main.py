
class BinTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.number = None

    def set_number(self, data: list):
        for i in data:
            self.__set_recursion(i)

    def __set_recursion(self, data):
        if self.number is None:
            self.number = data
            return

        if self.number > data:
            if self.left is None:
                self.left = BinTree()
            self.left.__set_recursion(data)
        else:
            if self.right is None:
                self.right = BinTree()
            self.right.__set_recursion(data)

    def find_number(self, data: int) -> bool:
        if data == self.number:
            return True

        if data > self.number:
            if self.right is None:
                return False
            return self.right.find_number(data)
        else:
            if self.left is None:
                return False
            return self.left.find_number(data)


def main():
    tree = BinTree()
    tree.set_number([7, 3, 10, 5, 2, 9, 13, 12, 17, 1])

    print(tree.find_number(15))
    print(tree.find_number(1))


if __name__ == '__main__':
    main()
