import os
import datetime
from utilidades import Utilidades
from crearDBcaras import verificar_facial

localidades = {
    "01": {"nombre": "Atlántida",
           "municipios": {"01": "La Ceiba", "02": "El Porvenir", "03": "Tela", "04": "Arizona", "05": "Esparta",
                          "06": "Jutiapa", "07": "La Masica", "08": "San Francisco"}},
    "02": {"nombre": "Choluteca",
           "municipios": {"01": "Choluteca", "02": "Apacilagua", "03": "Concepción de María", "04": "Duyure",
                          "05": "El Corpus", "06": "El Triunfo", "07": "Marcovia", "08": "Morolica", "09": "Namasigüe",
                          "10": "Orocuina", "11": "Pespire", "12": "San Antonio de Flores", "13": "San Isidro",
                          "14": "San José", "15": "San Marcos de Colón", "16": "Santa Ana de Yusguare"}},
    "03": {"nombre": "Colón",
           "municipios": {"01": "Trujillo", "02": "Balfate", "03": "Iriona", "04": "Limón", "05": "Sabá",
                          "06": "Santa Fe", "07": "Santa Rosa de Aguán", "08": "Sonaguera", "09": "Tocoa",
                          "10": "Bonito Oriental"}},
    "04": {"nombre": "Comayagua",
           "municipios": {"01": "Comayagua", "02": "Ajuterique", "03": "El Rosario", "04": "Esquías", "05": "Humuya",
                          "06": "La Libertad", "07": "Lamaní", "08": "La Trinidad", "09": "Lejamani", "10": "Meámbar",
                          "11": "Minas de Oro", "12": "Ojos de Agua", "13": "San Jerónimo",
                          "14": "San José de Comayagua", "15": "San José del Potrero", "16": "San Luis",
                          "17": "San Sebastián", "18": "Siguatepeque", "19": "Villa de San Antonio", "20": "Las Lajas",
                          "21": "Taulabé"}},
    "05": {"nombre": "Copán",
           "municipios": {"01": "Santa Rosa de Copán", "02": "Cabañas", "03": "Concepción", "04": "Copán Ruinas",
                          "05": "Corquín", "06": "Cucuyagua", "07": "Dolores", "08": "Dulce Nombre", "09": "El Paraíso",
                          "10": "Florida", "11": "La Jigua", "12": "La Unión", "13": "Nueva Arcadia",
                          "14": "San Agustín", "15": "San Antonio", "16": "San Jerónimo", "17": "San José",
                          "18": "San Juan de Opoa", "19": "San Nicolás", "20": "San Pedro", "21": "Santa Rita",
                          "22": "Trinidad de Copán", "23": "Veracruz"}},
    "06": {"nombre": "Cortés",
           "municipios": {"01": "San Pedro Sula", "02": "Choloma", "03": "Omoa", "04": "Pimienta", "05": "Potrerillos",
                          "06": "Puerto Cortés", "07": "San Antonio de Cortés", "08": "San Francisco de Yojoa",
                          "09": "San Manuel", "10": "Santa Cruz de Yojoa", "11": "Villanueva", "12": "La Lima"}},
    "07": {"nombre": "El Paraíso",
           "municipios": {"01": "Yuscarán", "02": "Alauca", "03": "Danlí", "04": "El Paraíso", "05": "Güinope",
                          "06": "Jacaleapa", "07": "Liure", "08": "Morocelí", "09": "Oropolí", "10": "Potrerillos",
                          "11": "San Antonio de Flores", "12": "San Lucas", "13": "San Matías", "14": "Soledad",
                          "15": "Teupasenti", "16": "Texiguat", "17": "Vado Ancho", "18": "Yauyupe", "19": "Trojes"}},
    "08": {"nombre": "Francisco Morazán",
           "municipios": {"01": "Tegucigalpa", "02": "Alubarén", "03": "Cedros", "04": "Curarén", "05": "El Porvenir",
                          "06": "Guaimaca", "07": "La Libertad", "08": "La Venta", "09": "Lepaterique", "10": "Maraita",
                          "11": "Marale", "12": "Nueva Armenia", "13": "Ojojona", "14": "Orica", "15": "Reitoca",
                          "16": "Sabanagrande", "17": "San Antonio de Oriente", "18": "San Buenaventura",
                          "19": "San Ignacio", "20": "San Juan de Flores", "21": "San Miguelito", "22": "Santa Ana",
                          "23": "Santa Lucía", "24": "Talanga", "25": "Tatumbla", "26": "Valle de Ángeles",
                          "27": "Villa de San Francisco", "28": "Vallecillo"}},
    "09": {"nombre": "Gracias a Dios",
           "municipios": {"01": "Puerto Lempira", "02": "Brus Laguna", "03": "Ahuas", "04": "Juan Francisco Bulnes",
                          "05": "Ramón Villeda Morales", "06": "Wampusirpi"}},
    "10": {"nombre": "Intibucá",
           "municipios": {"01": "La Esperanza", "02": "Camasca", "03": "Colomoncagua", "04": "Concepción",
                          "05": "Dolores", "06": "Intibucá", "07": "Jesús de Otoro", "08": "Magdalena",
                          "09": "Masaguara", "10": "San Antonio", "11": "San Isidro", "12": "San Juan",
                          "13": "San Marcos de la Sierra", "14": "San Miguel Guancapla", "15": "Santa Lucía",
                          "16": "Yamaranguila"}},
    "11": {"nombre": "Islas de la Bahía",
           "municipios": {"01": "Roatán", "02": "Guanaja", "03": "José Santos Guardiola", "04": "Utila"}},
    "12": {"nombre": "La Paz",
           "municipios": {"01": "La Paz", "02": "Aguanqueterique", "03": "Cabañas", "04": "Cane", "05": "Chinacla",
                          "06": "Guajiquiro", "07": "Lauterique", "08": "Marcala", "09": "Mercedes de Oriente",
                          "10": "Opatoro", "11": "San Antonio del Norte", "12": "San José", "13": "San Juan",
                          "14": "San Pedro de Tutule", "15": "Santa Ana", "16": "Santa Elena", "17": "Santa María",
                          "18": "Santiago de Puringla", "19": "Yarula"}},
    "13": {"nombre": "Lempira",
           "municipios": {"01": "Gracias", "02": "Belén", "03": "Candelaria", "04": "Cololaca", "05": "Erandique",
                          "06": "Gualcince", "07": "Guarita", "08": "La Campa", "09": "La Iguala", "10": "Las Flores",
                          "11": "La Unión", "12": "La Virtud", "13": "Lepaera", "14": "Mapulaca", "15": "Piraera",
                          "16": "San Andrés", "17": "San Francisco", "18": "San Juan Guarita",
                          "19": "San Manuel Colohete", "20": "San Rafael", "21": "San Sebastián", "22": "Santa Cruz",
                          "23": "Talgua", "24": "Tambla", "25": "Tomalá", "26": "Valladolid", "27": "Virginia",
                          "28": "San Marcos de Caiquín"}},
    "14": {"nombre": "Ocotepeque",
           "municipios": {"01": "Nueva Ocotepeque", "02": "Belén Gualcho", "03": "Concepción", "04": "Dolores Merendón",
                          "05": "La Encarnación", "06": "La Labor", "07": "Lucerna", "08": "Mercedes",
                          "09": "San Fernando", "10": "San Francisco del Valle", "11": "San Jorge", "12": "San Marcos",
                          "13": "Santa Fe", "14": "Sensenti", "15": "Sinuapa"}},
    "15": {"nombre": "Olancho",
           "municipios": {"01": "Juticalpa", "02": "Campamento", "03": "Catacamas", "04": "Concordia",
                          "05": "Dulce Nombre de Culmí", "06": "El Rosario", "07": "Esquipulas del Norte",
                          "08": "Gualaco", "09": "Guarizama", "10": "Guata", "11": "Guayape", "12": "Jano",
                          "13": "La Unión", "14": "Mangulile", "15": "Manto", "16": "Salamá", "17": "San Esteban",
                          "18": "San Francisco de Becerra", "19": "San Francisco de la Paz",
                          "20": "Santa María del Real", "21": "Silca", "22": "Yocón", "23": "Patuca"}},
    "16": {"nombre": "Santa Bárbara",
           "municipios": {"01": "Santa Bárbara", "02": "Arada", "03": "Atima", "04": "Ceguaca",
                          "05": "San Jose de Colinas", "06": "Concepción del Norte", "07": "Concepción del Sur",
                          "08": "Chinda", "09": "El Níspero", "10": "Gualala", "11": "Ilama", "12": "Macuelizo",
                          "13": "Naranjito", "14": "Nuevo Celicac", "15": "Petoa", "16": "Protección",
                          "17": "Quimistán", "18": "San Francisco de Ojuera", "19": "San Luis", "20": "San Marcos",
                          "21": "San Nicolás", "22": "San Marcos", "23": "San Pedro Zacapa", "24": "San Rita",
                          "25": "San Vicente Centenario", "26": "Trinidad", "27": "Las Vegas", "28": "Nueva Frontera"}},
    "17": {"nombre": "Valle",
           "municipios": {"01": "Nacaome", "02": "Alianza", "03": "Amapala", "04": "Aramecina", "05": "Caridad",
                          "06": "Goascorán", "07": "Langue", "08": "San Francisco de Coray", "09": "San Lorenzo"}},
    "18": {"nombre": "Yoro",
           "municipios": {"01": "Yoro", "02": "Arenal", "03": "El Negrito", "04": "El Progreso", "05": "Jocón",
                          "06": "Morazán", "07": "Olanchito", "08": "Santa Rita", "09": "Sulaco", "10": "Victoria",
                          "11": "Yorito"}}
}

