class IconFamily:

    def __init__(self, name, container, leaf):
        self.name = name
        self.container = container
        self.leaf = leaf

    def get_container_icon(self):
        return self.container

    def get_leaf_icon(self):
        return self.leaf

class IconFamilyManager:
    def __init__(self):
        self.icon_families = {}

    def add_icon_family(self, name, container, leaf):
        self.icon_families[name] = IconFamily(name, container, leaf)

    def get_icon_family(self, name):
        return self.icon_families.get(name, None)

    def get_all_icon_families(self):
        return self.icon_families
