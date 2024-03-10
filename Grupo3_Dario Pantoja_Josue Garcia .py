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
            
class ImplantesDentales: #clase de implante
    def __init__(self):
        self.__id = 0
        self.__forma = ""
        self.__sistema_fijacion = ""
        self.__material = ""

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
    
class protesis_cadera: #clase de implante
    def __init__(self):
        self.__id = 0
        self.__material = ""
        self.__sistema_fijacion = ""
        self.__tamaño = 0
    #get
        
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

class MarcapasosCardiacos:  #clase de implante
    def __init__(self):
        self.__id = 0
        self.__electrodos = 0
        self.__tipo_conexion = ""
        self.__frecuencia_estimulacion = 0

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



class StentsCoronarios: #clase de implante
    def __init__(self):
        self.__id = 0
        self.__longitud = 0
        self.__diametro = 0
        self.__material = ""

    def ver_id(self):
        return self.__id

    def asignar_id(self, id):
        self.__id = id

    def ver_longitud(self):
        return self.__longitud

    def asignar_longitud(self, longitud):
        self.__longitud = longitud

    def ver_diametro(self):
        return self.__diametro

    def asignar_diametro(self, diametro):
        self.__diametro = diametro

    def ver_material(self):
        return self.__material

    def asignar_material(self, material):
        self.__material = material

class ProtesisDeRodillas: #clase de implante
    def __init__(self):
        self.__id = 0
        self.__material = ""
        self.__tipo_fijacion = ""
        self.__tamaño = 0

    def ver_id(self):
        return self.__id

    def asignar_id(self, id):
        self.__id = id

    def ver_material(self):
        return self.__material

    def asignar_material(self, material):
        self.__material = material

    def ver_tipo_fijacion(self):
        return self.__tipo_fijacion

    def asignar_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion

    def ver_tamaño(self):
        return self.__tamaño

    def asignar_tamaño(self, tamaño):
        self.__tamaño = tamaño


class Paciente(Persona): #paciente hereda de Persona y damos las funciones
    def __init__(self,  implante=None ):
        super().__init__()
        self.__nombre = ""
        self.__cedula = 0
        self.__sexo = ""
        self.__implantes = self._get_implantes(implante)
        self.__fecha_revision = ""
        self.__fecha_mantenimiento = ""

    
    def _get_implantes(self, implante):
        

        if implante is None:
            return None
        elif self.__implantes is None or not isinstance(self.__implantes, (protesis_cadera, MarcapasosCardiacos, StentsCoronarios, ProtesisDeRodillas, ImplantesDentales)) or type(self.__implantes) != type(implante):
            if implante == 1:
                self.__implantes = protesis_cadera
            elif implante == 2:
                self.__implantes = MarcapasosCardiacos
            elif implante == 3:
                self.__implantes = StentsCoronarios()
            elif implante == 4:
                self.__implantes = ProtesisDeRodillas()
            elif implante == 5:
                self.__implantes = ImplantesDentales()
            return self.__implantes
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
        if self.__implantes:
            print("ID: ", self.__implantes.ver_id())

            if isinstance(self.__implantes, protesis_cadera()):
                print("Material: ", self.__implantes.ver_material())
                print("Sistema de fijacion: ", self.__implantes.ver_sistema_fijacion())
                print("Tamaño: ", self.__implantes.ver_tamaño())
               

            elif isinstance(self.__implantes, MarcapasosCardiacos):
                print("Electrodos: ", self.__implantes.ver_electrodos())
                print("Tipo de conexion: ", self.__implantes.ver_tipo_conexion())
                print("Frecuencia de estimulacion: ", self.__implantes.ver_frecuencia_estimulacion())
                

            elif isinstance(self.__implantes, StentsCoronarios):
                print("Longitud: ", self.__implantes.ver_longitud())
                print("Diametro: ", self.__implantes.ver_diametro())
                print("Material: ", self.__implantes.ver_material())
               

            elif isinstance(self.__implantes, ProtesisDeRodillas):
                print("Material: ", self.__implantes.ver_material())
                print("Tipo de fijacion: ", self.__implantes.ver_tipo_fijacion())
                print("Tamaño: ", self.__implantes.ver_tamaño())
               

            elif isinstance(self.__implantes, ImplantesDentales):
                print("Material: ", self.__implantes.ver_material())
                print("Tipo de fijacion: ", self.__implantes.ver_sistema_de_fijacion())
                print("Tamaño: ", self.__implantes.ver_forma())
                

        else:
            print("No hay implantes asignados")

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
        super().__init__()
        self.__especialidad = especialidad
        #variables para el medico heredando de Persona 

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

    def agregar_paciente(self, paciente):   #agregar paciente al sistema
        if paciente.ver_cedula() in self.__pacientes:
            print(f"Ya existe un paciente con cedula {paciente.ver_cedula()}")
        else:
            self.__pacientes[paciente.ver_cedula()] = paciente #se agrega al diccionario 

    def eliminar_paciente(self, cedula):    #eliminar paciente del sistema
        if cedula in self.__pacientes:
            del self.__pacientes[cedula]
        else:
            print(f"No existe un paciente con cedula {cedula}")

    def ver_medicos(self): #ver medicos en el sistema
        return self.__medicos

    def agregar_medico(self, medico):  #agregar medico al sistema
        if medico.ver_cedula() in self.__medicos:
            print(f"Ya existe un medico con cedula {medico.ver_cedula()}")
        else:
            self.__medicos[medico.ver_cedula()] = medico

    def eliminar_medico(self, cedula):  #eliminar medico del sistema
        if cedula in self.__medicos:
            del self.__medicos[cedula]
        else:
            print(f"No existe un medico con cedula {cedula}")
    def ver_implantes(self): #ver implantes 
        return self.__implantes

    def agregar_implante(self, implante):  #agregar implante al sistema
        if implante.ver_id() in self.__implantes:
            print(f"Ya existe un implante con id {implante.ver_id()}")
        else:
            self.__implantes[implante.ver_id()] = implante

    def eliminar_implante(self, id): #eliminar implante del sistema
        if id in self.__implantes:
            del self.__implantes[id]
        else:
            print(f"No existe un implante con el id {id}")

    def verDatosPacienteC(self, c): #buscar paciente en el sistema
        if c in self.__pacientes:
            return self.__pacientes[c]
        else:
            return None
        
    def buscar_paciente_ced(self, c):  #funcion para buscar cedulas en el diccionario pacientes
        encontrado = False
        if c in self.__pacientes:
            encontrado = True
        return encontrado
    
