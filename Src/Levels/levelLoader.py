import pygame 

class Level():
    def __init__(self, data, map)->None:
        self.waypoints_ = []
        self.data_level_ = data
        self.map_ = map
        self.tilemap_ = []
        self.waves = []

    def ProcessData(self)->None:
        for layer in self.data_level_["layers"]:
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoint_data_x_ = obj["x"]
                    waypoint_data_y_ = obj["y"] 
                    self.waypoints_.append((waypoint_data_x_, waypoint_data_y_))
            elif layer["name"] == "Plano de fundo":
                self.tilemap_ = layer["data"]

    def loadWaves(self, filename: str)->list:
        with open(filename, 'r') as file:
            current_wave = []
            for line in file:
                line = line.strip()
                if line.startswith('Wave'):
                    if current_wave:
                        self.waves.append(current_wave)
                        current_wave = []
                else:
                    parts = line.split(',')
                    if len(parts) == 3:
                        count = int(parts[0].strip())
                        enemy_type = parts[1].strip()
                        delay = float(parts[2].strip())
                        current_wave.append((count, enemy_type, delay))
            if current_wave:
                self.waves.append(current_wave)

        return self.waves         

    def draw(self, surface: pygame.Surface)->None:
        surface.blit(self.map_, (0, 0))