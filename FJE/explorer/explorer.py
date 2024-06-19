from abc import ABC, abstractmethod

class Leaf:
    def __init__(self, name, icon=None):
        self.name = name
        self.icon = icon

    def draw(self):
        pass

class Container:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.icon = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
    def draw(self):
        pass

class FunnyJsonExplorer:
    def __init__(self, style, icon_family):
        self.style = style
        self.icon_family = icon_family
        self.root_container = Container("root", level=0)

    def show(self, data):
        # 构建树结构
        self._load(data, self.root_container)
        # 使用样式渲染数据
        self.style.draw(self.root_container, self.icon_family)

    def _load(self, data, parent_container):
        for key, value in data.items():
            if isinstance(value, dict):
                # 如果值是字典，则创建新的容器节点并递归加载
                new_container = Container(key, parent_container.level + 1)
                parent_container.add_child(new_container)
                self._load(value, new_container)
            else:
                # 如果值不是字典，则创建叶子节点
                if isinstance(value, str):
                    key = f"{key}: {value}"
                leaf = Leaf(key)
                parent_container.add_child(leaf)
