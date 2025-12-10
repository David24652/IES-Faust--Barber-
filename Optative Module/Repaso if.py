#_*_ coding: utf-8 _*_
print("\tEjercicio notas")
print("----------------------------------")

nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("\nIntroduce la segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Has suspendido")
    print(f"Has sacado un {media:.0f}")
elif media >= 5 and media < 6:
    print("Has aprobado")
    print(f"Has sacado un suficiente: {media:.0f}")
elif media >= 6 and media < 7:
    print("Has aprobado")
    print(f"Has sacado un bien: {media:.0f}")
elif media >= 7 and media < 8:
    print("Has aprobado")
    print(f"Has sacado un notable: {media:.0f}")
elif media >= 8 and media < 9:
    print("Has aprobado")
    print(f"Has sacado un excelente: {media:.0f}")
elif media == 10:
    print("Has aprobado")
    print(f"Has sacado un sobresaliente: {media:.0f}")
elif nota2 >= 8:
    print("Has aprobado por sacar un 8 en el segundo examen")
    print(f"Has sacado un: {nota2:.0f}")