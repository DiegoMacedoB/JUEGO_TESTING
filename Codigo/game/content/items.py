class Item:
    def __init__(self, name, type_, price, armor=0, damage=0, health_restore=0, sanity_restore=0, stat_bonuses=None):
        self.name = name
        self.type = type_  # "weapon", "head", "body", "consumable", etc.
        self.price = price
        self.armor = armor
        self.damage = damage
        self.health_restore = health_restore
        self.sanity_restore = sanity_restore
        self.stat_bonuses = stat_bonuses or {}

class ItemManager:
    def __init__(self):
        self.items = [
            Item("Espada Oxidada", "weapon", price=10, damage=1),
            Item("Armadura Ligera", "body", price=15, armor=1),
            Item("Poción Curativa", "consumable", price=8, health_restore=2),
            Item("Amuleto de Cordura", "accessory", price=12, sanity_restore=1),
        ]

    def get_shop_items(self):
        return self.items
