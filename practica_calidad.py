# Cambio de prueba para  GitHub Actions
"""
Sistema de Gestión de Pedidos - Versión de Práctica
Calidad de Software - Actividad SonarLint

INSTRUCCIONES:
1. Abre este archivo con SonarLint instalado en VS Code
2. Verás líneas subrayadas en amarillo/rojo - son los problemas detectados
3. Identifica al menos 5 problemas y corrígelos
4. Completa la tabla de registro que te entregó el docente
"""

import os
import json
import requests

API_KEY = "sk-test-12345abcdef67890"
DB_PASSWORD = "admin123"


def dividir(a, b):
    return a / b


def conectar_bd(usuario, password=DB_PASSWORD):
    query = "SELECT * FROM usuarios WHERE nombre = '" + usuario + "'"
    return query


def procesar_pedido(tipo, monto, descuento, cliente, fecha, region, vendedor):
    resultado = 0
    if tipo == "A":
        if monto > 100:
            if descuento > 0:
                if cliente == "VIP":
                    resultado = monto * 0.8
                else:
                    resultado = monto * 0.9
            else:
                resultado = monto
        else:
            resultado = monto * 1.1
    elif tipo == "B":
        if monto > 100:
            if descuento > 0:
                if cliente == "VIP":
                    resultado = monto * 0.7
                else:
                    resultado = monto * 0.85
            else:
                resultado = monto
        else:
            resultado = monto * 1.05
    return resultado


def leer_archivo(nombre):
    archivo = open(nombre, "r")
    contenido = archivo.read()
    return contenido


def agregar_item(item, lista=[]):
    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        resultado = usuario / clave
    except:
        pass
    return resultado


def calcular_total(precios):
    total = 0
    for p in precios:
        total = total + p
    descuento_especial = 50
    return total - descuento_especial


def main():
    print(dividir(10, 0))
    print(procesar_pedido("A", 150, 1, "VIP", "2026-06-20", "Norte", "Juan"))
    print(agregar_item("manzana"))
    print(agregar_item("pera"))


if __name__ == "__main__":
    main()