usuarios = {
    "admin": "1234",
    "user1": "abcd"
}

def autenticar_usuario(usuario, contrasena):
    return usuarios.get(usuario) == contrasena

def buscar_por_identidad(identidad):
    departamento_codigo = identidad[0:2]
    municipio_codigo = identidad[2:4]
    if departamento_codigo in localidades:
        departamento = localidades[departamento_codigo]['nombre']
        if municipio_codigo in localidades[departamento_codigo]['municipios']:
            municipio = localidades[departamento_codigo]['municipios'][municipio_codigo]
            return f"Departamento: {departamento}, Municipio: {municipio}"
        else:
            return "Código de municipio no válido."
    else:
        return "Código de departamento no válido."

def buscar_municipios_por_departamento(codigo_departamento):
    if codigo_departamento in localidades:
        return localidades[codigo_departamento]['municipios']
    else:
        return "Código de departamento no válido."

def buscar_departamento_por_codigo(codigo_departamento):
    if codigo_departamento in localidades:
        return localidades[codigo_departamento]['nombre']
    else:
        return "Código de departamento no válido."

def buscar_departamento_y_municipio_por_codigo(codigo_departamento, codigo_municipio):
    if codigo_departamento in localidades:
        departamento = localidades[codigo_departamento]['nombre']
        if codigo_municipio in localidades[codigo_departamento]['municipios']:
            municipio = localidades[codigo_departamento]['municipios'][codigo_municipio]
            return f"Departamento: {departamento}, Municipio: {municipio}"
        else:
            return "Código de municipio no válido."
    else:
        return "Código de departamento no válido."

