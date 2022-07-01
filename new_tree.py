"""class Country():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        self.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_tree():
    root=Country("Global")

    india=Country("India")
    india.add_child(Country("Gujrat"))
    india.add_child(Country("Karnataka"))

    usa=Country('USA')
    usa.add_child(Country('New Jersey'))
    usa.add_child(Country('California'))

    guj=Country("Gujrat")
    guj.add_child(Country('Ahmedabad'))
    guj.add_child(Country('Baroda'))

    kar=Country("Karnataka")
    kar.add_child(Country("Bangluru"))
    kar.add_child(Country("Mysore"))

    newjersey=Country("New Jersey")
    newjersey.add_child(Country("Princeton"))
    newjersey.add_child(Country("Trenton"))

    california=Country("California")
    california.add_child(Country("San Francisco"))
    california.add_child(Country("Mountain View"))
    california.add_child(Country("Palo Alto"))

    root.add_child(Country("India"))
    root.add_child(Country("USA"))

    root.print_tree()


if __name__ == '__main__':
    root=build_tree()
    print(root.print_tree())"""