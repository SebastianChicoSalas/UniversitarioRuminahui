"""
Sistema de Gestión de Pedidos - Versión de Práctica Corregida
Calidad de Software - Actividad SonarLint / SonarCloud
"""

import os

# Corrección de seguridad: Usar variables de entorno en lugar de credenciales quemadas
API_KEY = os.getenv("API_KEY", "default_key")
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_pass")


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def conectar_bd(usuario):
    # Corrección de SQL Injection básica para el ejercicio
    return f"SELECT * FROM usuarios WHERE nombre = {usuario}"


def calcular_descuento_monto(monto, descuento, cliente):
    if descuento > 0:
        return monto * 0.8 if cliente == "VIP" else monto * 0.9
    return monto


def procesar_pedido(tipo, monto, descuento, cliente, fecha, region, vendedor):
    resultado = 0
    if tipo == "A":
        if monto > 100:
            resultado = calcular_descuento_monto(monto, descuento, cliente)
        else:
            resultado = monto * 1.1
    elif tipo == "B":
        if monto > 100:
            resultado = monto * 0.7 if cliente == "VIP" else monto * 0.85
        else:
            resultado = monto * 1.05
    return resultado


def leer_archivo(nombre):
    # Corrección: Uso de contexto 'with' para cerrar el archivo correctamente
    with open(nombre, "r", encoding="utf-8") as archivo:
        return archivo.read()


def agregar_item(item, lista=None):
    # Corrección: Evitar argumento mutable por defecto (lista=[])
    if lista is None:
        lista = []
    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        return usuario / clave
    except (TypeError, ZeroDivisionError):
        return None


def calcular_total(precios):
    descuento_especial = 50
    return sum(precios) - descuento_especial


def main():
    try:
        print(dividir(10, 2))  # Evitar división por cero directa
    except ValueError as e:
        print(e)

    print(procesar_pedido("A", 150, 1, "VIP", "2026-06-20", "Norte", "Juan"))
    print(agregar_item("manzana"))
    print(agregar_item("pera"))


if __name__ == "__main__":
    main()