def main():
    print("Bienvenido al sistema de consulta de localidades y cálculo de edad.")

    metodo_autenticacion = input("¿Desea iniciar sesión con (1) Usuario y Contraseña o (2) Verificación Facial? (1/2): ")

    if metodo_autenticacion == "1":
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if autenticar_usuario(usuario, contrasena):
            print("Autenticación exitosa.")
        else:
            print("Autenticación fallida. Usuario o contraseña incorrectos.")
            return
    elif metodo_autenticacion == "2":
        print("Por favor, mire a la cámara para la verificación facial.")
        nombre_empleado = verificar_facial()
        if nombre_empleado:
            print(f"Bienvenido {nombre_empleado}")
        else:
            print("Verificación facial fallida. No se encontró coincidencia.")
            return
    else:
        print("Método de autenticación no válido. Intente nuevamente.")
        return

    while True:
        print("\n1. Consultar departamentos y municipios")
        print("2. Calcular edad")
        print("3. Buscar por número de identidad")
        print("4. Buscar municipios por código de departamento")
        print("5. Buscar departamento por código")
        print("6. Buscar departamento y municipio por código")
        print("7. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4, 5, 6, 7): ")

        if opcion == "1":
            print("Departamentos:")
            for codigo, departamento in localidades.items():
                print(f"{codigo}. {departamento['nombre']}")
            codigo_departamento = input("Ingrese el código del departamento para ver sus municipios: ")

            if codigo_departamento in localidades:
                print(f"Municipios de {localidades[codigo_departamento]['nombre']}:")
                for codigo_municipio, nombre_municipio in localidades[codigo_departamento]['municipios'].items():
                    print(f"{codigo_municipio}. {nombre_municipio}")
            else:
                print("Código de departamento no válido.")

        elif opcion == "2":
            anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
            edad = Utilidades.calcular_edad(anio_nacimiento)
            print(f"Su edad es: {edad} años.")

        elif opcion == "3":
            identidad = input("Ingrese su número de identidad: ")
            resultado = buscar_por_identidad(identidad)
            print(resultado)

        elif opcion == "4":
            codigo_departamento = input("Ingrese el código del departamento: ")
            resultado = buscar_municipios_por_departamento(codigo_departamento)
            if isinstance(resultado, dict):
                for codigo, municipio in resultado.items():
                    print(f"{codigo}. {municipio}")
            else:
                print(resultado)

        elif opcion == "5":
            codigo_departamento = input("Ingrese el código del departamento: ")
            resultado = buscar_departamento_por_codigo(codigo_departamento)
            print(resultado)

        elif opcion == "6":
            codigo_departamento = input("Ingrese el código del departamento: ")
            codigo_municipio = input("Ingrese el código del municipio: ")
            resultado = buscar_departamento_y_municipio_por_codigo(codigo_departamento, codigo_municipio)
            print(resultado)

        elif opcion == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
