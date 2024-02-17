class NewVariable:
    def __init__(self, left: str, operation: str, right: None | str) -> None:
        self.left = left
        self.operation = operation
        self.right = right

    def compute(self):
        result = None
        return self.checkType(self.left, self.right)
            
    def checkType(self, left, right):
        if left.simType == right.simType:
            pass
        else:
            raise BaseException()