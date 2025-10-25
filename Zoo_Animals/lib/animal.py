class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name

    def make_sound(self):
        return self.sound