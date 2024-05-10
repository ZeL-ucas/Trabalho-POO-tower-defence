import pygame 
class Level():
    def __init__(self, data, map):
        self.waypoints_ = []
        self.data_level_ = data
        self.map_ = map
    def ProcessData(self):
        for layer in self.data_level_["layers"]:
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoint_data_x_ = obj["x"]
                    waypoint_data_y_ = obj["y"]
                    # print((waypoint_data_x_), (waypoint_data_y_))
                    self.waypoints_.append((waypoint_data_x_, waypoint_data_y_))
    def draw(self, surface):
        surface.blit(self.map_, (0, 0))