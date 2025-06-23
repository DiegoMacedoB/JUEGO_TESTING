class InventorySystem:
    def __init__(self, player):
        self.player = player
    
    def equip_item(self, item):
        if item.item_type in self.player.equipment:
            # Remover bonificaciones del item actual si existe
            current_item = self.player.equipment[item.item_type]
            if current_item:
                self.player.armor -= current_item.armor
                self.player.damage -= current_item.damage
                for stat, bonus in current_item.stat_bonuses.items():
                    if stat == "strength":
                        self.player.strength -= bonus
                    elif stat == "agility":
                        self.player.agility -= bonus
                    elif stat == "intelligence":
                        self.player.intelligence -= bonus
            
            # Equipar nuevo item
            self.player.equipment[item.item_type] = item
            self.player.armor += item.armor
            self.player.damage += item.damage
            for stat, bonus in item.stat_bonuses.items():
                if stat == "strength":
                    self.player.strength += bonus
                elif stat == "agility":
                    self.player.agility += bonus
                elif stat == "intelligence":
                    self.player.intelligence += bonus
    
    def use_consumable(self, item):
        if item.consumable:
            self.player.restore(
                health=item.health_restore,
                sanity=item.sanity_restore
            )
            self.player.inventory.remove(item)
            return True
        return False
    
    def add_item(self, item):
        self.player.inventory.append(item)
    
    def remove_item(self, item):
        if item in self.player.inventory:
            self.player.inventory.remove(item)
            return True
        return False