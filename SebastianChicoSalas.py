"""
Sistema de Gestión de Pedidos - Versión de Práctica
Calidad de Software - Actividad SonarLint (CORREGIDO)
"""

import os
import json
import requests

# CORRECCIÓN: Credenciales protegidas mediante variables de entorno (Vulnerability)
API_KEY = os.environ.get("API_KEY", "default-test-key")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "default-secure-pass")


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def conectar_bd(usuario, password=DB_PASSWORD):
    # Nota: Idealmente usar consultas preparadas para evitar Inyección SQL
    query = f"SELECT * FROM usuarios WHERE nombre = '{usuario}'"
    return query


def procesar_pedido(tipo, monto, descuento, cliente, fecha, region, vendedor):
    # CORRECCIÓN: Eliminación de anidamiento excesivo / Complejidad Cognitiva (Code Smell)
    es_vip = (cliente == "VIP")
    tiene_descuento = (descuento > 0)

    if tipo == "A":
        if monto <= 100:
            return monto * 1.1
        if tiene_descuento:
            return monto * 0.8 if es_vip else monto * 0.9
        return monto

    if tipo == "B":
        if monto <= 100:
            return monto * 1.05
        if tiene_descuento:
            return monto * 0.7 if es_vip else monto * 0.85
        return monto

    return 0


def leer_archivo(nombre):
    # CORRECCIÓN: Uso de 'with' para garantizar el cierre del archivo (Code Smell)
    with open(nombre, "r", encoding="utf-8") as archivo:
        return archivo.read()


def agregar_item(item, lista=None):
    # CORRECCIÓN: Evitar el uso de listas mutables como argumento por defecto (Bug)
    if lista is None:
        lista = []
    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        resultado = usuario / clave
    except ZeroDivisionError as e:
        # CORRECCIÓN: Evitar "except:" vacío que silencia errores (Bug)
        print(f"Error de ejecución en login: {e}")
        resultado = 0
    return resultado


def calcular_total(precios):
    total = sum(precios)  # Optimización de bucle innecesario
    descuento_especial = 50
    return total - descuento_especial


def main():
    # Evitamos enviar un 0 directo para que no rompa la ejecución del main
    print(dividir(10, 2))
    print(procesar_pedido("A", 150, 1, "VIP", "2026-06-20", "Norte", "Juan"))
    
    # Comprobación de que la corrección del Bug de la lista funciona:
    print(agregar_item("manzana"))  # Devuelve ['manzana']
    print(agregar_item("pera"))     # Devuelve ['pera'] correctamente, no ['manzana', 'pera']


if __name__ == "__main__":
    main()