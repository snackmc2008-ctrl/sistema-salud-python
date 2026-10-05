import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ============================================================
# MODELO
# ============================================================

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
        return f"ID: {self._id}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}\nSexo: {self._sexo}\nDNI: ******{self._dni[-2:]}"


class Medico:
    def __init__(self, id, nombre, apellido, edad, sexo, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        self._dni = dni

    def mostrar_informacion(self):
        return f"ID: {self._id}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}\nSexo: {self._sexo}\nDNI: ******{self._dni[-2:]}"


class Enfermero:
    def __init__(self, id, nombre, apellido, edad, sexo, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        self._dni = dni

    def mostrar_informacion(self):
        return f"ID: {self._id}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}\nSexo: {self._sexo}\nDNI: ******{self._dni[-2:]}"


class Cita:
    def __init__(self, id, paciente, medico, fecha, hora, motivo):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._estado = "Programada"


class Atencion:
    def __init__(self, id, paciente, medico, enfermero, motivo, diagnostico, tratamiento):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._enfermero = enfermero
        self._motivo = motivo
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento


class Receta:
    def __init__(self, id, paciente, medico, fecha, medicamento, indicaciones):
        self._id = id
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._medicamento = medicamento
        self._indicaciones = indicaciones


class SistemaSalud:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.enfermeros = []
        self.citas = []
        self.atenciones = []
        self.recetas = []


sistema = SistemaSalud()

# ============================================================
# INTERFAZ
# ============================================================

class SistemaSaludApp:
    BG = "#eef2f7"
    SIDEBAR = "#123b5d"
    SIDEBAR_HOVER = "#1b527c"
    PRIMARY = "#1685ff"
    DARK = "#102a43"
    WHITE = "#ffffff"
    TEXT = "#263238"
    MUTED = "#6b7280"
    GREEN = "#198754"

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Salud")
        self.root.geometry("1180x720")
        self.root.minsize(1000, 650)
        self.root.configure(bg=self.BG)

        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except:
            pass

        self.configurar_estilos()
        self.crear_interfaz()
        self.mostrar_inicio()

    def configurar_estilos(self):
        self.style.configure(
            "Treeview",
            background="white",
            foreground=self.TEXT,
            rowheight=32,
            fieldbackground="white",
            font=("Segoe UI", 10)
        )
        self.style.configure(
            "Treeview.Heading",
            background=self.DARK,
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )
        self.style.map("Treeview", background=[("selected", "#cfe5ff")],
                       foreground=[("selected", self.DARK)])

        self.style.configure(
            "TCombobox",
            padding=8,
            font=("Segoe UI", 10)
        )

    def crear_interfaz(self):
        # Barra lateral
        self.sidebar = tk.Frame(self.root, bg=self.SIDEBAR, width=235)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        logo = tk.Frame(self.sidebar, bg=self.SIDEBAR, height=105)
        logo.pack(fill="x")

        tk.Label(
            logo, text="🏥", bg=self.SIDEBAR, fg="white",
            font=("Segoe UI Emoji", 32)
        ).pack(pady=(15, 0))

        tk.Label(
            logo, text="SISTEMA DE SALUD", bg=self.SIDEBAR,
            fg="white", font=("Segoe UI", 13, "bold")
        ).pack()

        tk.Label(
            self.sidebar, text="MENÚ PRINCIPAL", bg=self.SIDEBAR,
            fg="#a9c7df", font=("Segoe UI", 9, "bold")
        ).pack(anchor="w", padx=22, pady=(12, 8))

        botones = [
            ("⌂", "Inicio", self.mostrar_inicio),
            ("👤", "Registrar persona", self.ventana_registrar),
            ("🔎", "Buscar persona", self.ventana_buscar),
            ("📅", "Citas", self.ventana_citas),
            ("🩺", "Atenciones", self.ventana_atenciones),
            ("💊", "Recetas", self.ventana_recetas),
        ]

        for icono, texto, comando in botones:
            b = tk.Button(
                self.sidebar,
                text=f"  {icono}   {texto}",
                command=comando,
                anchor="w",
                bg=self.SIDEBAR,
                fg="white",
                activebackground=self.SIDEBAR_HOVER,
                activeforeground="white",
                relief="flat",
                bd=0,
                padx=16,
                pady=11,
                font=("Segoe UI", 10, "bold"),
                cursor="hand2"
            )
            b.pack(fill="x", padx=10, pady=2)

        tk.Frame(self.sidebar, bg="#28516f", height=1).pack(fill="x", padx=18, pady=18)

        tk.Button(
            self.sidebar,
            text="  ✕   Salir",
            command=self.root.destroy,
            anchor="w",
            bg=self.SIDEBAR,
            fg="#ffdddd",
            activebackground="#8f2635",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=16,
            pady=11,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack(fill="x", padx=10)

        # Área principal
        self.main = tk.Frame(self.root, bg=self.BG)
        self.main.pack(side="right", fill="both", expand=True)

        self.header = tk.Frame(self.main, bg="white", height=72)
        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        self.header_title = tk.Label(
            self.header, text="Inicio", bg="white", fg=self.DARK,
            font=("Segoe UI", 20, "bold")
        )
        self.header_title.pack(side="left", padx=30, pady=20)

        self.content = tk.Frame(self.main, bg=self.BG)
        self.content.pack(fill="both", expand=True, padx=25, pady=25)

    def limpiar(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def titulo(self, texto, subtitulo=None):
        self.header_title.config(text=texto)
        self.limpiar()

        if subtitulo:
            tk.Label(
                self.content, text=subtitulo, bg=self.BG, fg=self.MUTED,
                font=("Segoe UI", 10)
            ).pack(anchor="w", pady=(0, 15))

    def tarjeta(self, parent, titulo, valor, icono):
        card = tk.Frame(parent, bg="white", highlightbackground="#dbe3ec",
                        highlightthickness=1)
        card.pack(side="left", fill="both", expand=True, padx=6)

        tk.Label(card, text=icono, bg="white", font=("Segoe UI Emoji", 25)).pack(
            anchor="w", padx=18, pady=(15, 0)
        )
        tk.Label(card, text=titulo, bg="white", fg=self.MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", padx=18, pady=(5, 0))
        tk.Label(card, text=valor, bg="white", fg=self.DARK,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=18, pady=(0, 15))
        return card

    # ========================================================
    # INICIO
    # ========================================================

    def mostrar_inicio(self):
        self.titulo("Panel principal", "Resumen del sistema de salud")
        cards = tk.Frame(self.content, bg=self.BG)
        cards.pack(fill="x", pady=(5, 20))

        self.tarjeta(cards, "Pacientes", len(sistema.pacientes), "👤")
        self.tarjeta(cards, "Médicos", len(sistema.medicos), "🩺")
        self.tarjeta(cards, "Enfermeros", len(sistema.enfermeros), "👨‍⚕️")
        self.tarjeta(cards, "Citas", len(sistema.citas), "📅")

        box = tk.Frame(self.content, bg="white", highlightbackground="#dbe3ec",
                       highlightthickness=1)
        box.pack(fill="both", expand=True)

        tk.Label(box, text="Bienvenido al Sistema de Salud",
                 bg="white", fg=self.DARK,
                 font=("Segoe UI", 17, "bold")).pack(anchor="w", padx=25, pady=(25, 8))

        tk.Label(
            box,
            text="Gestiona pacientes, personal médico, citas, atenciones y recetas desde el menú lateral.",
            bg="white", fg=self.MUTED, font=("Segoe UI", 11)
        ).pack(anchor="w", padx=25)

        acciones = tk.Frame(box, bg="white")
        acciones.pack(anchor="w", padx=20, pady=25)

        self.boton(acciones, "👤 Registrar paciente", self.ventana_registrar).pack(
            side="left", padx=5
        )
        self.boton(acciones, "📅 Nueva cita", self.ventana_citas).pack(
            side="left", padx=5
        )
        self.boton(acciones, "🩺 Atención médica", self.ventana_atenciones).pack(
            side="left", padx=5
        )

    # ========================================================
    # UTILIDADES
    # ========================================================

    def boton(self, parent, texto, comando, primary=True):
        return tk.Button(
            parent, text=texto, command=comando,
            bg=self.PRIMARY if primary else "#e8eef5",
            fg="white" if primary else self.DARK,
            activebackground="#0d6dcc" if primary else "#d7e0e9",
            activeforeground="white" if primary else self.DARK,
            relief="flat", bd=0, padx=16, pady=10,
            font=("Segoe UI", 10, "bold"), cursor="hand2"
        )

    def campo(self, parent, etiqueta, fila, variable=None, show=None):
        tk.Label(parent, text=etiqueta, bg="white", fg=self.TEXT,
                 font=("Segoe UI", 10, "bold")).grid(
            row=fila, column=0, sticky="w", padx=18, pady=(10, 4)
        )
        entry = tk.Entry(
            parent, textvariable=variable, show=show,
            font=("Segoe UI", 10), relief="solid", bd=1
        )
        entry.grid(row=fila, column=1, sticky="ew", padx=(0, 18), pady=(10, 4),
                   ipady=6)
        return entry

    def panel(self, titulo):
        box = tk.Frame(self.content, bg="white", highlightbackground="#dbe3ec",
                       highlightthickness=1)
        box.pack(fill="x", pady=5)
        tk.Label(box, text=titulo, bg="white", fg=self.DARK,
                 font=("Segoe UI", 13, "bold")).pack(
            anchor="w", padx=18, pady=(15, 5)
        )
        return box

    # ========================================================
    # REGISTRAR PERSONA
    # ========================================================

    def ventana_registrar(self):
        self.titulo("Registrar persona", "Agrega pacientes, médicos o enfermeros")

        box = self.panel("Datos de la persona")
        form = tk.Frame(box, bg="white")
        form.pack(fill="x", padx=10, pady=5)

        tipo = tk.StringVar(value="Paciente")
        idv = tk.StringVar()
        nombre = tk.StringVar()
        apellido = tk.StringVar()
        edad = tk.StringVar()
        sexo = tk.StringVar()
        dni = tk.StringVar()

        tk.Label(form, text="Tipo", bg="white", fg=self.TEXT,
                 font=("Segoe UI", 10, "bold")).grid(
            row=0, column=0, sticky="w", padx=18, pady=(10, 4)
        )
        combo = ttk.Combobox(
            form, textvariable=tipo,
            values=["Paciente", "Médico", "Enfermero"],
            state="readonly", width=28
        )
        combo.grid(row=0, column=1, sticky="ew", padx=(0, 18), pady=(10, 4))

        self.campo(form, "ID", 1, idv)
        self.campo(form, "Nombre", 2, nombre)
        self.campo(form, "Apellido", 3, apellido)
        self.campo(form, "Edad", 4, edad)
        self.campo(form, "Sexo", 5, sexo)
        self.campo(form, "DNI (8 dígitos)", 6, dni)

        form.columnconfigure(1, weight=1)

        def registrar():
            if not all([idv.get().strip(), nombre.get().strip(),
                        apellido.get().strip(), dni.get().strip()]):
                messagebox.showwarning("Datos incompletos",
                                       "Completa los campos obligatorios.")
                return

            if not dni.get().isdigit() or len(dni.get()) != 8:
                messagebox.showwarning("DNI inválido",
                                       "El DNI debe tener exactamente 8 dígitos.")
                return

            todas = sistema.pacientes + sistema.medicos + sistema.enfermeros
            if any(p._id == idv.get().strip() or p._dni == dni.get().strip()
                   for p in todas):
                messagebox.showerror("Registro duplicado",
                                     "El ID o DNI ya está registrado.")
                return

            datos = (idv.get().strip(), nombre.get().strip(),
                     apellido.get().strip(), edad.get().strip(),
                     sexo.get().strip(), dni.get().strip())

            if tipo.get() == "Paciente":
                persona = Paciente(*datos)
                sistema.pacientes.append(persona)
            elif tipo.get() == "Médico":
                persona = Medico(*datos)
                sistema.medicos.append(persona)
            else:
                persona = Enfermero(*datos)
                sistema.enfermeros.append(persona)

            messagebox.showinfo(
                "Registro exitoso",
                f"{tipo.get()} registrado correctamente.\n\n{persona.mostrar_informacion()}"
            )

            for v in [idv, nombre, apellido, edad, sexo, dni]:
                v.set("")

            self.mostrar_inicio()

        botones = tk.Frame(self.content, bg=self.BG)
        botones.pack(anchor="e", pady=15)
        self.boton(botones, "✓ Registrar", registrar).pack(side="left", padx=5)

    # ========================================================
    # BUSCAR PERSONA
    # ========================================================

    def ventana_buscar(self):
        self.titulo("Buscar persona", "Busca por ID o DNI")

        box = self.panel("Consulta")
        top = tk.Frame(box, bg="white")
        top.pack(fill="x", padx=18, pady=10)

        dato = tk.StringVar()

        tk.Label(top, text="ID o DNI:", bg="white", fg=self.TEXT,
                 font=("Segoe UI", 10, "bold")).pack(side="left")
        tk.Entry(top, textvariable=dato, font=("Segoe UI", 10),
                 relief="solid", bd=1, width=35).pack(side="left", padx=10, ipady=6)

        resultado = tk.Text(
            box, height=10, bg="#f8fafc", fg=self.TEXT,
            relief="flat", font=("Consolas", 10), state="disabled"
        )
        resultado.pack(fill="x", padx=18, pady=(5, 18))

        def buscar():
            valor = dato.get().strip()
            todas = sistema.pacientes + sistema.medicos + sistema.enfermeros

            encontrado = next(
                (p for p in todas if p._id == valor or p._dni == valor),
                None
            )

            resultado.config(state="normal")
            resultado.delete("1.0", "end")

            if encontrado:
                resultado.insert("1.0", encontrado.mostrar_informacion())
            else:
                resultado.insert("1.0", "No se encontró la persona.")

            resultado.config(state="disabled")

        self.boton(top, "🔎 Buscar", buscar).pack(side="left")

        lista_box = self.panel("Personas registradas")
        columnas = ("tipo", "id", "nombre", "apellido", "edad", "sexo", "dni")
        tree = ttk.Treeview(lista_box, columns=columnas, show="headings", height=10)

        nombres = {
            "tipo": "Tipo", "id": "ID", "nombre": "Nombre",
            "apellido": "Apellido", "edad": "Edad", "sexo": "Sexo",
            "dni": "DNI"
        }

        for col in columnas:
            tree.heading(col, text=nombres[col])
            tree.column(col, width=100)

        tree.pack(fill="both", expand=True, padx=18, pady=(5, 18))

        for p in sistema.pacientes:
            tree.insert("", "end", values=("Paciente", p._id, p._nombre,
                                           p._apellido, p._edad, p._sexo,
                                           p._dni))
        for p in sistema.medicos:
            tree.insert("", "end", values=("Médico", p._id, p._nombre,
                                           p._apellido, p._edad, p._sexo,
                                           p._dni))
        for p in sistema.enfermeros:
            tree.insert("", "end", values=("Enfermero", p._id, p._nombre,
                                           p._apellido, p._edad, p._sexo,
                                           p._dni))

    # ========================================================
    # CITAS
    # ========================================================

    def ventana_citas(self):
        self.titulo("Citas médicas", "Registra y consulta las citas")

        formbox = self.panel("Registrar nueva cita")
        form = tk.Frame(formbox, bg="white")
        form.pack(fill="x", padx=10, pady=5)

        pacientes = [f"{p._id} - {p._nombre} {p._apellido}"
                     for p in sistema.pacientes]
        medicos = [f"{m._id} - {m._nombre} {m._apellido}"
                   for m in sistema.medicos]

        pv = tk.StringVar()
        mv = tk.StringVar()
        fecha = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y"))
        hora = tk.StringVar()
        motivo = tk.StringVar()

        self.combo_campo(form, "Paciente", 0, pv, pacientes)
        self.combo_campo(form, "Médico", 1, mv, medicos)
        self.campo(form, "Fecha (DD/MM/AAAA)", 2, fecha)
        self.campo(form, "Hora (HH:MM)", 3, hora)
        self.campo(form, "Motivo", 4, motivo)
        form.columnconfigure(1, weight=1)

        def registrar():
            if not pv.get() or not mv.get() or not fecha.get() or not hora.get() or not motivo.get():
                messagebox.showwarning("Datos incompletos", "Completa todos los campos.")
                return

            pid = pv.get().split(" - ")[0]
            mid = mv.get().split(" - ")[0]

            paciente = next((p for p in sistema.pacientes if p._id == pid), None)
            medico = next((m for m in sistema.medicos if m._id == mid), None)

            cita = Cita(str(len(sistema.citas) + 1), paciente, medico,
                        fecha.get(), hora.get(), motivo.get())
            sistema.citas.append(cita)

            messagebox.showinfo("Cita registrada",
                                f"Cita #{cita._id} registrada correctamente.")

            self.ventana_citas()

        actions = tk.Frame(self.content, bg=self.BG)
        actions.pack(anchor="e", pady=10)
        self.boton(actions, "✓ Registrar cita", registrar).pack()

        lista = self.panel("Citas registradas")
        cols = ("id", "paciente", "medico", "fecha", "hora", "motivo", "estado")
        tree = ttk.Treeview(lista, columns=cols, show="headings", height=8)

        headers = {
            "id": "ID", "paciente": "Paciente", "medico": "Médico",
            "fecha": "Fecha", "hora": "Hora", "motivo": "Motivo",
            "estado": "Estado"
        }

        for c in cols:
            tree.heading(c, text=headers[c])
            tree.column(c, width=100)

        tree.pack(fill="both", expand=True, padx=18, pady=(5, 18))

        for c in sistema.citas:
            tree.insert("", "end", values=(
                c._id,
                f"{c._paciente._nombre} {c._paciente._apellido}",
                f"{c._medico._nombre} {c._medico._apellido}",
                c._fecha, c._hora, c._motivo, c._estado
            ))

    # ========================================================
    # ATENCIONES
    # ========================================================

    def ventana_atenciones(self):
        self.titulo("Atenciones médicas", "Registra atenciones y consulta el historial")

        formbox = self.panel("Realizar atención médica")
        form = tk.Frame(formbox, bg="white")
        form.pack(fill="x", padx=10, pady=5)

        pacientes = [f"{p._id} - {p._nombre} {p._apellido}"
                     for p in sistema.pacientes]
        medicos = [f"{m._id} - {m._nombre} {m._apellido}"
                   for m in sistema.medicos]
        enfermeros = [f"{e._id} - {e._nombre} {e._apellido}"
                      for e in sistema.enfermeros]

        pv = tk.StringVar()
        mv = tk.StringVar()
        ev = tk.StringVar(value="Sin asignar")
        motivo = tk.StringVar()
        diagnostico = tk.StringVar()
        tratamiento = tk.StringVar()

        self.combo_campo(form, "Paciente", 0, pv, pacientes)
        self.combo_campo(form, "Médico", 1, mv, medicos)
        self.combo_campo(form, "Enfermero", 2, ev, ["Sin asignar"] + enfermeros)
        self.campo(form, "Motivo", 3, motivo)
        self.campo(form, "Diagnóstico", 4, diagnostico)
        self.campo(form, "Tratamiento", 5, tratamiento)
        form.columnconfigure(1, weight=1)

        def registrar():
            if not pv.get() or not mv.get() or not motivo.get() or not diagnostico.get() or not tratamiento.get():
                messagebox.showwarning("Datos incompletos", "Completa los campos obligatorios.")
                return

            pid = pv.get().split(" - ")[0]
            mid = mv.get().split(" - ")[0]

            paciente = next((p for p in sistema.pacientes if p._id == pid), None)
            medico = next((m for m in sistema.medicos if m._id == mid), None)

            enfermero = None
            if ev.get() != "Sin asignar":
                eid = ev.get().split(" - ")[0]
                enfermero = next(
                    (e for e in sistema.enfermeros if e._id == eid), None
                )

            at = Atencion(
                str(len(sistema.atenciones) + 1),
                paciente, medico, enfermero,
                motivo.get(), diagnostico.get(), tratamiento.get()
            )

            sistema.atenciones.append(at)
            paciente._historial.append(at)

            messagebox.showinfo(
                "Atención registrada",
                f"Atención #{at._id} registrada correctamente."
            )
            self.ventana_atenciones()

        actions = tk.Frame(self.content, bg=self.BG)
        actions.pack(anchor="e", pady=10)
        self.boton(actions, "✓ Registrar atención", registrar).pack()

        lista = self.panel("Atenciones registradas")
        cols = ("id", "paciente", "medico", "enfermero", "motivo", "diagnostico")
        tree = ttk.Treeview(lista, columns=cols, show="headings", height=7)

        headers = {
            "id": "ID", "paciente": "Paciente", "medico": "Médico",
            "enfermero": "Enfermero", "motivo": "Motivo",
            "diagnostico": "Diagnóstico"
        }

        for c in cols:
            tree.heading(c, text=headers[c])
            tree.column(c, width=125)

        tree.pack(fill="both", expand=True, padx=18, pady=(5, 18))

        for a in sistema.atenciones:
            enf = "No asignado" if not a._enfermero else (
                f"{a._enfermero._nombre} {a._enfermero._apellido}"
            )
            tree.insert("", "end", values=(
                a._id,
                f"{a._paciente._nombre} {a._paciente._apellido}",
                f"{a._medico._nombre} {a._medico._apellido}",
                enf, a._motivo, a._diagnostico
            ))

        histbox = self.panel("Historial de un paciente")
        htop = tk.Frame(histbox, bg="white")
        htop.pack(fill="x", padx=18, pady=8)

        hv = tk.StringVar()
        self.combo_campo(htop, "Paciente", 0, hv, pacientes, compact=True)

        historial = tk.Text(
            histbox, height=8, bg="#f8fafc", fg=self.TEXT,
            relief="flat", font=("Consolas", 9), state="disabled"
        )
        historial.pack(fill="x", padx=18, pady=(0, 18))

        def ver_historial():
            historial.config(state="normal")
            historial.delete("1.0", "end")

            if not hv.get():
                historial.insert("1.0", "Selecciona un paciente.")
            else:
                pid = hv.get().split(" - ")[0]
                p = next((x for x in sistema.pacientes if x._id == pid), None)

                if p and p._historial:
                    for a in p._historial:
                        historial.insert(
                            "end",
                            f"Atención #{a._id}\n"
                            f"Motivo: {a._motivo}\n"
                            f"Diagnóstico: {a._diagnostico}\n"
                            f"Tratamiento: {a._tratamiento}\n"
                            "----------------------------------------\n"
                        )
                else:
                    historial.insert("1.0", "No tiene atenciones registradas.")

            historial.config(state="disabled")

        self.boton(htop, "📋 Ver historial", ver_historial).grid(
            row=0, column=2, padx=8
        )

    # ========================================================
    # RECETAS
    # ========================================================

    def ventana_recetas(self):
        self.titulo("Recetas médicas", "Emite y consulta recetas")

        formbox = self.panel("Emitir receta médica")
        form = tk.Frame(formbox, bg="white")
        form.pack(fill="x", padx=10, pady=5)

        pacientes = [f"{p._id} - {p._nombre} {p._apellido}"
                     for p in sistema.pacientes]
        medicos = [f"{m._id} - {m._nombre} {m._apellido}"
                   for m in sistema.medicos]

        mv = tk.StringVar()
        pv = tk.StringVar()
        fecha = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y"))
        medicamento = tk.StringVar()
        indicaciones = tk.StringVar()

        self.combo_campo(form, "Médico", 0, mv, medicos)
        self.combo_campo(form, "Paciente", 1, pv, pacientes)
        self.campo(form, "Fecha (DD/MM/AAAA)", 2, fecha)
        self.campo(form, "Medicamento", 3, medicamento)
        self.campo(form, "Indicaciones", 4, indicaciones)
        form.columnconfigure(1, weight=1)

        def emitir():
            if not mv.get() or not pv.get() or not medicamento.get() or not indicaciones.get():
                messagebox.showwarning("Datos incompletos",
                                       "Completa los campos obligatorios.")
                return

            mid = mv.get().split(" - ")[0]
            pid = pv.get().split(" - ")[0]

            medico = next((m for m in sistema.medicos if m._id == mid), None)
            paciente = next((p for p in sistema.pacientes if p._id == pid), None)

            receta = Receta(
                str(len(sistema.recetas) + 1),
                paciente, medico, fecha.get(),
                medicamento.get(), indicaciones.get()
            )

            sistema.recetas.append(receta)
            paciente._recetas.append(receta)

            messagebox.showinfo(
                "Receta emitida",
                f"Receta #{receta._id} registrada correctamente."
            )
            self.ventana_recetas()

        actions = tk.Frame(self.content, bg=self.BG)
        actions.pack(anchor="e", pady=10)
        self.boton(actions, "💊 Emitir receta", emitir).pack()

        lista = self.panel("Recetas registradas")
        cols = ("id", "fecha", "paciente", "medico", "medicamento", "indicaciones")
        tree = ttk.Treeview(lista, columns=cols, show="headings", height=8)

        headers = {
            "id": "ID", "fecha": "Fecha", "paciente": "Paciente",
            "medico": "Médico", "medicamento": "Medicamento",
            "indicaciones": "Indicaciones"
        }

        for c in cols:
            tree.heading(c, text=headers[c])
            tree.column(c, width=125)

        tree.pack(fill="both", expand=True, padx=18, pady=(5, 18))

        for r in sistema.recetas:
            tree.insert("", "end", values=(
                r._id, r._fecha,
                f"{r._paciente._nombre} {r._paciente._apellido}",
                f"{r._medico._nombre} {r._medico._apellido}",
                r._medicamento, r._indicaciones
            ))

        # Consulta de receta
        consult = self.panel("Consultar receta")
        top = tk.Frame(consult, bg="white")
        top.pack(fill="x", padx=18, pady=10)

        rid = tk.StringVar()
        tk.Label(top, text="ID de receta:", bg="white", fg=self.TEXT,
                 font=("Segoe UI", 10, "bold")).pack(side="left")
        tk.Entry(top, textvariable=rid, width=20, font=("Segoe UI", 10),
                 relief="solid", bd=1).pack(side="left", padx=10, ipady=6)

        details = tk.Text(top, height=6, bg="#f8fafc", fg=self.TEXT,
                           relief="flat", font=("Consolas", 9), state="disabled")
        details.pack(side="left", fill="x", expand=True, padx=10)

        def consultar():
            r = next((x for x in sistema.recetas if x._id == rid.get().strip()), None)

            details.config(state="normal")
            details.delete("1.0", "end")

            if r:
                details.insert(
                    "1.0",
                    f"RECETA #{r._id}\n"
                    f"Fecha: {r._fecha}\n"
                    f"Paciente: {r._paciente._nombre} {r._paciente._apellido}\n"
                    f"Médico: {r._medico._nombre} {r._medico._apellido}\n"
                    f"Medicamento: {r._medicamento}\n"
                    f"Indicaciones: {r._indicaciones}"
                )
            else:
                details.insert("1.0", "No se encontró la receta.")

            details.config(state="disabled")

        self.boton(top, "🔎 Consultar", consultar).pack(side="left")

    # ========================================================
    # COMPONENTE COMBOBOX
    # ========================================================

    def combo_campo(self, parent, etiqueta, fila, variable, valores,
                    compact=False):
        tk.Label(parent, text=etiqueta, bg="white", fg=self.TEXT,
                 font=("Segoe UI", 10, "bold")).grid(
            row=fila, column=0, sticky="w", padx=18, pady=(10, 4)
        )

        combo = ttk.Combobox(
            parent, textvariable=variable,
            values=valores, state="readonly"
        )
        combo.grid(
            row=fila, column=1, sticky="ew",
            padx=(0, 18), pady=(10, 4)
        )
        return combo


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaSaludApp(root)
    root.mainloop()
