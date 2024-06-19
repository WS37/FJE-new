from icon_family_strategies.IconFamilyStrategy import IconFamilyStrategy

class Card(IconFamilyStrategy):
    def Container(self):
        return "♦"  # 方块
    
    def Leaf(self):
        return "♠"  # 黑桃