from .explorer import FunnyJsonExplorer

class ExplorerBuilder:
    def __init__(self, factory):
        self.factory = factory
    
    def build(self, style_name, icon_family_name):
        # 使用工厂创建样式对象
        style = self.factory.create_style(style_name)
        
        # 使用工厂获取图标族对象
        icon_family = self.factory.get_icon_family(icon_family_name)
        
        # 如果未找到指定的图标族，则抛出异常
        if not icon_family:
            raise ValueError(f"Icon family '{icon_family_name}' not found.")
        
        # 返回一个新的 FunnyJsonExplorer 实例，使用创建的样式和图标族
        return FunnyJsonExplorer(style, icon_family)
