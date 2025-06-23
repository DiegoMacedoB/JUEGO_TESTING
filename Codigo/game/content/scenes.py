import random

class Scene:
    def __init__(self, scene_id, description, image, choices=None, enemy_id=None, shop=False):
        self.id = scene_id
        self.description = description
        self.image = image
        self.choices = choices or []
        self.enemy_id = enemy_id
        self.shop = shop

class SceneManager:
    def __init__(self, player, enemies, items):
        self.player = player
        self.enemies = enemies
        self.items = items
        self.scenes = {}
        self.load_scenes()
    
    def load_scenes(self):
        # Escena inicial
        self.add_scene("start", 
                      "Te despiertas en un bosque oscuro. A lo lejos ves una cabaña y un camino al pueblo.",
                      "bosque.png",
                      choices=[
                          {"text": "Ir a la cabaña", "next_scene": "cabin", "required_stat": "strength"},
                          {"text": "Ir al pueblo", "next_scene": "village"}
                      ])
        
        # Escena de cabaña
        self.add_scene("cabin",
                      "Una babosa gigante bloquea la entrada a la cabaña.",
                      "cabania.png",
                      enemy_id="babosa")
        
        self.add_scene("cabin_win",
                      "¡Derrotaste a la babosa! Dentro encuentras provisiones.",
                      "cabania.png",
                      choices=[{"text": "Tomar provisiones", "next_scene": "start"}])
        
        self.add_scene("cabin_lose",
                      "La babosa te derrota. Escapas herido.",
                      "cabania.png",
                      choices=[{"text": "Regresar al bosque", "next_scene": "start"}])
        
        # Escena de pueblo
        self.add_scene("village",
                      "Llegas a un pueblo. Hay una tienda y las cloacas.",
                      "tienda.png",
                      choices=[
                          {"text": "Entrar a la tienda", "next_scene": "shop"},
                          {"text": "Bajar a las cloacas", "next_scene": "sewers"}
                      ])
        
        # Escena de cloacas
        self.add_scene("sewers",
                      "El Rey Goblin y sus secuaces te rodean.",
                      "cloacas.png",
                      enemy_id="rey_goblin")
        
        self.add_scene("sewers_win",
                      "¡Derrotaste al Rey Goblin! Encuentras un tesoro.",
                      "cloacas.png",
                      choices=[{"text": "Tomar el tesoro", "next_scene": "village"}])
        
        self.add_scene("sewers_lose",
                      "El Rey Goblin te derrota. Escapas por poco.",
                      "cloacas.png",
                      choices=[{"text": "Regresar al pueblo", "next_scene": "village"}])
        
        # Escena de tienda
        self.add_scene("shop",
                      "Bienvenido a la tienda. ¿Qué deseas comprar?",
                      "tienda.png",
                      shop=True,
                      choices=[{"text": "Salir", "next_scene": "village"}])
    
    def add_scene(self, scene_id, description, image, choices=None, enemy_id=None, shop=False):
        self.scenes[scene_id] = Scene(scene_id, description, image, choices, enemy_id, shop)
    
    def get_scene(self, scene_id):
        scene = self.scenes.get(scene_id)
        if not scene:
            print(f"Error: Escena '{scene_id}' no encontrada! Volviendo al inicio.")
            return self.scenes["start"]  # Retorna objeto Scene, no string
        return scene
    
    def handle_choice(self, choice):
        if "required_stat" in choice:
            stat_value = self.player.get_stat(choice["required_stat"])
            return random.randint(1, 100) <= (40 + stat_value * 5)
        return True