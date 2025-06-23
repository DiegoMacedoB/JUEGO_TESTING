import pygame
import sys
from game.core.player import Player
from game.content.enemies import EnemyManager
from game.content.scenes import SceneManager
from game.ui.game_ui import GameUI
from game.core.combat import CombatSystem

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Life in Adventure")
    clock = pygame.time.Clock()
    
    # Inicializar sistemas
    player = Player()
    enemies = EnemyManager()
    scenes = SceneManager(player, enemies, None)
    ui = GameUI(screen, player)
    
    current_scene = scenes.get_scene("start")
    in_combat = False
    combat_system = None
    
    running = True
    while running and player.health > 0 and player.sanity > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_combat:
                    # Manejar combate
                    result = ui.handle_combat_click(event.pos, combat_system)
                    
                    if result == "reroll":
                        # Actualizar UI con nueva tirada
                        pass
                    elif result:  # Resultado del combate
                        # Aplicar consecuencias al jugador
                        player.health -= result["damage_taken"]
                        player.sanity -= result["sanity_loss"]
                        player.gold += result["gold_gained"]
                        player.add_exp(result["exp_gained"])
                        
                        # Transición a escena de resultado
                        if result["result"] == "win":
                            current_scene = scenes.get_scene(f"{current_scene.id}_win")
                        else:
                            current_scene = scenes.get_scene(f"{current_scene.id}_lose")
                        
                        in_combat = False
                else:
                    # Manejar escenas normales
                    if current_scene.enemy_id:
                        # Iniciar combate
                        enemy = enemies.get_enemy(current_scene.enemy_id)
                        combat_system = CombatSystem(player)
                        combat_system.start_combat(enemy)
                        in_combat = True
                    else:
                        # Manejar decisiones normales
                        next_scene_id = ui.handle_click(event.pos, current_scene)
                        if next_scene_id:
                            current_scene = scenes.get_scene(next_scene_id)
        
        # Dibujar
        if in_combat:
            ui.draw_combat(combat_system)
        else:
            ui.draw(current_scene)
        
        pygame.display.flip()
        clock.tick(30)
    
    # Pantalla de fin de juego
    if player.health <= 0:
        game_over_text = "¡Has perdido toda tu salud! Juego terminado."
    elif player.sanity <= 0:
        game_over_text = "¡Has perdido tu cordura! Juego terminado."
    else:
        game_over_text = "¡Juego terminado!"
    
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Arial', 48)
    text_surf = font.render(game_over_text, True, (255, 0, 0))
    text_rect = text_surf.get_rect(center=(600, 400))
    screen.blit(text_surf, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()