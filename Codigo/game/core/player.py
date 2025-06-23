class Player:
    def __init__(self):
        self.health = 5
        self.sanity = 5
        self.strength = 3
        self.agility = 3
        self.intelligence = 3
        self.armor = 0
        self.damage = 0
        self.gold = 0
        self.exp = 0
        self.level = 1
        self.equipment = {
            "head": None,
            "body": None,
            "weapon": None,
            "companion": None
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
    
    def add_exp(self, amount):
        self.exp += amount
        required_exp = 5 + (self.level - 1) * 5
        if self.exp >= required_exp:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.exp = 0
        # En un juego real, aquí se mostraría una interfaz para elegir qué stat mejorar
        self.strength += 1
        self.agility += 1
        self.intelligence += 1
    
    def take_damage(self, amount, is_mental=False):
        if is_mental:
            self.sanity = max(0, self.sanity - amount)
            return self.sanity <= 0
        else:
            self.health = max(0, self.health - amount)
            return self.health <= 0
    
    def restore(self, health=0, sanity=0):
        self.health = min(5, self.health + health)
        self.sanity = min(5, self.sanity + sanity)
    
    
    def equip_item(self, item):
        if item.type in self.equipment:
            # Si ya hay un item equipado, lo devolvemos al inventario
            if self.equipment[item.type]:
                self.inventory.append(self.equipment[item.type])
            
            # Equipar el nuevo item
            self.equipment[item.type] = item
            
            # Aplicar bonificaciones
            if "armor" in item:
                self.armor += item.armor
            if "damage" in item:
                self.damage += item.damage
            
            # Remover el item del inventario
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