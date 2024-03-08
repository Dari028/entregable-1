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
        self.__id = 0
        self.__forma = ""
        self.__sistema_fijacion = ""
        self.__material = ""
        self.__cantidad = 0

    # Metodos para ver y asignar atributos
    def ver_id(self):
        return self.__id

    def asignar_id(self, _id):
        self.__id = _id

    def ver_forma(self):
        return self.__forma

    def asignar_forma(self, forma):
        self.__forma = forma

    def ver_sistema_de_fijacion(self):
        return self.__sistema_fijacion

    def asignar_sistema_de_fijacion(self, sistema_fijacion):
        self.__sistema_fijacion = sistema_fijacion

    def ver_material(self):
        return self.__material

    def asignar_material(self, material):
        self.__material = material

    def ver_cantidad(self):
        return self.__cantidad

class protesis_cadera:
    def __init__(self):
        self.__id = 0
        self.__material = ""
        self.__sistema_fijacion = ""
        self.__tamaño = 0
        self.__cantidad = 0

    def ver_id(self):
        return self.__id

    def asignar_id(self, id):
        self.__id = id

    def ver_material(self):
        return self.__material

    def asignar_material(self, material):
        self.__material = material

    def ver_sistema_fijacion(self):
        return self.__sistema_fijacion

    def asignar_sistema_fijacion(self, sistema_fijacion):
        self.sistema_fijacion = sistema_fijacion

    def ver_tamaño(self):
        return self.__tamaño

    def asignar_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def ver_cantidad(self):
        return self.__cantidad

    def asignar_cantidad(self, cantidad):
        self.__cantidad = cantidad
class MarcapasosCardiacos:  
    def __init__(self):
        self.__id = 0
        self.__electrodos = 0
        self.__tipo_conexion = ""
        self.__frecuencia_estimulacion = 0
        self.__cantidad = 0

    def ver_id(self):
        return self.__id

    def asignar_id(self, id):
        self.__id = id

    def ver_electrodos(self):
        return self.__electrodos

    def asignar_electrodos(self, electrodos):
        self.__electrodos = electrodos

    def ver_tipo_conexion(self):
        return self.__tipo_conexion

    def asignar_tipo_conexion(self, tipo_conexion):
        self.__tipo_conexion = tipo_conexion

    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion

    def asignar_frecuencia_estimulacion(self, frecuencia_estimulacion):
        self.__frecuencia_estimulacion = frecuencia_estimulacion

    def ver_cantidad(self):
        return self.__cantidad

    def asignar_cantidad(self, cantidad):
        self.__cantidad = cantidad
class StentsCoronarios:
    def __init__(self):
        self.__id = 0
        self.__longitud = 0
        self.__diametro = 0
        self.__material = ""
        self.__cantidad = 0

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_longitud(self):
        return self.__longitud

    def set_longitud(self, longitud):
        self.__longitud = longitud

    def get_diametro(self):
        return self.__diametro

    def set_diametro(self, diametro):
        self.__diametro = diametro

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad