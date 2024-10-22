import customtkinter as ctk
import threading

# Importar la función desde el archivo main.py
from main import submit_form

# Configurar la apariencia para que siga la configuración del sistema
ctk.set_appearance_mode("system")  # Esto hará que siga el modo claro/oscuro del sistema
ctk.set_default_color_theme("blue")  # Tema de color predeterminado

# Lista completa de títulos
all_titles = [
    "Activacion de cuenta de usuario de correo",
	"Activacion de cuenta de usuario de intranet",
	"Activacion de cuenta de usuario de red",
	"Apoyo a eventos",
	"Videoconferencia con Webex",
	"Videoconferencia con Skype",
	"Videoconferencia con Aethra",
	"Ataque de Virus",
	"Conexion del Equipo de Computo  (Especificar)",
	"Configuracion de cuenta de correo",
	"Configuracion de Impresora",
	"Configuracion de Pagina web",
	"Configuracion de Usuario",
	"Configuracion del Equipo de Computo  (Especificar)",
	"Deshabilitacion de SIAF",
	"Creacion de cuenta de usuario de correo",
	"Creacion de Cuenta de usuario de red",
	"Creacion de cuenta de usuario Intranet",
	"Creacion de Usuario SIGA MEF (Especificar Modulo)",
	"Creacion de Usuario SIGA (Especificar Modulo)",
	"Creacion de usuario Sistema de Tramite Documentario",
	"Creacion de Usuario SIL70 (Especificar Modulo)",
	"Desbloqueo de cuenta de correo",
	"Desbloqueo de cuenta de intranet",
	"Desbloqueo de cuenta de red",
	"Desbloqueo de cuenta de usuario SIGA",
	"Desplazamiento de equipos de computo  (Especificar)",
	"Instalacion de Escaner",
	"Habilitacion de salas de reuniones",
	"Instalacion de Impresora",
	"Instalacion de SIAF",
	"Instalacion de Anexo",
	"Instalacion de Microsoft Office",
	"Instalacion de Equipo de computo (Especificar)",
	"Instalacion de Sistemas administrativos",
	"Instalacion de Software",
	"Instalacion de telefonos",
	"Instalacion de Arcgis",
	"Instalacion de Software de diseño (Especificar software)",
	"Instalacion de Software Melissa V 2.0",
	"Instalacion de SIL70 ( Sistema de Patrimonio)",
	"Instalacion de programas basicos ( Especificar )",
	"Instalacion de SIGA",
	"Instalacion de SIGA MEF",
	"Instalacion de sistema operativo",
	"Instalacion de sistema WinVentas",
	"Instalacion de SPSS",
	"Instalacion de SQL (especificar version)",
	"Instalacion de STATA",
	"Instalacion de Usuario SIAF",
	"Instalacion de Punto de Red",
	"Instalacion de usuario SIGA",
	"Instalacion de Visual Basic",
	"Mantenimiento de impresora",
	"Instalacion sistema de tramite documentario(version escritorio)",
	"Realizacion de Inventario",
	"Otros",
	"Permiso a carpetas especiales",
	"Permisos a solicitudes a IP",
	"Problema de correo",
	"Problemas con aplicaciones",
	"Problemas con el compartir de archivos",
	"Problemas con el Correo",
	"Problemas con el mouse",
	"Problemas con el sistema operativo",
	"Problemas con el teclado",
	"Problemas con internet",
	"Problemas con intranet",
	"Problemas con IP",
	"Problemas con la cuenta de usuario",
	"Problemas con Equipo de Computo  (Especificar)",
	"Problemas con Microsoft Office",
	"Problemas con paginas web",
	"Problemas con programas instalados",
	"Problemas con Punto de Red",
	"Problemas con virus",
	"Problemas con Windows",
	"Problemas de impresion",
	"Problemas de red",
	"Problemas de uso de Telefono",
	"Problemas Pagina Web",
	"Problemas Switch",
	"Recuperacion de archivos",
	"Retiro de Anexo",
	"Reubicacion de equipos",
	"Solicitud de Backup de archivos",
	"Solicitud de cable telefonico",
	"Consulta Sistema de Tramite Documentario",
	"Deshabilitar/Habilitar Usuarios en el SIAF",
	"Problemas con el marcador Biometrico",
	"Impresiones  y  copias manchadas.",
	"Impresiones  atascadas.",
	"Impresora  sale error.",
	"Impresiones arrugadas.",
	"Impresiones no jala el papel.",
	"Impresiones se traba en el fusor.",
	"Configuracion de impresora y escaner",
	"Impresiones no saca dúplex.",
	"Impresiones no funciona el  Alimentador automático.",
	"Se trabo papel en el Alimentador Automático.",
	"Impresiones borrosas.",
	"Impresiones  con líneas.",
	"Impresiones muy claras",
	"Impresora no prende.",
	"Impresora con derrame de toner.",
	"Configuracion de  IP  en Impresora Multifuncional.",
	"Impresiones manchadas a un extremo.",
	"Impresiones  necesita mantenimiento preventivo.",
	"impresora  necesita  cambio de toner.",
	"Impresora necesita Mantenimiento General y Cambio de repuestos.",
	"Consulta Gestor de Contenido (Sharepoint)",
	"Mantenimiento del Sistema de Cobertura  Encuesta Nacional de Programas Estratégicos 2016 – ENAPRES",
	"Mantenimiento del Sistema del Directorio de Empresas y Establecimientos  - SIDE",
	"Mantenimiento del Sistema de Estadísticas  Vitales – Matrimonios",
	"Mantenimiento del Sistema de Codigos Estandarizados",
	"Sistema de Difusion de los Censos Nacionales - DWH ",
	"Carga/Actualizacion de Data  del Directorio de Empresas y Establecimientos ",
	"Mantenimiento del Sistema de Permanencia de Personal fuera del Horario Normal",
	"Mantenimiento de la Encuesta del RENAMU",
	"Mantenimiento de la Encuesta Economica Anual",
	"Mantenimiento de Normas Legales",
	"Mantenimiento del Sistema de Visitas",
	"Mantenimiento del Sistema de Ventas",
	"Mantenimiento del SIGA",
	"Mantenimiento del Sistema de Consecucion de RRHH",
	"Mantenimiento de Sistema de Mensajeria",
	"Asignacion de usuarios para el sistema de seguridad de aplicativos",
	"Generacion de videos de los sistemas de informacion",
	"Actualizacion de Micro datos",
	"Actualizacion del Portal de Transparencia",
	"Actualizacion del Portal del INEI",
	"Actualizacion de la Intranet",
	"Actualizacion de aplicaciones",
	"Pases a produccion de aplicaciones",
	"Mantenimiento del Sistema de Votacion Electronica",
	"Mantenimiento del PENDES",
	"Mantenimiento de digitacion ONP",
	"Servicio de implementacion de switch / switchcore / AP",
	"Administracion de proxy",
	"Administracion de firewall institucional",
	"Servicio de configuracion de impresora",
	"Monitoreo de aplicaciones y servicios",
	"Incidentes de red solucionados",
	"Instalacion de antivirus institucional PC",
	"Servicio de actualizaciones de windows PC",
	"Servicio de monitoreo ODEIS",
	"Servicio de asignacion de IP",
	"Permiso para conexion a impresora",
	"Restauracion de informacion",
	"Administracion del servicio de radioenlace",
	"Copia de cintas mensuales: BCR, ENEI, Sede Central",
	"Servicio de respaldo de informacion institucional",
	"Servicio de almacenamiento de archivos",
	"Servicio de directorio activo institucional ",
	"Servicio de correo electronico institucional",
	"Servicio de aplicaciones SIGA - MEF",
	"administracion de antispam",
	"Servicio de antivirus institucional Servidores",
	"Servicio de actualizaciones de windows Servidor",
	"Servicio de aplicaciones biostar - relojes biométricos",
	"Servicio de Página Web",
	"Servicio JBOSS",
	"Servicio Red Had",
	"Implementacion de Servidores Virtuales ",
	"Transmision en vivo - TV INEI",
	"Mantenimiento Preventivo de Equipo de Computo",
	"Publicacion de Aplicativos Web a Produccion",
	"Videoconferencia con Zoom",
	"CREACION DE CUENTA SSI",
	"Instalacion de Firma Digital",
	"Cambio de Equipo Informatico",
	"Revision y Diagnostico de Tablet (Masivo)",
	"Revision y Diagnostico de Tablet (Individual)",
	"Realizar Especificacion Tecnica",
	"Realizar Evaluacion Tecnica",
	"Realizar Conformidad Tecnica",
	"Reseteo de Contrasena",
	"Desarrollo de Sistemas - Soporte",
	"Quemado de CD o DVD",
	"Acceso Remoto",
	"Apoyo Remoto",
	"Configuracion De Laptop",
	"Capacitacion Videoconferencia",
	"Realizar Evaluacion Tecnica",
	"Implementacion de Cableado Estructurado",
	"Realizar especificacion Tecnica",
	"Apoyo en Videoconferencia",
	"Administracion del Help Desk",
	"Prendido de PC",
	"Entregar copia de Base Datos de proyectos",
	"Registro de Base Dato de proyectos",
	"Elaboracion de Informes",
	"Indizacion de legaj",
	"Problemas con el SGD",
	"Administracion de base de datos",
	"Mantenimiento SGRI -Code",
	"Mantenimiento SSI -Code",
	"Instalacion de Perifericos",
	"Implementación cableado estructurado(Todo el Día)",
	"Instalacion de Mica para Tablet(Individual)",
	"Configuración De Laptop(Masivo)",
	"Revisión de Monitores(Masivo)",
	"Revisión deMonitores",
	"Documentar Sistemas"
]

