class grand_father:
    def __init__(self, g_f_property):
        self.grand_father_property = g_f_property

    def display_property1(self):
        print("The grand father property is", self.grand_father_property)


class father(grand_father):
    def __init__(self, f_property, g_f_property):
        self.father_property = f_property
        super().__init__(g_f_property)

    def display_property2(self):
        print("The father property is", self.father_property)


class son(father):
    def __init__(self, s_property, f_property, g_f_property):
        self.property = s_property
        super().__init__(f_property, g_f_property)

    def display_property3(self):
        print("The son property is", self.property)


son_obj = son("bike", "car", "house")

son_obj.display_property1()
son_obj.display_property2()
son_obj.display_property3()
