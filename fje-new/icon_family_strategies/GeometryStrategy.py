from icon_family_strategies.IconFamilyStrategy import IconFamilyStrategy

class Geometry(IconFamilyStrategy):
    def Container(self):
        return "◎"  # 圆形
    
    def Leaf(self):
        return "★"  # 星形
