import random

class CombatSystem:
    def __init__(self, player):
        self.player = player
        self.rerolls_remaining = 2  # Dos rerolles disponibles
        self.current_roll = None
        self.enemy = None
    
    def start_combat(self, enemy):
        """Inicia un nuevo combate con un enemigo"""
        self.enemy = enemy
        self.rerolls_remaining = 2
        self.current_roll = self.roll_dice()
        return self.current_roll
    
    def roll_dice(self):
        """Realiza una tirada de dado (0-20)"""
        return random.randint(0, 20)
    
    def reroll(self):
        """Realiza un rerolleo si quedan disponibles"""
        if self.rerolls_remaining > 0:
            self.current_roll = self.roll_dice()
            self.rerolls_remaining -= 1
            return self.current_roll
        return None
    
    def resolve_combat(self):
        """Resuelve el combate con el valor actual del dado"""
        if self.enemy is None:
            return None
        
        # Calcular diferencia de stats
        player_stats = (self.player.strength + self.player.agility + self.player.intelligence)
        enemy_stats = (self.enemy.strength + self.enemy.agility + self.enemy.intelligence)
        stat_diff = player_stats - enemy_stats
        
        # Calcular probabilidad de éxito
        base_chance = 50
        dice_mod = (self.current_roll - 10) * 2  # +2% por punto arriba de 10
        stat_mod = stat_diff * 5  # +5% por punto de diferencia
        success_chance = max(5, min(95, base_chance + dice_mod + stat_mod))
        
        # Determinar resultado
        roll = random.randint(1, 100)
        if roll <= success_chance:
            # Victoria
            if self.current_roll >= 15:  # Victoria decisiva
                damage_taken = 0
                sanity_loss = 0
            else:  # Victoria normal
                damage_taken = max(0, self.enemy.damage - self.player.armor) // 2
                sanity_loss = random.randint(0, 1)
            
            return {
                "result": "win",
                "damage_taken": damage_taken,
                "sanity_loss": sanity_loss,
                "gold_gained": self.enemy.gold_reward,
                "exp_gained": 3
            }
        else:
            # Derrota
            if self.current_roll <= 5:  # Derrota catastrófica
                damage_taken = max(1, self.enemy.damage - self.player.armor)
                sanity_loss = 2
            else:  # Derrota normal
                damage_taken = max(1, self.enemy.damage - self.player.armor)
                sanity_loss = 1
            
            return {
                "result": "lose",
                "damage_taken": damage_taken,
                "sanity_loss": sanity_loss,
                "gold_gained": 0,
                "exp_gained": 1
            }