# Función para manejar el evento del botón
def enviar_datos():
    # Actualizar la etiqueta de estado para indicar que está procesando
    status_label.configure(text="Esperando...", text_color="orange")
    
    # Ejecutar la función en un hilo separado
    thread = threading.Thread(target=ejecutar_submit_form)
    thread.start()

# Función que ejecuta la función submit_form
def ejecutar_submit_form():
    sede = sede_var.get()
    titulo = titulo_var.get()
    descripcion = descripcion_entry.get("1.0", "end-1c")  # Obtener el texto del textbox

    try:
        # Llamar a la función submit_form
        submit_form(sede, titulo, descripcion)
        # Si tiene éxito, actualizar la etiqueta de estado
        status_label.configure(text="Proceso finalizado con éxito", text_color="green")
    except Exception as e:
        # En caso de error, actualizar la etiqueta de estado con el mensaje de error
        status_label.configure(text=f"Error: {str(e)}", text_color="red")

# Función para manejar la búsqueda en el selector
def update_options(event):
    """Filtra las opciones basadas en el término de búsqueda."""
    search_term = search_entry.get().lower()
    filtered_values = [title for title in all_titles if search_term in title.lower()]
    
    # Limpiar el frame existente
    clear_options()

    # Limitar el número de opciones a mostrar a 3
    for value in filtered_values[:3]:  # Solo mostrar hasta 3 resultados
        button = ctk.CTkButton(options_frame, text=value, command=lambda v=value: select_title(v))
        button.pack(fill='x', padx=5, pady=2)

