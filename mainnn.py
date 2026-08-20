def rd_stud():
    estudiantes = []
    try:
        with open("estudiantes.txt", "r") as archivo:
            for lincha in archivo:
                lincha = lincha.strip()
                if not lincha:
                    continue
                name, calf = lincha.split(",")
                calf = float(calf)
                if calf < 0 or calf > 100:
                    raise ValueError("La calificación debe estar entre 0 y 100.")
                estudiantes.append((name, calf))
    except ValueError:
        print("algo pusiste mal poser.")
    except Exception as e:
        print("pusiste esto mal. :", e)
    return estudiantes

def cal_prom(stud):
    if len(stud) == 0:
        return 0
    ttl = sum(calf for name, calf in stud)
    return ttl / len(stud)

def gen_rp(stud, prom):
    try:
        with open("reporte.txt", "w") as archive:
            for name, calf in stud:
                archive.write(f"{name},{calf:g}\n")

            archive.write(f"Promedio general: {prom:.1f}\n")
        print("Reporte generado correctamente.")
    except Exception as e:
        print("Error al generar el reporte:", e)


def agg_stud():
    try:
        name = input("Ingresa el nombre del estudiante: ")
        calf = float(input("Ingresa la calificación: "))

        if calf < 0 or calf > 100:
            print("La calificación debe estar entre 0 y 100.")
            return

        with open("estudiantes.txt", "a") as archivo:
            archivo.write(f"{name},{calf:g}\n")

        print("Estudiante agregado correctamente.")

    except ValueError:
        print("Error: La calificación debe ser un número.")
    except Exception as e:
        print("Ocurrió un error:", e)


def main():
    while True:
        print("el coso de los estudiantes")
        print("1. Mostrar estudiantes y promedio")
        print("2. Agregar estudiante")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            estudiantes = rd_stud()

            if estudiantes:
                print("\nEstudiantes:")

                for nombre, calificacion in estudiantes:
                    print(f"{nombre}: {calificacion:g}")

                promedio = cal_prom(estudiantes)

                print(f"\nPromedio general: {promedio:.1f}")

                gen_rp(estudiantes, promedio)

        elif opcion == "2":
            agg_stud()

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


main()