def validar_N(N): #validar numeros 
    while  N.isdigit() != True:
        print("El dato no es valido")
        N = input("Ingrese un dato valido: ")


def main():
    Sistem = Sistema()
    while True:
        menu = input("""
                    1. Registro de paciente
                    2. Buscar paciente 
                    3. Eliminar paciente
                    4. Salir
                     """)
        
        if menu == "1":
            #pedimos informacion de paciente
            N = input("Nombre del paciente: ")
            C =input("Cedula del paciente: ")
            validar_N(C) #validar numero 
            S = input("Ingresar genero del paciente: ")
            #pedimos informacion del medico 
            D = input("Nombre medico: ")
            CD = input("Cedula medico: ")
            validar_N(CD) #validar numero 
            DS = input("Genero medico: ")

            #asignamos el medico

            Med = Medico()
            Med.asignar_nombre(D)
            Med.asignar_cedula(CD)
            Med.asignar_sexo(DS)

            I = int(input("""Implante:
                    1. Protesis Cadera
                    2. Marcapasos Cardiacos
                    3. Stents Coronarios
                    4. Protesis De Rodillas
                    5. Implantes Dentales
                          """))
            pac = Paciente()
            if I == 1:
                #asignamos para guardar en implante 
                implante = protesis_cadera()
                implante.asignar_id(validar_N(input("Id: ")))
                implante.asignar_material(input("Material: "))
                implante.asignar_sistema_fijacion(input("Sistema de fijacion: "))
                implante.asignar_tamaño(validar_N(input("Tamaño: ")))
              

            elif I == 2:
                #asignamos para guardar en implante
                implante = MarcapasosCardiacos()
                implante.asignar_id(validar_N(input("Id: ")))
                implante.asignar_electrodos(validar_N(input("Electrodos: ")))
                implante.asignar_tipo_conexion(input("Tipo de conexion: "))
                implante.asignar_frecuencia_estimulacion(validar_N(input("Frecuencia de estimulacion: ")))
               

            elif I == 3:
                #asignamos para guardar en implante
                implante = StentsCoronarios()
                implante.asignar_id(validar_N(input("Id: ")))
                implante.asignar_longitud(validar_N(input("Longitud: ")))
                implante.asignar_diametro(validar_N(input("Diametro: ")))
                implante.asignar_material(input("Material: "))
               


            elif I == 4:
                #asignamos para guardar en implante
                implante = ProtesisDeRodillas()
                implante.asignar_id(validar_N(input("Id: ")))
                implante.asignar_material(input("Material: "))
                implante.asignar_tipo_fijacion(input("Tipo de fijacion: "))
                implante.asignar_tamaño(validar_N(input("Tamaño: ")))
             

            elif I == 5:
                implante = ImplantesDentales()
                implante.asignar_id(validar_N(input("Id: ")))
                implante.asignar_material(input("Material: "))
                implante.asignar_sistema_de_fijacion(input("Sistema de fijacion: "))
                implante.asignar_forma(input("Forma: "))
            
           
            FR = input("Fecha de revision: ")
            FM = input("Fecha de mantenimiento: ")

            
            #asignamos el paciente
            pac.asignar_nombre(N)
            pac.asignar_cedula(C)
            pac.asignar_sexo(S)
            pac.asignar_implantes(implante)
            pac.asignar_fecha_revision(FR)
            pac.asignar_fecha_mantenimiento(FM)
            #guardamos el paciente en el sistema y el implante
            Sistem.agregar_implante(implante)
            Sistem.agregar_paciente(pac)
            

        elif menu == "2":
            C = input("Cedula: ")
            validar_N(C) #validamos la cedula 

            if Sistem.buscar_paciente_ced(C): 
                p = Sistem.verDatosPacienteC(C)
                print("Nombre: " + p.ver_nombre())
                print("Cedula: " + str(p.ver_cedula()))
                print("Genero: " + p.ver_sexo())
                print("Implantes: " + str(p.ver_implantes()))
                print("Fecha Revision: " + p.ver_fecha_revision())
                print("Fecha Mantenimiento: " + p.ver_fecha_mantenimiento())
    
            else: #si el paciente no existe 
                print("No se encontró el paciente con cédula", C)

        elif menu == "3":
            q = input("Cedula: ")
            validar_N(q)
            Sistem.eliminar_paciente(q) #eliminamos el paciente con la funcion 
            print("El paciente con cedula {} a sido eliminado" .format(q))
        
        elif menu == "4":
            break

        else:
            print("No es opcion ")


if __name__=='__main__':
    main()