class IncreasingList:
    def __init__(self):
        self._list = []
        self.size = 0

    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val,
        starting from the last one, and once there are no greater element in the list,
        it appends val to the end of the list
        """
        # self._list = [element for element in self._list if element <= val]
        i = 0
        for element in reversed(self._list):
            if val < element:
                i += 1
            else:
                break

        if i > 0:
            self._list = self._list[:-i] + [val]
        else:
            self._list.append(val)

        # self._list.append(val)

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise,
        if the list is empty, it does nothing
        """
        if len(self._list) > 0:
            return self._list.pop()

    def __len__(self):
        """
        returns the number of elements in the list
        """
        return len(self._list)


def main():
    il = IncreasingList()
    assert len(il) == 0
    il.append(2)
    il.append(4)
    il.append(5)
    assert len(il) == 3
    il.append(2)
    assert len(il) == 2
    il.pop()
    assert len(il) == 1


if __name__ == '__main__':
    main()
