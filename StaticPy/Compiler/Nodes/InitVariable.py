class NewVariable:
    def __init__(self, name: str, annot: str, value: None | str) -> None:
        self.name = name
        self.annot = annot
        self.value = value

    def getValue(self):
        return self.value.compute()


class NewConst:
    def __init__(self, name: str, value: None | str, annot: str = None) -> None:
        self.name = name
        self.annot = annot
        self.value = value

    def getValue(self):
        return self.value.compute()
    