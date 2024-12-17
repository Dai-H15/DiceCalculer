class DiceData():
    def __init__(self, name: str, datalist: list[int]):
        self.name: str = name
        self.datalist: list[int] = datalist
    name: str
    datalist: list[int | float | str]
    result: int = 0

    def __str__(self):
        return f"{self.name} x target 's result = {self.result}"


class DiceCalc():
    def __init__(self, target: DiceData, data: list[DiceData]):
        self.target: DiceData = target
        self.data: list[DiceData] = data
    target: DiceData
    data: list[DiceData] = []

    def calc(self):
        for mini in self.data:
            now = 0
            upper = 0
            if len(mini.datalist) != len(self.target.datalist):
                raise ValueError("Data length is incorrect")
            for data in mini.datalist:
                if data == 1 and (self.target.datalist[now] == 1):
                    upper += 1
                now += 1
            lower = sum(self.target.datalist) + sum(mini.datalist)
            mini.result = (upper * 2) / lower
        return self.__str__()

    def __str__(self, data: list[DiceData] = None):
        res = "\n".join(i.__str__() for i in self.data)
        if data is not None:
            res = "\n".join(i.__str__() for i in data)
        return res

    def max_sort(self):
        check = 0
        check += sum([x.result for x in self.data])
        if check == 0:
            self.calc()
        self.sorted_data = sorted(self.data, key=lambda x: x.result, reverse=True)
        print(" ".join(f"{x.name}→" for x in self.sorted_data))
        return self.__str__(self.sorted_data)
