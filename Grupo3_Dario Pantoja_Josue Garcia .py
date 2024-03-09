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
class ProtesisDeRodillas:
    def __init__(self):
        self.__id = 0
        self.__material = ""
        self.__tipo_fijacion = ""
        self.__tamaño = 0
        self.__cantidad = 0

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_tipo_fijacion(self):
        return self.__tipo_fijacion

    def set_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
class Paciente(Persona):
    def __init__(self,  implante=None ):
        super().__init__()
        self.__nombre = ""
        self.__cedula = 0
        self.__sexo = ""
        self.__implantes = self._get_implantes(implante)
        self.__fecha_revision = ""
        self.__fecha_mantenimiento = ""

    def _get_implantes(self, implante):
        implante=implante
        if implante is None:
            return None
        elif implante == 1:
            return protesis_cadera()
        elif implante == 2:
            return MarcapasosCardiacos()
        elif implante == 3:
            return StentsCoronarios()
        elif implante == 4:
            return ProtesisDeRodillas()

    def ver_nombre(self):
        return self.__nombre

    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def ver_cedula(self):
        return self.__cedula

    def asignar_cedula(self, cedula):
        self.__cedula = cedula

    def ver_sexo(self):
        return self.__sexo

    def asignar_sexo(self, sexo):
        self.__sexo = sexo

    def ver_implantes(self):
        if self.__implantes is None:
            print("No implants")
        else:
            print(self.__implantes)

    def asignar_implantes(self, implante):
        self.__implantes = self._get_implantes(implante)

    def ver_fecha_revision(self):
        return self.__fecha_revision

    def asignar_fecha_revision(self, fecha_revision):
        self.__fecha_revision = fecha_revision

    def ver_fecha_mantenimiento(self):
        return self.__fecha_mantenimiento

    def asignar_fecha_mantenimiento(self, fecha_mantenimiento):
        self.__fecha_mantenimiento = fecha_mantenimiento
class Medico(Persona):
    def __init__(self, nombre="", cedula=0, sexo="", especialidad=""):
        super().__init__(nombre, cedula, sexo)
        self.__especialidad = especialidad

    def ver_nombre(self):
        return self.__nombre

    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def ver_cedula(self):
        return self.__cedula

    def asignar_cedula(self, cedula):
        self.__cedula = cedula

    def ver_sexo(self):
        return self.__sexo

    def asignar_sexo(self, sexo):
        self.__sexo = sexo

    def ver_especialidad(self):
        return self.__especialidad

    def asignar_especialidad(self, especialidad):
        self.__especialidad = especialidad

class Sistema:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__implantes = {}

    def ver_pacientes(self):
        return self.__pacientes

    def agregar_paciente(self, paciente):
        if paciente.ver_cedula() in self.__pacientes:
            print(f"Ya existe un paciente con cedula {paciente.ver_cedula()}")
        else:
            self.__pacientes[paciente.ver_cedula()] = paciente

    def eliminar_paciente(self, cedula):
        if cedula in self.__pacientes:
            del self.__pacientes[cedula]
        else:
            print(f"No existe un paciente con cedula {cedula}")

    def ver_medicos(self):
        return self.__medicos

    def agregar_medico(self, medico):
        if medico.ver_cedula() in self.__medicos:
            print(f"Ya existe un medico con cedula {medico.ver_cedula()}")
        else:
            self.__medicos[medico.ver_cedula()] = medico

    def eliminar_medico(self, cedula):
        if cedula in self.__medicos:
            del self.__medicos[cedula]
        else:
            print(f"No existe un medico con cedula {cedula}")
    def ver_implantes(self):
        return self.__implantes

    def agregar_implante(self, implante):
        if implante.ver_id() in self.__implantes:
            print(f"Ya existe un implante con id {implante.ver_id()}")
        else:
            self.__implantes[implante.ver_id()] = implante

    def eliminar_implante(self, id):
        if id in self.__implantes:
            del self.__implantes[id]
        else:
            print(f"No existe un implante con el id {id}")

    def verDatosPacienteC(self, c): #definimos la forma en la que veremos los datos ya sea con cedula 
        if c in self.__pacientes:
            for i in self.__pacientes[c]:
                print(i[c])


def main():
    Sistem = Sistema()
    while True:
        menu = input("""
                    1. Registro de paciente
                    2. Buscar paciente
                    3. Cambiar implantes 
                    4. eliminar paciente
                    4. Salir
                     """)
        
        if menu == "1":
            N = input("Nombre del paciente: ")
            C = input("Cedula del paciente: ")
            S = input("Ingresar genero del paciente: ")
            I = int(input("""Implante:
                    1. Protesis Cadera
                    2. Marcapasos Cardiacos
                    3. Stents Coronarios
                    4. Protesis De Rodillas
                          """))
            if I == 1:
                a = input("Id: ")
                b = input("Material: ")
                c = input("Sistema de fijacion: ")
                d = input("Tamaño: ")
                ID = protesis_cadera.asignar_id(a)
                MA = protesis_cadera.asignar_material(b)
                SF = protesis_cadera.asignar_sistema_fijacion(c)
                T = protesis_cadera.asignar_tamaño(d)

            elif I == 2:
                a = input("Id: ")
                b = input("Electrodos: ")
                c = input("Frecuencia de estimulacion: ")
                d = input("Tipo de conexion: ")
                MarcapasosCardiacos.asignar_id()
                MarcapasosCardiacos.asignar_electrodos()
                MarcapasosCardiacos.asignar_frecuencia_estimulacion()
                MarcapasosCardiacos.asignar_tipo_conexion()
            elif I == 3:
                a = input("Id: ")
                b = input("Forma: ")
                c = input("Material: ")
                d = input("Sistema de fijacion: ")
                ID = ImplantesDentales.asignar_id(a)
                FO = ImplantesDentales.asignar_forma(b)
                MA = ImplantesDentales.asignar_material(c)
                SF = ImplantesDentales.asignar_sistema_de_fijacion(d)
            elif I == 4:
                pass


            FR = input("Fecha de revision: ")
            FM = input("Fecha de mantenimiento: ")

            Implante = []
            Implante.append(I)
            pac = Paciente()
            pac.asignar_nombre(N)
            pac.asignar_cedula(C)
            pac.asignar_sexo(S)
            pac.asignar_implantes(Implante)
            pac.asignar_fecha_revision(FR)
            pac.asignar_fecha_mantenimiento(FM)
            Sistem.agregar_paciente(pac)
            

        elif menu == "2":
            C = int(input("Cedula: "))
            P = Sistem.verDatosPacienteC(C)
            print(P[C])            

        elif menu == "3":
            pass
        elif menu == "4":
            break

        else:
            print("No es opcion")

if __name__=='__main__':
    main()