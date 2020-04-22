class ArtificialChristmasTree:
    color = 'Green'

    def __init__(self, name_of_manufacturer=None, price_in_uah=None, height_in_cm=None, material=None,
                 weight_in_kg=None, year_of_production=None,
                 is_snow_covered=None):
        self.name_of_manufacturer = name_of_manufacturer
        self.price_in_uah = price_in_uah
        self.height_in_cm = height_in_cm
        self.material = material
        self.weight_in_kg = weight_in_kg
        self.year_of_production = year_of_production
        self.is_snow_covered = is_snow_covered

    def __str__(self):
        name_of_manufacturer = "Name of manufacturer: {0}\n".format(self.name_of_manufacturer)
        price_in_uah = "Price in UAH: {0}\n".format(self.price_in_uah)
        height_in_cm = "Height in centimeters: {0}\n".format(self.height_in_cm)
        material = "Material: {0}\n".format(self.material)
        weight_in_kg = "Weight in kilograms: {0}\n".format(self.weight_in_kg)
        year_of_production = "Year of production: {0}\n".format(self.year_of_production)
        is_snow_covered = "Covered by snow: {0}\n".format(self.is_snow_covered)
        color = "Color: {0}\n".format(ArtificialChristmasTree.color)
        return name_of_manufacturer + price_in_uah + height_in_cm + material \
            + weight_in_kg + year_of_production + is_snow_covered + color

    def __del__(self):
        print("Deleting tree... ")
        del self.name_of_manufacturer
        del self.price_in_uah
        del self.height_in_cm
        del self.material
        del self.weight_in_kg
        del self.year_of_production
        del self.is_snow_covered
        del self
        print("Done!")

    @staticmethod
    def get_color():
        return ArtificialChristmasTree.color


def main():
    default_tree = ArtificialChristmasTree()
    tree = ArtificialChristmasTree("Virpol", 1499, 200, "plastic")
    second_tree = ArtificialChristmasTree("ukrElka", 999, 175, "plastic", 5, 2018, True)
    print(default_tree)
    print(tree)
    print(second_tree)


main()
