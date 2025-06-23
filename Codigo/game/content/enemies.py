class Enemy:
    def __init__(self, enemy_id, name, image, strength, agility, intelligence, damage, armor, gold_reward):
        self.id = enemy_id
        self.name = name
        self.image = image  # Asegurar que este atributo existe
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.damage = damage
        self.armor = armor
        self.gold_reward = gold_reward
class EnemyManager:
    def __init__(self):
        self.enemies = {}
        self.load_enemies()
    
    def load_enemies(self):
        self.add_enemy("babosa", "Babosa Gigante", "babosa.png", 
                    strength=2, agility=1, intelligence=0, 
                    damage=3, armor=0, gold_reward=8)
        
        self.add_enemy("rey_goblin", "Rey Goblin", "rey_goblin.png", 
                    strength=5, agility=3, intelligence=2, 
                    damage=6, armor=2, gold_reward=20)
        
        self.add_enemy("berserker", "Berserker", "berserker.png", 
                    strength=7, agility=4, intelligence=1, 
                    damage=8, armor=1, gold_reward=15)
        
        self.add_enemy("arquero", "Arquero Goblin", "arquero.png", 
                    strength=3, agility=5, intelligence=2, 
                    damage=4, armor=0, gold_reward=10)
        
        self.add_enemy("mago", "Mago Renegado", "mago.png", 
                    strength=1, agility=2, intelligence=8, 
                    damage=5, armor=0, gold_reward=25)
    
    def add_enemy(self, enemy_id, name, image, **kwargs):
        self.enemies[enemy_id] = Enemy(enemy_id, name, image, **kwargs)
    
    def get_enemy(self, enemy_id):
        return self.enemies.get(enemy_id)