
class Paciente:
    def __init__(self, id, nombre, apellido, edad, sexo, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        self._dni = dni
        self._historial = []
        self._recetas = []

    def mostrar_informacion(self):
        print("ID:", self._id)
        print("Nombre:", self._nombre)
        print("Apellido:", self._apellido)
        print("Edad:", self._edad)
        print("Sexo:", self._sexo)
        print("DNI:", "******" + self._dni[-2:])


class Medico:
    def __init__(self, id, nombre, apellido, edad, sexo, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        self._dni = dni

    def mostrar_informacion(self):
        print("ID:", self._id)
        print("Nombre:", self._nombre)
        print("Apellido:", self._apellido)
        print("Edad:", self._edad)
        print("Sexo:", self._sexo)
        print("DNI:", "******" + self._dni[-2:])


class Enfermero:
    def __init__(self, id, nombre, apellido, edad, sexo, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        self._dni = dni

    def mostrar_informacion(self):
        print("ID:", self._id)
        print("Nombre:", self._nombre)
        print("Apellido:", self._apellido)
        print("Edad:", self._edad)
        print("Sexo:", self._sexo)
        print("DNI:", "******" + self._dni[-2:])


class Cita:
    def __init__(self, id, paciente, medico, fecha, hora, motivo):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._estado = "Programada"

    def mostrar_informacion(self):
        print("\nID de cita:", self._id)
        print("Paciente:", self._paciente._nombre,
              self._paciente._apellido)
        print("Medico:", self._medico._nombre,
              self._medico._apellido)
        print("Fecha:", self._fecha)
        print("Hora:", self._hora)
        print("Motivo:", self._motivo)
        print("Estado:", self._estado)


class Atencion:
    def __init__(self, id, paciente, medico, enfermero,
                 motivo, diagnostico, tratamiento):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._enfermero = enfermero
        self._motivo = motivo
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento

    def mostrar_informacion(self):
        print("\nID de atencion:", self._id)
        print("Paciente:", self._paciente._nombre,
              self._paciente._apellido)
        print("Medico:", self._medico._nombre,
              self._medico._apellido)
        if self._enfermero:
            print("Enfermero:", self._enfermero._nombre,
                  self._enfermero._apellido)
        else:
            print("Enfermero: No asignado")
        print("Motivo:", self._motivo)
        print("Diagnostico:", self._diagnostico)
        print("Tratamiento:", self._tratamiento)


class Receta:
    def __init__(self, id, paciente, medico, fecha,
                 medicamento, indicaciones):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._medicamento = medicamento
        self._indicaciones = indicaciones

    def mostrar_informacion(self):
        print("\n========== RECETA MEDICA ==========")
        print("ID de receta:", self._id)
        print("Fecha:", self._fecha)
        print("PACIENTE:")
        print(self._paciente._nombre, self._paciente._apellido)
        print("ID paciente:", self._paciente._id)
        print("\nMEDICO:")
        print(self._medico._nombre, self._medico._apellido)
        print("ID medico:", self._medico._id)
        print("\nMedicamento:", self._medicamento)
        print("Indicaciones:", self._indicaciones)
        print("===================================")


class SistemaSalud:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.enfermeros = []
        self.citas = []
        self.atenciones = []
        self.recetas = []


sistema = SistemaSalud()


# ==================================
# REGISTRO UNICO
# ==================================

def registrar_persona():
    while True:
        print("\n===== REGISTRAR PERSONA =====")
        print("1. Paciente")
        print("2. Medico")
        print("3. Enfermero")
        print("0. Volver al menu")

        opcion = input("Seleccione: ")

        if opcion == "0":
            break

        if opcion not in ["1", "2", "3"]:
            print("Opcion invalida.")
            continue

        id_persona = input("Ingresar ID: ")
        nombre = input("Ingresar nombre: ")
        apellido = input("Ingresar apellido: ")
        edad = input("Ingresar edad: ")
        sexo = input("Ingresar sexo: ")
        dni = input("Ingresar DNI: ")

        if not id_persona or not nombre or not apellido or not dni:
            print("Completa los campos obligatorios.")
            continue

        if not dni.isdigit() or len(dni) != 8:
            print("El DNI debe tener 8 digitos.")
            continue

        # Evitar repetir ID o DNI en cualquier tipo de persona
        repetido = False
        todas = (sistema.pacientes + sistema.medicos
                 + sistema.enfermeros)

        for persona in todas:
            if persona._id == id_persona or persona._dni == dni:
                repetido = True
                break

        if repetido:
            print("El ID o DNI ya esta registrado.")
            continue

        if opcion == "1":
            persona = Paciente(
                id_persona, nombre, apellido, edad, sexo, dni
            )
            sistema.pacientes.append(persona)
            tipo = "Paciente"

        elif opcion == "2":
            persona = Medico(
                id_persona, nombre, apellido, edad, sexo, dni
            )
            sistema.medicos.append(persona)
            tipo = "Medico"

        else:
            persona = Enfermero(
                id_persona, nombre, apellido, edad, sexo, dni
            )
            sistema.enfermeros.append(persona)
            tipo = "Enfermero"

        print("\n", tipo, "registrado correctamente.")
        persona.mostrar_informacion()


# ==================================
# BUSQUEDAS
# ==================================

def buscar_en_lista(lista, tipo):
    print("\n===== BUSCAR", tipo.upper(), "=====")
    dato = input("Ingresar ID o DNI: ")

    for persona in lista:
        if persona._id == dato or persona._dni == dato:
            print("\nPersona encontrada:")
            persona.mostrar_informacion()
            return persona

    print("No se encontro la persona.")
    return None


def buscar_paciente():
    return buscar_en_lista(sistema.pacientes, "Paciente")


def buscar_medico():
    return buscar_en_lista(sistema.medicos, "Medico")


def buscar_enfermero():
    return buscar_en_lista(sistema.enfermeros, "Enfermero")


def buscar_persona():
    while True:
        print("\n===== BUSCAR PERSONA =====")
        print("1. Paciente")
        print("2. Medico")
        print("3. Enfermero")
        print("0. Volver al menu")

        opcion = input("Seleccione: ")

        if opcion == "0":
            break
        elif opcion == "1":
            buscar_paciente()
        elif opcion == "2":
            buscar_medico()
        elif opcion == "3":
            buscar_enfermero()
        else:
            print("Opcion invalida.")


# ==================================
# REGISTRAR CITA
# ==================================

def registrar_cita():
    print("\n===== REGISTRAR CITA =====")

    paciente = buscar_paciente()
    if paciente is None:
        return

    medico = buscar_medico()
    if medico is None:
        return

    id_cita = str(len(sistema.citas) + 1)
    fecha = input("Fecha (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    motivo = input("Motivo de la cita: ")

    cita = Cita(id_cita, paciente, medico,
                fecha, hora, motivo)

    sistema.citas.append(cita)
    print("\nCita registrada correctamente.")
    cita.mostrar_informacion()


# ==================================
# MOSTRAR CITAS
# ==================================

def mostrar_citas():
    print("\n===== CITAS REGISTRADAS =====")

    if not sistema.citas:
        print("No hay citas registradas.")
        return

    for cita in sistema.citas:
        cita.mostrar_informacion()


# ==================================
# REALIZAR ATENCION
# ==================================

def realizar_atencion():
    print("\n===== ATENCION MEDICA =====")

    paciente = buscar_paciente()
    if paciente is None:
        return

    medico = buscar_medico()
    if medico is None:
        return

    print("\n¿Desea asignar un enfermero?")
    print("1. Si")
    print("2. No")
    opcion = input("Seleccione: ")

    enfermero = None

    if opcion == "1":
        enfermero = buscar_enfermero()
        if enfermero is None:
            return
    elif opcion != "2":
        print("Opcion invalida.")
        return

    motivo = input("Motivo de atencion: ")
    diagnostico = input("Diagnostico: ")
    tratamiento = input("Tratamiento: ")

    id_atencion = str(len(sistema.atenciones) + 1)

    atencion = Atencion(
        id_atencion, paciente, medico, enfermero,
        motivo, diagnostico, tratamiento
    )

    sistema.atenciones.append(atencion)
    paciente._historial.append(atencion)

    print("\nAtencion registrada correctamente.")
    atencion.mostrar_informacion()


# ==================================
# MOSTRAR ATENCION
# ==================================

def mostrar_atencion():
    print("\n===== MOSTRAR ATENCION =====")
    id_atencion = input("Ingresar ID de atencion: ")

    for atencion in sistema.atenciones:
        if atencion._id == id_atencion:
            atencion.mostrar_informacion()
            return

    print("No se encontro la atencion.")


# ==================================
# HISTORIAL DEL PACIENTE EN ATENCIONES
# ==================================

def mostrar_historial():
    print("\n===== HISTORIAL DEL PACIENTE =====")

    paciente = buscar_paciente()
    if paciente is None:
        return

    print("\nHistorial de:",
          paciente._nombre, paciente._apellido)

    if not paciente._historial:
        print("No tiene atenciones registradas.")
    else:
        for atencion in paciente._historial:
            atencion.mostrar_informacion()

    print("\n===== RECETAS DEL PACIENTE =====")

    if not paciente._recetas:
        print("No tiene recetas registradas.")
    else:
        for receta in paciente._recetas:
            receta.mostrar_informacion()


# ==================================
# DAR RECETA
# ==================================

def dar_receta():
    print("\n===== EMITIR RECETA MEDICA =====")

    print("\nIdentificar al medico que emite la receta:")
    medico = buscar_medico()
    if medico is None:
        print("No se puede emitir la receta sin un medico registrado.")
        return

    print("\nIdentificar al paciente:")
    paciente = buscar_paciente()
    if paciente is None:
        return

    print("\n===== DATOS DE LA RECETA =====")
    fecha = input("Fecha (DD/MM/AAAA): ")
    medicamento = input("Medicamento indicado: ")
    indicaciones = input("Indicaciones escritas por el medico: ")

    if not medicamento or not indicaciones:
        print("Completa el medicamento y las indicaciones.")
        return

    id_receta = str(len(sistema.recetas) + 1)

    receta = Receta(
        id_receta, paciente, medico,
        fecha, medicamento, indicaciones
    )

    sistema.recetas.append(receta)
    paciente._recetas.append(receta)

    print("\nReceta registrada correctamente.")
    receta.mostrar_informacion()


# ==================================
# MOSTRAR RECETA
# ==================================

def mostrar_receta():
    print("\n===== CONSULTAR RECETA =====")
    id_receta = input("Ingresar ID de receta: ")

    for receta in sistema.recetas:
        if receta._id == id_receta:
            receta.mostrar_informacion()
            return

    print("No se encontro la receta.")


# ==================================
# SUBMENU DE CITAS
# ==================================

def menu_citas():
    while True:
        print("\n===== MENU DE CITAS =====")
        print("1. Registrar cita")
        print("2. Mostrar citas")
        print("0. Volver al menu")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            mostrar_citas()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


# ==================================
# SUBMENU DE ATENCIONES
# ==================================

def menu_atenciones():
    while True:
        print("\n===== MENU DE ATENCIONES =====")
        print("1. Realizar atencion medica")
        print("2. Mostrar atencion medica")
        print("3. Ver historial del paciente")
        print("0. Volver al menu")

        opcion = input("Seleccione: ")

        if opcion == "1":
            realizar_atencion()
        elif opcion == "2":
            mostrar_atencion()
        elif opcion == "3":
            mostrar_historial()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


# ==================================
# SUBMENU DE RECETAS
# ==================================

def menu_recetas():
    while True:
        print("\n===== MENU DE RECETAS =====")
        print("1. Dar receta a paciente")
        print("2. Mostrar receta")
        print("0. Volver al menu")

        opcion = input("Seleccione: ")

        if opcion == "1":
            dar_receta()
        elif opcion == "2":
            mostrar_receta()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


# ==================================
# MENU PRINCIPAL
# ==================================

def mostrar_menu():
    print("\n========== SISTEMA DE SALUD ==========")
    print("1. Registrar persona")
    print("2. Buscar persona")
    print("3. Menu de citas")
    print("4. Menu de atenciones")
    print("5. Menu de recetas")
    print("0. Salir")
    print("======================================")


# ==================================
# PROGRAMA PRINCIPAL
# ==================================

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_persona()

    elif opcion == "2":
        buscar_persona()

    elif opcion == "3":
        menu_citas()

    elif opcion == "4":
        menu_atenciones()

    elif opcion == "5":
        menu_recetas()

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion invalida.")