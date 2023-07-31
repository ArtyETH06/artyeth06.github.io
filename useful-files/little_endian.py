import sys

def hex_to_little_endian(hex_string):
    # Supprime le préfixe "0x" de la chaîne hexadécimale si présent
    hex_string = hex_string.replace("0x", "")

    # Vérifie que la longueur de la chaîne est paire (nombre pair d'octets)
    if len(hex_string) % 2 != 0:
        raise ValueError("Invalid hex string. The length must be even.")

    # Convertit la chaîne hexadécimale en une séquence d'octets
    byte_sequence = bytes.fromhex(hex_string)

    # Inverse la séquence d'octets pour obtenir le format Little Endian
    little_endian_bytes = byte_sequence[::-1]

    # Formatte la séquence d'octets avec "\x" tous les deux caractères
    formatted_bytes = b"".join([b"\\x" + format(byte, "02x").encode() for byte in little_endian_bytes])

    return formatted_bytes

if __name__ == "__main__":
    # Vérifie si l'option -s et la chaîne hexadécimale sont spécifiées en ligne de commande
    if len(sys.argv) != 3 or sys.argv[1] != "-s":
        print("Usage: python script.py -s <hex_string>")
        sys.exit(1)

    # Récupère la chaîne hexadécimale passée en argument
    hex_string = sys.argv[2]

    try:
        # Appelle la fonction de conversion et affiche le résultat
        little_endian_result = hex_to_little_endian(hex_string)
        print("Input Hex String:", hex_string)
        print("Little Endian Bytes:", little_endian_result.decode())
    except ValueError as e:
        print("Error:", e)
