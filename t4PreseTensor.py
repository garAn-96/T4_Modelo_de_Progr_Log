import cv2 #Captura y muestra video, dibuja sobre imágenes
import mediapipe as mp #Detecta landmarks faciales y procesa gestos
import numpy as np #Cálculos numéricos y manipulación de arrays
import requests #Obtiene IP pública vía HTTP
import mysql.connector #Conecta y opera con base de datos MySQL
import time #Controla tiempos y pausas
import socket #Obtiene IP privada local
from datetime import datetime #Fecha y hora actual para registros
import pandas as pd #Exporta datos a Excel para análisis

# ------------------------- CONFIGURACIÓN BASE DE DATOS -------------------------
def crear_base_datos():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='daddyLEO99##',
            auth_plugin='mysql_native_password'
        )
        cursor = conexion.cursor()
        
        # Crear BD si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS bd_prueba")
        cursor.execute("USE bd_prueba")
        
        # Crear tabla con nueva estructura
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha DATETIME NOT NULL,
                ip_privada VARCHAR(45) NOT NULL,
                ip_publica VARCHAR(45) NOT NULL,
                nombre_usuario VARCHAR(100) NOT NULL
            )
        """)
        conexion.commit()
        print("Base de datos y tabla verificadas/creadas")
        
    except Exception as e:
        print(f"Error en configuración BD: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# ------------------------- FUNCIONES DE RED -------------------------
def obtener_ip_privada():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_privada = s.getsockname()[0]
        s.close()
        return ip_privada
    except Exception as e:
        return f"Error: {e}"

def obtener_ip_publica():
    try:
        respuesta = requests.get('https://api.ipify.org?format=json', timeout=5)
        return respuesta.json()['ip']
    except Exception as e:
        return f"Error: {e}"

# ------------------------- FUNCIÓN PRINCIPAL -------------------------
def insertar_datos(ip_privada, ip_publica, nombre_usuario):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='bd_prueba',
            user='root',
            password='daddyLEO99##',
            auth_plugin='mysql_native_password'
        )
        
        cursor = conexion.cursor()
        
        # Insertar datos con marca temporal
        query = """
            INSERT INTO datos_usuario 
            (fecha, ip_privada, ip_publica, nombre_usuario)
            VALUES (%s, %s, %s, %s)
        """
        valores = (datetime.now(), ip_privada, ip_publica, nombre_usuario)
        cursor.execute(query, valores)
        conexion.commit()
        
        # Generar Excel con todos los registros
        df = pd.read_sql("SELECT * FROM datos_usuario", conexion)
        df.to_excel('registros_faciales.xlsx', index=False)
        print("Datos actualizados en Excel")
        
    except Exception as e:
        print(f"Error BD: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# ------------------------- RECONOCIMIENTO FACIAL -------------------------
def inicializar_facemesh():
    mp_face_mesh = mp.solutions.face_mesh
    return mp_face_mesh.FaceMesh(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_faces=1
    )

def procesar_gestos(frame, face_mesh):
    global boca_abierta, inicio_boca_abierta
    
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    frame.flags.writeable = False
    resultados = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    frame.flags.writeable = True
    
    if resultados.multi_face_landmarks:
        for landmarks in resultados.multi_face_landmarks:
            # Dibuja los landmarks en el frame
            mp_drawing.draw_landmarks(
                frame,
                landmarks,
                mp.solutions.face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec
            )

            # Puntos específicos para mejorar detección de boca
            labio_sup = landmarks.landmark[13]
            labio_inf = landmarks.landmark[14]
            
            h, w = frame.shape[:2]
            pos_sup = (int(labio_sup.x * w), int(labio_sup.y * h))
            pos_inf = (int(labio_inf.x * w), int(labio_inf.y * h))
            
            distancia = np.linalg.norm(np.array(pos_sup) - np.array(pos_inf))
            
            if distancia > 15:  # Ajuste preciso para gesto
                if not boca_abierta:
                    boca_abierta = True
                    inicio_boca_abierta = time.time()
                elif time.time() - inicio_boca_abierta > 1.5:  # Tiempo óptimo
                    cv2.putText(frame, "DETECTADO!", (30, 50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                    return True
            else:
                boca_abierta = False
    return False

# ------------------------- EJECUCIÓN PRINCIPAL -------------------------
if __name__ == "__main__":
    crear_base_datos()
    
    # Configuración inicial
    face_mesh = inicializar_facemesh()
    cap = cv2.VideoCapture(0)
    boca_abierta = False
    usuario = "Pascual"
    
    # Obtener IPs una vez al inicio
    ip_publica = obtener_ip_publica()
    ip_privada = obtener_ip_privada()
    
    print("Sistema iniciado. Presione 'Q' para salir...")
    
    while cap.isOpened():
        exito, frame = cap.read()
        if not exito:
            continue
            
        if procesar_gestos(frame, face_mesh):
            insertar_datos(ip_privada, ip_publica, usuario)
            time.sleep(1)  # Prevenir múltiples detecciones
            
        cv2.imshow('Detector de Gestos', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
