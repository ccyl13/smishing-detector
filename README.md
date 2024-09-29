# Smishing Detector

## Descripción

**Smishing Detector** es una herramienta diseñada para analizar mensajes SMS en busca de señales de phishing (smishing). La herramienta puede identificar enlaces sospechosos, números de teléfono y palabras clave comunes asociadas con fraudes. Además, proporciona información sobre la seguridad de los enlaces y los números detectados.

## Capturas de Pantalla

A continuación se presentan algunas capturas de pantalla de la herramienta en acción:

![Análisis de SMS](https://github.com/ccyl13/smishing-detector/blob/main/Analizando%20SMS.png?raw=true)


## Instalación

 **Instala las dependencias sin necesidad de virtualizar**:
 
   ```bash

   sudo apt update && sudo apt install python3-tk python3-pil python3-pil.imagetk python3-requests python3-bs4

 **Ejecución**:

   ```bash
   git clone https://github.com/ccyl13/smishing-detector.git
   cd smishing-detector
   python3 smishing_detector.py
