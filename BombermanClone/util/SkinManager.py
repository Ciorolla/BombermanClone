import os


class SkinManager:
    @staticmethod
    def getAvailableBomberSkins():
        skin_names = []

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        sprites_path = os.path.join(parent_dir, 'resources', 'sprites')

        for filename in os.listdir(sprites_path):
            if filename.startswith('bomber') and filename.endswith('.png'):
                skin_name = os.path.splitext(filename)[0]
                skin_names.append(skin_name)
        return skin_names


    @staticmethod
    def getAvailableBombSkins():
        skin_names = []

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        sprites_path = os.path.join(parent_dir, 'resources', 'sprites')

        for filename in os.listdir(sprites_path):
            if filename.startswith('bomb') and filename.endswith('.png') and not filename.startswith('bomber'):
                skin_name = os.path.splitext(filename)[0]
                skin_names.append(skin_name)
        return skin_names


