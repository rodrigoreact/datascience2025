import random
import string

def generar_contraseña(longitud=12):
    """Genera una contraseña segura de la longitud especificada."""
    if longitud < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("🔐 Generador de Contraseñas Seguras")
    try:
        longitud = int(input("Ingrese la longitud de la contraseña (mínimo 6): "))
        contraseña = generar_contraseña(longitud)
        print(f"\nTu contraseña generada es:\n👉 {contraseña}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
