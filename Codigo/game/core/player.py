class Player:
    def __init__(self):
        self.health = 5
        self.sanity = 5
        self.strength = 3
        self.agility = 3
        self.intelligence = 3
        self.armor = 0
        self.damage = 0
        self.gold = 50  
        self.exp = 0
        self.level = 1
        self.equipment = {
            "head": None,
            "body": None,
            "weapon": None,
            "companion": None,
            "accessory": None
        }
        self.inventory = []
    
    def get_stat(self, stat_name):
        stats = {
            "strength": self.strength,
            "agility": self.agility,
            "intelligence": self.intelligence
        }
        base_stat = stats.get(stat_name, 0)
        
        # Añadir bonificaciones del equipo
        for slot, item in self.equipment.items():
            if item and stat_name in item.stat_bonuses:
                base_stat += item.stat_bonuses[stat_name]
        
        return base_stat
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def equip_item(self, item):
        if item.type in self.equipment:
            # Si ya hay un item equipado, lo devolvemos al inventario
            if self.equipment[item.type]:
                self.inventory.append(self.equipment[item.type])
            
            self.equipment[item.type] = item
            
            if "armor" in item:
                self.armor += item.armor
            if "damage" in item:
                self.damage += item.damage
            
            if item in self.inventory:
                self.inventory.remove(item)
            return True
        return False
    
    def use_consumable(self, item):
        if item.type == "consumable":
            self.health = min(5, self.health + item.health_restore)
            self.sanity = min(5, self.sanity + item.sanity_restore)
            self.inventory.remove(item)
            return True
        return False
    
    def buy_item(self, item):
        if self.gold >= item.price:
            self.gold -= item.price
            self.add_item(item)
            return True
        return False
    
    def add_exp(self, amount):
        self.exp += amount
        if self.exp >= 10:
            self.level += 1
            self.exp = 0
            self.health = min(5, self.health + 1)
            self.sanity = min(5, self.sanity + 1)
            print(f" wazaaa Subiste al nivel {self.level}! Salud y cordura mejoradas.")