def clear_options():
    """Limpia las opciones en el frame."""
    for widget in options_frame.winfo_children():
        widget.destroy()  # Destruir los widgets existentes

def select_title(value):
    """Selecciona un título del menú desplegable.""" 
    titulo_var.set(value)  # Establecer el valor seleccionado en el StringVar
    search_entry.delete(0, 'end')  # Limpiar el campo de búsqueda
    search_entry.insert(0, value)  # Insertar el valor seleccionado en el campo de búsqueda
    clear_options()  # Limpiar las opciones

def load_initial_options():
    """Cargar las opciones iniciales en el frame."""
    clear_options()  # Limpiar opciones existentes
    for title in all_titles[:3]:  # Cargar solo los primeros 3 títulos inicialmente
        button = ctk.CTkButton(options_frame, text=title, command=lambda v=title: select_title(v))
        button.pack(fill='x', padx=5, pady=2)

# Crear la ventana principal
root = ctk.CTk()  # Usar CTk en lugar de Tk
root.title("Scraping SII")
root.geometry("400x650")  # Tamaño de la ventana

# Etiqueta principal
label = ctk.CTkLabel(root, text="Interfaz gráfica con tema del sistema", font=("Helvetica", 16))
label.pack(pady=10)

# Campo selector para "Sede"
label_sede = ctk.CTkLabel(root, text="Selecciona la Sede:")
label_sede.pack(pady=5)
sede_var = ctk.StringVar(value="Sede Central")  # Valor inicial
sede_selector = ctk.CTkOptionMenu(root, values=["Sede Central", "Sede DNCN", "Sede Iquique"], variable=sede_var)
sede_selector.pack(pady=5)

# Campo de búsqueda para el título
label_titulo = ctk.CTkLabel(root, text="Selecciona el Título:")
label_titulo.pack(pady=5)

titulo_var = ctk.StringVar(value="Otros")  # Valor inicial
search_entry = ctk.CTkEntry(root)
search_entry.pack(pady=5)
search_entry.bind("<KeyRelease>", update_options)  # Actualiza las opciones al escribir

# Frame para las opciones filtradas
options_frame = ctk.CTkFrame(root)
options_frame.pack(pady=5, fill='x')

# Campo de descripción
label_descripcion = ctk.CTkLabel(root, text="Descripción:")
label_descripcion.pack(pady=5)
descripcion_entry = ctk.CTkTextbox(root, width=300, height=100)  # Ajusta la altura según sea necesario
descripcion_entry.pack(pady=10)
descripcion_entry.insert("1.0", "Se requiere apoyo para (nombre), ya que está experimentando problemas con (descripción del problema).")

# Botón para enviar los datos
button = ctk.CTkButton(root, text="Enviar", command=enviar_datos)
button.pack(pady=20)

# Etiqueta de estado para mostrar mensajes
status_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

# Centrar la ventana en la pantalla y moverla más arriba
x = int(root.winfo_screenwidth() / 2 - root.winfo_width() / 2) - 100
y = int(root.winfo_screenheight() / 2 - root.winfo_height() / 2) - 300  # Ajusta el valor aquí
root.geometry(f"+{x}+{y}")

# Cargar las opciones iniciales al iniciar la aplicación
load_initial_options()

# Ejecutar la interfaz gráfica
root.mainloop()
