import importlib
from icon_family.icon import IconFamilyManager

class StyleFactory:
    def create_style(self, style_name):
        # 动态导入样式模块
        style_module = importlib.import_module(f"style.{style_name.replace('.py', '')}")
        # 获取样式类
        style_class = getattr(style_module, style_name.split('_')[0].capitalize() + 'Style')
        # 返回样式实例
        return style_class()

class IconFamilyFactory:
    def __init__(self):
        self.manager = IconFamilyManager()

    def create_icon_family(self, icon_family_name, icons):
        self.manager.add_icon_family(icon_family_name, icons['icon_container'], icons['icon_leaf'])

    def get_icon_family(self, icon_family_name):
        return self.manager.get_icon_family(icon_family_name)

    def load_icon_families(self, icon_families_config):
        for name, icons in icon_families_config.items():
            self.create_icon_family(name, icons)

class ExplorerFactory:
    def __init__(self):
        self.style_factory = StyleFactory()
        self.icon_family_factory = IconFamilyFactory()
    
    def create_style(self, style_name):
        return self.style_factory.create_style(style_name)
    
    def load_icon_families(self, icon_families_config):
        self.icon_family_factory.load_icon_families(icon_families_config)
    
    def get_icon_family(self, icon_family_name):
        return self.icon_family_factory.get_icon_family(icon_family_name)
