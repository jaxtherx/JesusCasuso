#La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
def iniciales(cadena):
    palabras = cadena.split()
    iniciales = [palabra[0] for palabra in palabras]
    return ''.join(iniciales)

print(iniciales("file transfer protocol"))