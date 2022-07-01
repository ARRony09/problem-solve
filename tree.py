"""class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        spaces=' ' * self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("ASUS"))

    mobile=TreeNode("Smart Phone")
    mobile.add_child(TreeNode("Lenovo"))
    mobile.add_child(TreeNode("Realme"))
    mobile.add_child(TreeNode("Oneplus"))

    tv=TreeNode("Tv")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()


if __name__=='__main__':
    build_product_tree()"""


class Management():
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None

    def add_child(self,child):
        self.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self,property_name):
        if property_name == 'both':
            value = self.name +'('+self.designation+ ')'
        elif property_name == 'name':
            value=self.name
        else:
            value=self.designation
        
        spaces=' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)
    

def bulid_tree():
    vishwa=Management("Vishwa","Infrastructure Head")
    vishwa.add_child(Management("Dhaval", "Cloud Manager"))
    vishwa.add_child(Management("Abijit", "App Manager"))

    cto=Management("Chinmay", "CTO")
    cto.add_child(vishwa)
    cto.add_child(Management("Amir" ,"Application Head"))

    gels=Management("Gels", "HR Head")
    gels.add_child(Management("Peter", "Recruitment Manager"))
    gels.add_child(Management("Waqas", "Policy Manager"))

    ceo=Management("Nirupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(gels)
    
    return ceo


"""if __name__=='__main__':
    root_node=bulid_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")

"""

if __name__ == '__main__':
    root_node = bulid_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")

