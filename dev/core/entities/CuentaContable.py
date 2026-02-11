import hashlib

class CuentaContable:
    def __init__(self, name: str, type: str, special: bool, id=None):
        self.name = name
        self.type = type
        self.special = special
        if id is None:
            self.id = self.calculate_id(name)
        else:
            self.id = id

    @staticmethod
    def calculate_id(name: str):
        encoded_name = name.encode('utf-8')
        hash_object = hashlib.sha256(encoded_name)
        return hash_object.hexdigest()

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_special(self):
        return self.special

    # Setters
    def set_name(self, name: str):
        self.name = name

    def set_type(self, type: str):
        self.type = type

    def set_special(self, special: bool):
        self.special = special

    # Output
    def __str__(self):
        return f"Nombre: {self.name} Tipo: {self.type} Especial: {self.special} ID: {self.id}"

    # Other functions
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "special": self.special,
            "id": self.id
        }