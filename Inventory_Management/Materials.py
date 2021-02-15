

class Material:
    id = 0

    def __init__(self, name, supplier, part_number):
        self.name = name
        self.supplier = supplier
        self.part_number = part_number
        self.id = self._generate_id()
        self.receipt_lots = []

    def _generate_id(self):
        '''Assigns an ID and iterates.'''
        Material.id += 1
        return Material.id

    def add_receipt_lot(self, receipt_lot):
        '''
        :receipt_lot: Class
        '''

        pass

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value


class Biological(Material):
    def __init__(self, name, supplier, part_number):
        super().__init__(name, supplier, part_number)
        


class LabSupply(Material):
    def __init__(self, name, supplier, part_number):
        super().__init__(name, supplier, part_number)




class Chemical(Material):
    def __init__(self, name, supplier, part_number):
        super().__init__(name, supplier, part_number)


class ReceiptLot:
    def __init__(self):
        pass


class Container:
    id = 0
    controlled_terms = ['container_type','other']


    def __init__(self, quantity, unit_of_measure):
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure


    def set_attribute(self, data):
            for key in data:
                if key in Container.controlled_terms:
                    setattr(self, key, initial_data[key])

    def _generate_id(self):
        '''Assigns an ID and iterates.'''
        Container.id += 1
        return Container.id



class Size:
    def __init__(self):
        pass




'''
bleach = Material('clorox', 'clorox (again)', '11234234b')
other = Biological('something', 'clorox (again)', '11234234b')
other_other = Material('something', 'clorox (again)', '11234234b')

print(dir(bleach))

print(bleach.__iter__().__next__())

print(bleach.id, other.id,other_other.id)
print(bleach.id, other.id,other_other.part_number)
'''