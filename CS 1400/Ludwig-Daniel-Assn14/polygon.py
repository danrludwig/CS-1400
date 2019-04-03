class Polygon:


    def __init__(self, sides):
        self.__sides = sides

    def __add__(self, other):
        return Polygon(self.__sides + other.__sides)

    def __sub__(self, other):
        return Polygon(self.__sides - other.__sides)

    def __gt__(self, other):
        return self.__sides > other.__sides

    def __lt__(self, other):
        return self.__sides < other.__sides

    def __eq__(self, other):
        return self.__sides == other.__sides

    def __len__(self):
        return self.__sides

    def __str__(self):
        return str(self.__sides)
