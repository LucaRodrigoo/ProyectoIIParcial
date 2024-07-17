import cv2
import os
import face_recognition as fr
import numpy

def verificar_facial():
    ruta = "Empleados"  # carpeta donde se encuentran las fotos de los empleados
    mis_imagenes = []
    nombres_empleados = []
    lista_empleados = os.listdir(ruta)

    for empleado in lista_empleados:
        imagen_actual = cv2.imread(f"{ruta}/{empleado}")
        mis_imagenes.append(imagen_actual)
        nombres_empleados.append(os.path.splitext(empleado)[0])

    lista_empleados_codificada = codificar(mis_imagenes)

    captura = cv2.VideoCapture(0)

    exito, imagen = captura.read()

    captura.release()
    cv2.destroyAllWindows()

    if not exito:
        print("No se pudo tomar la foto")
        return None

    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, known_face_locations=cara_captura)

    for caracodif in cara_captura_codificada:
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif, tolerance=0.6)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        if coincidencias[indice_coincidencia]:
            return nombres_empleados[indice_coincidencia]

    return None

def codificar(imagenes):
    lista_codificada = []

    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)[0]
        lista_codificada.append(codificado)
    return lista_codificada
