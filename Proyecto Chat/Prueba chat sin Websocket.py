import time
import random

# ======================
# Simulación de chat local
# ======================

def generar_nombre_usuario():
    return f"Usuario_{random.randint(100, 999)}"

def mostrar_historial(historial):
    print("\n📜 Historial de mensajes:")
    for mensaje in historial:
        print(mensaje)
    print()

def iniciar_chat():
    print("=== Chat Local Simulado ===")
    nombre = input("Ingresa tu nombre (ENTER para uno automático): ").strip()
    if not nombre:
        nombre = generar_nombre_usuario()
    
    print(f"\n✅ Bienvenido, {nombre}!")
    print("Escribe tus mensajes. Escribe '/salir' para cerrar el chat.\n")

    historial = []
    mostrar_historial(historial)

    while True:
        mensaje = input("> ")
        if mensaje.lower() == "/salir":
            print("🚪 Saliendo del chat.")
            break
        if mensaje.strip() == "":
            continue

        timestamp = time.strftime("%H:%M:%S")
        mensaje_formateado = f"[{timestamp}] {nombre}: {mensaje}"
        historial.append(mensaje_formateado)
        mostrar_historial(historial)

if __name__ == "__main__":
    iniciar_chat()
    