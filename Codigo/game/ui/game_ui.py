from pygame import Rect, draw, font
from game.content.items import ItemManager

import pygame
import os

class GameUI:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.font = pygame.font.SysFont('Arial', 28)
        self.small_font = pygame.font.SysFont('Arial', 22)
        self.item_manager = ItemManager()  
        
        self.button_color = (70, 130, 180)
        self.button_hover = (100, 149, 237)
        self.text_box_color = (0, 0, 0, 180)  
        self.text_color = (255, 255, 255)
        self.notification = ""     
        self.notification_timer = 0  


    def load_image(self, filename):
        """Carga una imagen desde la carpeta assets"""
        try:
            full_path = os.path.join("assets", filename)
            return pygame.image.load(full_path)
        except Exception as e:
            print(f"Error cargando imagen {filename}: {e}")
            surf = pygame.Surface((500, 350))
            surf.fill((50, 50, 50))
            return surf
    
    def draw(self, scene):
        """Dibuja la interfaz de la escena actual"""
        self.screen.fill((30, 30, 30))
        
        scene_image = self.load_image(scene.image)
        if scene_image:
            scene_image = pygame.transform.scale(scene_image, (700, 400))
            self.screen.blit(scene_image, (250, 20))
        
        self.draw_player_info()
        
        text_box_y = 440
        
        self.draw_text_box(scene.description, (100, text_box_y), 1000)
        
        text_height = self.calculate_text_height(scene.description, 1000)
        button_start_y = text_box_y + text_height + 30
        
        if scene.enemy_id:
            self.draw_combat_button(button_start_y)
        elif scene.shop:
            self.draw_shop()
        else:
            self.draw_choices(scene.choices, button_start_y)

        
        pygame.display.flip()
    
    def draw_player_info(self):
        """Dibuja la información del jugador en la esquina superior izquierda"""
        # Panel de información
        info_rect = pygame.Rect(20, 20, 200, 200)
        pygame.draw.rect(self.screen, (40, 40, 40), info_rect)
        pygame.draw.rect(self.screen, (100, 100, 100), info_rect, 2)
        
        # Barra de salud
        pygame.draw.rect(self.screen, (200, 0, 0), (30, 30, 180, 25))
        health_width = 180 * self.player.health / 5
        pygame.draw.rect(self.screen, (0, 200, 0), (30, 30, health_width, 25))
        health_text = self.small_font.render(f"Salud: {self.player.health}/5", True, (255, 255, 255))
        self.screen.blit(health_text, (35, 35))
        
        # Barra de cordura
        pygame.draw.rect(self.screen, (100, 100, 200), (30, 70, 180, 25))
        sanity_width = 180 * self.player.sanity / 5
        pygame.draw.rect(self.screen, (50, 50, 255), (30, 70, sanity_width, 25))
        sanity_text = self.small_font.render(f"Cordura: {self.player.sanity}/5", True, (255, 255, 255))
        self.screen.blit(sanity_text, (35, 75))
        
        # Stats y otros
        stats = [
            f"Fuerza: {self.player.get_stat('strength')}",
            f"Agilidad: {self.player.get_stat('agility')}",
            f"Inteligencia: {self.player.get_stat('intelligence')}",
            f"Oro: {self.player.gold}",
            f"Nivel: {self.player.level}"
        ]
        
        for i, stat in enumerate(stats):
            stat_text = self.small_font.render(stat, True, (255, 255, 255))
            self.screen.blit(stat_text, (30, 110 + i * 30))
    
    def calculate_text_height(self, text, max_width):
        """Calcula la altura necesaria para mostrar el texto"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        # Dividir texto en líneas
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = self.font.size(test_line)[0]
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        line_height = self.font.get_linesize()
        return len(lines) * line_height + 40  # 40px de padding
    
    def draw_text_box(self, text, pos, max_width):
        """Dibuja un cuadro de texto con fondo semitransparente"""
        x, y = pos
        
        # Calcular tamaño del cuadro de texto
        text_height = self.calculate_text_height(text, max_width)
        bg_rect = pygame.Rect(x - 20, y - 20, max_width + 40, text_height)
        
        # Dibujar fondo semitransparente
        pygame.draw.rect(self.screen, self.text_box_color, bg_rect)
        pygame.draw.rect(self.screen, (100, 100, 100), bg_rect, 2)
        
        # Dividir texto en líneas
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = self.font.size(test_line)[0]
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        # Renderizar cada línea
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, self.text_color)
            self.screen.blit(text_surface, (x, y + i * self.font.get_linesize()))
    
    def draw_choices(self, choices, start_y):
        """Dibuja los botones de opciones para una escena normal"""
        for i, choice in enumerate(choices):
            button_rect = pygame.Rect(300, start_y + i * 70, 600, 60)
            color = self.button_hover if button_rect.collidepoint(pygame.mouse.get_pos()) else self.button_color
            
            pygame.draw.rect(self.screen, color, button_rect, border_radius=10)
            pygame.draw.rect(self.screen, (255, 255, 255), button_rect, 2, border_radius=10)
            
            # Texto centrado
            text_width = self.font.size(choice["text"])[0]
            text_x = button_rect.x + (button_rect.width - text_width) // 2
            text_y = button_rect.y + (button_rect.height - self.font.get_height()) // 2
            self.screen.blit(self.font.render(choice["text"], True, (255, 255, 255)), (text_x, text_y))
    
    def draw_combat_button(self, start_y):
        """Dibuja el botón de combate para escenas con enemigos"""
        button_rect = pygame.Rect(450, start_y, 300, 70)
        color = self.button_hover if button_rect.collidepoint(pygame.mouse.get_pos()) else self.button_color
        
        pygame.draw.rect(self.screen, color, button_rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), button_rect, 2, border_radius=10)
        
        # Texto centrado
        text = "¡Pelear!"
        text_width = self.font.size(text)[0]
        text_x = button_rect.x + (button_rect.width - text_width) // 2
        text_y = button_rect.y + (button_rect.height - self.font.get_height()) // 2
        self.screen.blit(self.font.render(text, True, (255, 255, 255)), (text_x, text_y))
    
    def handle_click(self, pos, current_scene):
        """Maneja los clics en la interfaz"""
        # Calcular posición de los botones
        text_height = self.calculate_text_height(current_scene.description, 1000)
        button_start_y = 440 + text_height + 30
        
        # Manejar clic en botones de combate
        if current_scene.enemy_id:
            button_rect = pygame.Rect(450, button_start_y, 300, 70)
            if button_rect.collidepoint(pos):
                return "start_combat"
        
        # Manejar clic en opciones normales
        else:
            for i, choice in enumerate(current_scene.choices):
                button_rect = pygame.Rect(300, button_start_y + i * 70, 600, 60)
                if button_rect.collidepoint(pos):
                    return choice["next_scene"]
        
        return None
    
    def handle_combat_click(self, pos, combat):
        """Maneja los clics durante el combate"""
        # Botón de rerollear
        reroll_rect = pygame.Rect(300, 650, 200, 50)
        if reroll_rect.collidepoint(pos) and combat.rerolls_remaining > 0:
            combat.reroll()
            return "reroll"
        
        # Botón de aceptar
        accept_rect = pygame.Rect(550, 650, 200, 50)
        if accept_rect.collidepoint(pos):
            return combat.resolve_combat()
        
        return None
    
    def draw_combat(self, combat):
        """Dibuja la interfaz de combate con opción de rerollear"""
        # Limpiar pantalla
        self.screen.fill((30, 30, 30))
        
        # Dibujar información del jugador
        self.draw_player_info()
        
        # Dibujar imagen del enemigo
        if combat.enemy:
            enemy_image = self.load_image(combat.enemy.image)
            if enemy_image:
                # Escalar la imagen manteniendo proporción
                enemy_image = pygame.transform.scale(enemy_image, (400, 400))
                self.screen.blit(enemy_image, (400, 100))
        
        # Panel de combate
        combat_panel = pygame.Rect(200, 500, 800, 200)
        pygame.draw.rect(self.screen, (0, 0, 0, 180), combat_panel)
        pygame.draw.rect(self.screen, (100, 100, 100), combat_panel, 2)
        
        # Mostrar tirada actual
        roll_text = self.font.render(f"Tirada actual: {combat.current_roll}/20", True, (255, 255, 255))
        self.screen.blit(roll_text, (250, 520))
        
        # Mostrar rerolles disponibles
        rerolls_text = self.font.render(f"Rerolles restantes: {combat.rerolls_remaining}", True, (255, 255, 255))
        self.screen.blit(rerolls_text, (250, 560))
        
        # Dibujar botones de combate
        self.draw_combat_buttons(combat.rerolls_remaining > 0)
        
        pygame.display.flip()
    
    def draw_combat_buttons(self, can_reroll):
        """Dibuja los botones para el combate"""
        # Botón de rerollear (solo si hay rerolles disponibles)
        if can_reroll:
            reroll_rect = pygame.Rect(300, 650, 200, 50)
            pygame.draw.rect(self.screen, (70, 180, 70), reroll_rect, border_radius=10)
            pygame.draw.rect(self.screen, (255, 255, 255), reroll_rect, 2, border_radius=10)
            reroll_text = self.font.render("Rerollear", True, (255, 255, 255))
            self.screen.blit(reroll_text, (reroll_rect.x + 50, reroll_rect.y + 15))
        
        # Botón de aceptar
        accept_rect = pygame.Rect(550, 650, 200, 50)
        pygame.draw.rect(self.screen, (180, 70, 70), accept_rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), accept_rect, 2, border_radius=10)
        accept_text = self.font.render("Aceptar", True, (255, 255, 255))
        self.screen.blit(accept_text, (accept_rect.x + 60, accept_rect.y + 15))

    def draw_shop(self):
        self.screen.fill((200, 200, 250))
        self.button_rects = []
        y = 100
        for item in self.item_manager.get_shop_items():
            text = f"{item.name} - {item.price} oro"
            txt_surf = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(txt_surf, (100, y))
            btn_rect = Rect(400, y, 120, 30)
            draw.rect(self.screen, (0, 200, 0), btn_rect)
            buy_txt = self.font.render("Comprar", True, (255, 255, 255))
            self.screen.blit(buy_txt, (btn_rect.x + 10, btn_rect.y + 5))
            self.button_rects.append((btn_rect, item))
            y += 50
        if self.notification_timer > 0:
            notif_surf = self.font.render(self.notification, True, (0, 0, 0))
            notif_rect = notif_surf.get_rect(center=(600, 700))
            pygame.draw.rect(self.screen, (255, 255, 200), notif_rect.inflate(20, 10))
            self.screen.blit(notif_surf, notif_rect)
            self.notification_timer -= 1


        # Botón salir
        salir_rect = Rect(100, y + 20, 120, 30)
        draw.rect(self.screen, (150, 0, 0), salir_rect)
        salir_txt = self.font.render("Salir", True, (255, 255, 255))
        self.screen.blit(salir_txt, (salir_rect.x + 30, salir_rect.y + 5))
        self.button_rects.append((salir_rect, "salir"))

    def handle_shop_click(self, pos):
        for rect, item in self.button_rects:
            if rect.collidepoint(pos):
                if item == "salir":
                    return "village"
                if self.player.buy_item(item):
                    self.notification = f"¡Compraste {item.name}!"
                    self.notification_timer = 90  
                else:
                    self.notification = "No tienes suficiente oro"
                    self.notification_timer = 90
        return None