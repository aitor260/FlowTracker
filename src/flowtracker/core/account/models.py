import hashlib

class CuentaContable:
    def __init__(self, name: str, type: str, special: bool):
        self.name = name
        self.type = type
        self.special = special
        self.id = self.calculate_id(name)

    @staticmethod
    def calculate_id(name: str):
        encoded_name = name.encode('utf-8')
        hash_object = hashlib.sha256(encoded_name)
        return hash_object.hexdigest()

    def __str__(self):
        return f"Nombre: {self.name} Tipo: {self.type} Especial: {self.special} ID: {self.id}"

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "special": self.special,
            "id": self.id
        }