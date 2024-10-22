import customtkinter as ctk
import threading

# Importar la función desde el archivo main.py
from main import process_sunat_request

# Configurar la apariencia para que siga la configuración del sistema
ctk.set_appearance_mode("system")  # Esto hará que siga el modo claro/oscuro del sistema
ctk.set_default_color_theme("blue")  # Tema de color predeterminado

# Lista completa de títulos
all_titles = [
    "Activacion de cuenta de usuario de correo",
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
        process_sunat_request(sede, titulo, descripcion)
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
