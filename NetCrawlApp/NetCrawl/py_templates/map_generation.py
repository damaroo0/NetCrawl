# map_generation.py

import json
import random

class MapData():
    def __init__(self, generation_data_file, map_elements_file):
        self.generation_data = self.load_json(generation_data_file)
        self.map_elements_data = self.load_json(map_elements_file)
    

    def load_json(self, file_path):
        with open(file_path, "r") as json_file:
            return json.load(json_file)


# Map generation using the BSP algorithm
class BSPGeneration:
    def __init__(self, selected_level):
        self.selected_level = selected_level


    def generate_map(self, selected_level):
        # Ваш код для генерации карты на основе выбранного уровня сложности
        print(f"Selected level: {selected_level}")

        # Получаем данные для выбранного уровня сложности
        level_data = self.difficulty_data.get(str(selected_level), {})
        if not level_data:
            print(f"Level {selected_level} data not found.")
            return

