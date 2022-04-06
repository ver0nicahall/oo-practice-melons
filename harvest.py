############
# Part 1   #
############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    #muskmelon
    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    #casaba
    cas = MelonType(
        "cas",
        2003,
        'orange',
        True,
        False,
        "Casaba",
    )
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    #crenshaw
    cren = MelonType(
        "cren",
        1996,
        "green",
        True,
        False,
        "Crenshaw"
    )
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    #yellow watermleon
    yw = MelonType(
        'yw',
        2013,
        'yellow',
        True,
        True,
        'Yellow Watermelon',
    )
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    # Fill in the rest


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with")
        for pairing in (melon_type.pairings):
            print('- ', pairing)



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons = {}
    for melon_type in melon_types:
        melons[melon_type.code] = melon_type
    return melons


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, code, shape_rating, color_rating, harvested_from, harvested_by
    ):
        """Initialize a melon."""

        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.harvested_from == 3:
            return False
        if self.shape_rating > 5 and self.color_rating > 5:
            return True
        else:
            return False 
     

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
