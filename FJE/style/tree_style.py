from .style import Style
from explorer.explorer import Container, Leaf

class TreeStyle(Style):
    def draw(self, data, icon_family):
        def _print_tree(node, indent=0, is_last=True, parent_prefix=""):
            if node.name == "root":
                # 特殊处理根节点，直接递归其子节点
                for i, child in enumerate(node.children):
                    _print_tree(child, indent=0, is_last=(i == len(node.children) - 1), parent_prefix="")
            else:
                # 根据节点位置确定连接符和前缀
                connector = "└── " if is_last else "├── "
                next_prefix = "    " if (isinstance(node, Leaf) or is_last) else "│   "
                
                # 打印当前节点
                if isinstance(node, Leaf):
                    print(parent_prefix + connector + f"{icon_family.get_leaf_icon()} {node.name}")
                else:
                    print(parent_prefix + connector + f"{icon_family.get_container_icon()} {node.name}")
                    for i, child in enumerate(node.children):
                        _print_tree(child, indent + 1, is_last=(i == len(node.children) - 1), parent_prefix=parent_prefix + next_prefix)
        
        _print_tree(data)
