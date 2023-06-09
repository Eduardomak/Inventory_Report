from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, importer):
        self.__importer = importer
        self.__index = 0

    def __next__(self):
        try:
            current_value = self.__importer[self.__index]
        except IndexError:
            raise StopIteration()
        else:
            self.__index += 1
            return current_value
