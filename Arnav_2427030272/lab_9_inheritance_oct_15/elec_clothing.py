"""
2. 
an online store has a base class product and 2 derived classes : electronics, clothing
electronics attributes : brand, warrenty
clothing attributes : size, fabric_type
"""

class product:
    def __init__(self, p_id):
        self.p_id = p_id

class electronics(product):
    def __init__(self, p_id, brand, warrenty):
        self.brand = brand
        self.warrenty = warrenty
        super().__init__(p_id)
    def print_elec(self):
        print(self.p_id)
        print(self.brand)
        print(self.warrenty)

class clothing(product):
    def __init__(self, p_id, size, fabric_type):
        self.size = size
        self.fabric_type = fabric_type
        super().__init__(p_id)
    def print_clo(self):
        print(self.p_id)
        print(self.size)
        print(self.fabric_type)

obj1 = electronics(12345, "samsung", "2 yrs")
obj1.print_elec()
print()
obj2 = clothing(67890, "large", "silk")
obj2.print_clo()