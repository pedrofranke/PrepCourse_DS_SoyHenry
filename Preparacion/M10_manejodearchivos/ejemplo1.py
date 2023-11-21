import sys

if len(sys.argv) ==4:
    print(f"El primer parametro es {sys.argv[1]}")
    print(f"El primer parametro es {sys.argv[2]}")
    print(f"El primer parametro es {sys.argv[3]}")
else:
    print("ERROR: no se ingresaron 3 parametros")