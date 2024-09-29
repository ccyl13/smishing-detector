import re
import requests
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import webbrowser
from bs4 import BeautifulSoup

# Palabras clave y frases para el análisis
PALABRAS_CLAVE = [
    'urgente', 'verifica tu cuenta', 'oferta', 'gratis', 'dinero', 'banco',
    'robo', 'phishing', 'multa', 'ganaste', 'haz clic', 'inmediatamente',
    'respuesta requerida', 'actualiza tu cuenta', 'confirma', 'pago',
    'reembolso', 'sin costo', 'haga clic aquí', 'compra ahora', 'enlace',
    'pago urgente', 'verificación urgente', 'acción requerida', 'revisión inmediata',
    'último recordatorio', 'pendiente de pago', 'pago'
]

# Función para detectar enlaces en el SMS
def detectar_enlaces(sms):
    return re.findall(r'(https?://\S+)', sms)

# Función para detectar números de teléfono en el SMS
def detectar_telefonos(sms):
    return re.findall(r'(\+\d{1,3}\s?\d{1,14}(\s\d{1,13})?)', sms)

# Función para detectar palabras clave sospechosas en el SMS
def detectar_palabras_clave(sms):
    return [palabra for palabra in PALABRAS_CLAVE if palabra.lower() in sms.lower()]

# Función para obtener detalles del número de teléfono desde un sitio web (ejemplo)
def obtener_detalles_numero(numero):
    # Aquí puedes implementar una lógica de scraping real
    # Simulando información para este ejemplo
    return f"Información sobre el número {numero}: Puede estar relacionado con estafas o spam."

# Función para analizar un enlace
def analizar_enlace(enlace):
    # Simulando análisis de enlace
    if "page.link" in enlace:
        return False, "Dominio sospechoso, relacionado con servicios de redireccionamiento."
    return True, "Dominio seguro."

# Función para realizar análisis del SMS
def iniciar_analisis():
    global sms_entry, remitente_entry  # Definimos como global
    sms = sms_entry.get("1.0", tk.END).strip()
    remitente = remitente_entry.get().strip()

    resultado_texto.delete("1.0", tk.END)  # Limpiar área de resultado

    if sms and remitente:
        resultado_texto.insert(tk.END, "Iniciando análisis de SMS...\n\n")
        
        # Detectar enlaces
        enlaces = detectar_enlaces(sms)
        if enlaces:
            for enlace in enlaces:
                seguro, mensaje = analizar_enlace(enlace)
                resultado_texto.insert(tk.END, f"Verificación del dominio {enlace}: {mensaje}\n")
        else:
            resultado_texto.insert(tk.END, "No se detectaron enlaces.\n")
        
        # Detectar teléfonos
        telefonos = detectar_telefonos(sms)
        for telefono in telefonos:
            resultado_texto.insert(tk.END, f"Número de teléfono detectado: {telefono}\n")
            
            # Obtener detalles del número
            detalles = obtener_detalles_numero(telefono)
            resultado_texto.insert(tk.END, f"Detalles del número:\n{detalles}\n")

            # Advertencia general
            resultado_texto.insert(tk.END, "Nota: Un servicio público nunca te enviará un SMS desde un número móvil.\n")

        # Detectar palabras clave sospechosas
        palabras_clave = detectar_palabras_clave(sms)
        if palabras_clave:
            resultado_texto.insert(tk.END, f"Palabras clave detectadas en el SMS:\n{', '.join(palabras_clave)}.\n")
        else:
            resultado_texto.insert(tk.END, "No se detectaron palabras clave.\n")

        resultado_texto.insert(tk.END, "\nAnálisis completado.\n")
    else:
        resultado_texto.insert(tk.END, "Por favor, ingresa un SMS y un remitente para analizar.\n")

# Función para abrir la página web al hacer clic en el enlace
def abrir_pagina_web(event):
    webbrowser.open_new_tab("https://www.cyberlandsec.com")

# Crear la interfaz gráfica
def create_gui():
    global sms_entry, remitente_entry  # Definimos como global
    window = tk.Tk()
    window.title("Smishing Detector")
    window.geometry("800x700")
    window.config(bg="black")

    # Título del programa
    titulo = tk.Label(window, text="Smishing Detector", font=("Arial", 24, "bold"), fg="red", bg="black")
    titulo.pack(pady=10)  # Reducido el padding

    # Logo de CyberLand
    logo_image = Image.open("/home/thomas/Desktop/logo2.png")
    logo_image.thumbnail((400, 400), Image.LANCZOS)  # Aumentar aún más el tamaño del logo
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(window, image=logo_photo, bg="black")
    logo_label.image = logo_photo
    logo_label.pack()

    # Texto "Created by CyberLand" y enlace
    created_by = tk.Label(window, text="Created by CyberLand", font=("Arial", 16), fg="#39FF14", bg="black")
    created_by.pack()

    link_label = tk.Label(window, text="www.cyberlandsec.com", font=("Arial", 16, "underline"), fg="#9400D3", bg="black")
    link_label.pack()
    link_label.bind("<Button-1>", abrir_pagina_web)  # Hacer el enlace clickeable

    # Cuadro de texto para el SMS
    sms_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=5, font=("Arial", 12), bg="#333333", fg="white")
    sms_entry.pack(pady=10)
    sms_entry.insert(tk.END, "Ingresa el SMS a analizar...")

    # Cuadro de texto para el remitente
    remitente_entry = tk.Entry(window, width=40, font=("Arial", 12), bg="#333333", fg="white")
    remitente_entry.pack(pady=10)
    remitente_entry.insert(0, "Ingresa el remitente del SMS...")

    # Botón de análisis
    analizar_button = tk.Button(window, text="Iniciar Análisis", command=iniciar_analisis, bg="purple", fg="white", font=("Arial", 14))
    analizar_button.pack(pady=20)

    # Cuadro de resultados
    global resultado_texto
    resultado_texto = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10, font=("Arial", 12), bg="#333333", fg="white")
    resultado_texto.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
