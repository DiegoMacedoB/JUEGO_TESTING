import random

class Item:
    def __init__(self, item_id, name, item_type, image, price, 
                 armor=0, damage=0, stat_bonuses=None, 
                 health_restore=0, sanity_restore=0):
        self.id = item_id
        self.name = name
        self.type = item_type
        self.image = image
        self.price = price
        self.armor = armor
        self.damage = damage
        self.stat_bonuses = stat_bonuses or {}
        self.health_restore = health_restore
        self.sanity_restore = sanity_restore
        self.consumable = (item_type == "consumable")

class ItemManager:
    def __init__(self):
        self.items = {}
        self.load_items()
    
    def load_items(self):
        # Armaduras
        self.add_item("leather_armor", "Armadura de Cuero", "body", "leather_armor.png", 30, armor=2)
        self.add_item("chainmail", "Cota de Malla", "body", "chainmail.png", 60, armor=4)
        
        # Armas
        self.add_item("iron_sword", "Espada de Hierro", "weapon", "iron_sword.png", 40, damage=3)
        self.add_item("steel_sword", "Espada de Acero", "weapon", "steel_sword.png", 80, damage=5)
        
        # Accesorios
        self.add_item("strength_ring", "Anillo de Fuerza", "accessory", "strength_ring.png", 50, 
                     stat_bonuses={"strength": 2})
        self.add_item("agility_boots", "Botas de Agilidad", "accessory", "agility_boots.png", 45, 
                     stat_bonuses={"agility": 2})
        
        # Compañeros
        self.add_item("tapioca", "Tapioca", "companion", "tapioca.png", 100, 
                     stat_bonuses={"intelligence": 1})
        self.add_item("layla", "Layla", "companion", "layla.png", 150, 
                     stat_bonuses={"agility": 2})
        
        # Consumibles
        self.add_item("health_potion", "Poción de Salud", "consumable", "health_potion.png", 15, 
                     health_restore=2)
        self.add_item("sanity_potion", "Poción de Cordura", "consumable", "sanity_potion.png", 20, 
                     sanity_restore=2)
        self.add_item("full_restore", "Elixir Completo", "consumable", "elixir.png", 30, 
                     health_restore=3, sanity_restore=3)
    
    def add_item(self, item_id, name, item_type, image, price, **kwargs):
        self.items[item_id] = Item(item_id, name, item_type, image, price, **kwargs)
    
    def get_item(self, item_id):
        return self.items.get(item_id)
    
    def generate_shop_items(self, num_items=6):
        """Genera una lista aleatoria de items para la tienda"""
        # Excluir compañeros para la tienda
        available_items = [item for item in self.items.values() if item.type != "companion"]
        return random.sample(available_items, min(num_items, len(available_items)))