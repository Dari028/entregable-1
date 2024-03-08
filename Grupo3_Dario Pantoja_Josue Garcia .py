class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__sexo = ""

    # Método para ver el nombre
    def ver_nombre(self):
        return self.__nombre

    # Método para ver la cedula
    def ver_cedula(self):
        return self.__cedula

    # Método para asignar la cedula
    def asignar_cedula(self, cedula):
        self.__cedula = cedula
        
    # Método para asignar el nombre
    def asignar_nombre(self, nombre):
        self.__nombre = nombre
    def ver_sexo(self):
        return self.__sexo

    # Método para asignar el sexo
    def asignar_sexo(self, sexo):
            self.__sexo = sexo
            
class ImplantesDentales:
    def __init__(self):
        self._id = 0
        self.forma = ""
        self.sistema_fijacion = ""
        self.material = ""
        self.cantidad = 0

    # Metodos para ver y asignar atributos
    def ver_id(self):
        return self._id

    def asignar_id(self, _id):
        self.id = _id

    def ver_forma(self):
        return self.forma

    def asignar_forma(self, forma):
        self.forma = forma

    def ver_sistema_de_fijacion(self):
        return self.sistema_fijacion

    def asignar_sistema_de_fijacion(self, sistema_fijacion):
        self.sistema_de_fijacion = sistema_fijacion

    def ver_material(self):
        return self.material

    def asignar_material(self, material):
        self.material = material

    def ver_cantidad(self):
        return self.cantidad

class protesis_cadera:
    def __init__(self,):
        self.id = 0
        self.material = ""
        self.sistema_fijacion = ""
        self.tamaño = 0
        self.cantidad = 0

    def ver_id(self):
        return self.id

    def asignar_id(self, id):
        self.id = id

    def ver_material(self):
        return self.material

    def asignar_material(self, material):
        self.material = material

    def ver_sistema_de_fijacion(self):
        return self.sistema_fijacion

    def asignar_sistema_de_fijacion(self, sistema_fijacion):
        self.sistema_de_fijacion = sistema_fijacion

    def ver_tamaño(self):
        return self.tamaño

    def asignar_tamaño(self, tamaño):
        self.tamaño = tamaño

    def ver_cantidad(self):
        return self.cantidad

    def asignar_cantidad(self, cantidad):
        self.cantidad = cantidad
