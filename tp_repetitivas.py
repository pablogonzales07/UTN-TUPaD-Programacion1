# Ejercicio 1 ==> "Caja del Kiosco"
while True:
    nombre_cliente = input("Ingrese su nombre ==> ")
    if nombre_cliente.isalpha():
        break

    print("Ingrese solo letras")

while True:
    cantidad_productos = input("Ingrese cantidad de productos a comprar ==> ")
    if cantidad_productos.isdigit() and int(cantidad_productos) > 0:
        cantidad_productos = int(cantidad_productos)
        break

    print("Ingrese un numero entero positivo")

total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0

for producto in range(1, cantidad_productos + 1):
    while True:
        precio = input(f"Ingrese precio del producto {producto} ==> ")
        if precio.isdigit() and int(precio) > 0:
            precio = int(precio)
            break
        print("Precio invalido")

    while True:
        descuento = input("El producto tiene descuento? (S/N) ==> ").lower()
        if descuento == "s" or descuento == "n":
            break
        print("Ingrese una respuesta valida")

    total_sin_descuento += precio

    if descuento == "s":
        precio_final = precio * 0.90
        ahorro_total += precio - precio_final
    else:
        precio_final = precio

    total_con_descuento += precio_final

promedio = total_con_descuento / cantidad_productos

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2 ==> "Acceso al Campus y Menu Seguro"
USUARIO = "alumno"
CONTRASEÑA = "python123"

intentos_usuario = 1
intentos_maximos = 3

while intentos_usuario <= intentos_maximos:
    print(f"Intento {intentos_usuario}/{intentos_maximos}  ")
    usuario_ingresado = input("Ingrese su usuario ==> ")
    contraseña_ingresada = input("Ingrese su contraseña ==> ")
    print(usuario_ingresado)
    print(len(contraseña_ingresada) * "X")
    if usuario_ingresado != USUARIO or contraseña_ingresada != CONTRASEÑA:
        print("Usuario o contraseña incorrectos")
        intentos_usuario += 1
        if intentos_usuario > 3:
            print("Cuenta bloqueada")
            break
        continue
    else:
        print("Acceso concedido")

        while True:
            print("1_ Ver estado de inscripcion")
            print("2_ Cambiar Clave")
            print("3_ Mostrar mensaje motivacional")
            print("4_ Salir")

            opcion_usuario = input("¿Que accion desea realizar? ==> ")
            if opcion_usuario.isdigit() and 1 <= int(opcion_usuario) <= 4:
                match opcion_usuario:
                    case "1":
                        print("Inscripto")
                    case "2":
                        nueva_contraseña = input("Ingrese su nueva contraseña ==> ")
                        confirmacion_contraseña = input("Confirme nueva contraseña ==> ")

                        if len(nueva_contraseña) < 6:
                            print("La contraseña debe tener minimamente 6 caracteres")
                        elif nueva_contraseña != confirmacion_contraseña:
                            print("ERROR: Las contraseñas no coinciden")
                        else:
                            print("Contraseña actualizada con exito")
                            CONTRASEÑA = nueva_contraseña
                    case "3":
                        print("Cada paso cuenta, seguí adelante.")
                    case "4":
                        print("Hasta la proxima")
                        break
            else:
                print("Opcion invalida")
    break

# Ejercicio 3 ==> "Agenda de Turnos con Nombres (sin listas)"

while True:
    nombre_operador = input("Ingrese nombre del operador ==> ")
    if nombre_operador.isalpha():
        break
    print("Ingrese solo letras")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("1_ Reservar Turno")
    print("2_ Cancelar turno")
    print("3_ Ver agenda del dia")
    print("4_ Ver resumen general")
    print("5_ Cerrar el sistema")

    while True:
        opcion_usuario = input("Seleccione una opcion ==> ")
        if (
            opcion_usuario.isdigit()
            and opcion_usuario in ("1", "2", "3", "4", "5")
        ):
            break
        print("Opcion invalida")

    match opcion_usuario:
        case "1":
            while True:
                dia_elegido = input(
                    "Seleccione el dia: 1 = Lunes -- 2 = Martes ==> "
                )
                if dia_elegido.isdigit() and 1 <= int(dia_elegido) <= 2:
                    break
                print("Opcion Invalida")

            while True:
                nombre_paciente = input(
                    "Ingrese nombre del paciente ==> "
                ).lower()

                if nombre_paciente.isalpha():
                    break

                print("Nombre invalido")

            paciente_repetido = False

            # Valido si ya tiene una reserva realizada
            if dia_elegido == "1" and lunes1 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "1" and lunes2 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "1" and lunes3 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "1" and lunes4 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "2" and martes1 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "2" and martes2 == nombre_paciente:
                paciente_repetido = True
            elif dia_elegido == "2" and martes3 == nombre_paciente:
                paciente_repetido = True

            if paciente_repetido:
                print("Ya tiene una reserva en este dia")

            else:
                # Cargo en el primer lugar disponible
                if dia_elegido == "1" and lunes1 == "":
                    lunes1 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "1" and lunes2 == "":
                    lunes2 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "1" and lunes3 == "":
                    lunes3 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "1" and lunes4 == "":
                    lunes4 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "2" and martes1 == "":
                    martes1 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "2" and martes2 == "":
                    martes2 = nombre_paciente
                    print("Turno reservado")
                elif dia_elegido == "2" and martes3 == "":
                    martes3 = nombre_paciente
                    print("Turno reservado")
                else:
                    print("No hay turnos disponibles para ese dia")

        case "2":
            while True:
                dia_elegido = input(
                    "Seleccione el dia: 1 = Lunes -- 2 = Martes ==> "
                )

                if dia_elegido.isdigit() and 1 <= int(dia_elegido) <= 2:
                    break

                print("Opcion Invalida")

            while True:
                nombre_paciente = input(
                    "Ingrese nombre del paciente ==> "
                ).lower()

                if nombre_paciente.isalpha():
                    break

                print("Nombre invalido")

            if dia_elegido == "1" and lunes1 == nombre_paciente:
                lunes1 = ""
                print("Turno cancelado")
            elif dia_elegido == "1" and lunes2 == nombre_paciente:
                lunes2 = ""
                print("Turno cancelado")
            elif dia_elegido == "1" and lunes3 == nombre_paciente:
                lunes3 = ""
                print("Turno cancelado")
            elif dia_elegido == "1" and lunes4 == nombre_paciente:
                lunes4 = ""
                print("Turno cancelado")
            elif dia_elegido == "2" and martes1 == nombre_paciente:
                martes1 = ""
                print("Turno cancelado")
            elif dia_elegido == "2" and martes2 == nombre_paciente:
                martes2 = ""
                print("Turno cancelado")
            elif dia_elegido == "2" and martes3 == nombre_paciente:
                martes3 = ""
                print("Turno cancelado")
            else:
                print("Usted no tiene una reserva activa")

        case "3":
            while True:
                dia_elegido = input(
                    "Seleccione el dia: 1 = Lunes -- 2 = Martes ==> "
                )

                if dia_elegido.isdigit() and 1 <= int(dia_elegido) <= 2:
                    break

                print("Opcion Invalida")

            if dia_elegido == "1":
                print(f"Turno 1: {'(libre)' if lunes1 == '' else lunes1}")
                print(f"Turno 2: {'(libre)' if lunes2 == '' else lunes2}")
                print(f"Turno 3: {'(libre)' if lunes3 == '' else lunes3}")
                print(f"Turno 4: {'(libre)' if lunes4 == '' else lunes4}")
            else:
                print(f"Turno 1: {'(libre)' if martes1 == '' else martes1}")
                print(f"Turno 2: {'(libre)' if martes2 == '' else martes2}")
                print(f"Turno 3: {'(libre)' if martes3 == '' else martes3}")

        case "4":
            ocupados_lunes = 0
            ocupados_martes = 0

            if lunes1:
                ocupados_lunes += 1
            if lunes2:
                ocupados_lunes += 1
            if lunes3:
                ocupados_lunes += 1
            if lunes4:
                ocupados_lunes += 1

            if martes1:
                ocupados_martes += 1
            if martes2:
                ocupados_martes += 1
            if martes3:
                ocupados_martes += 1

            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print(
                f"Lunes: Turnos ocupados: {ocupados_lunes} -- "
                f"Turnos disponibles: {disponibles_lunes}"
            )

            print(
                f"Martes: Turnos ocupados: {ocupados_martes} -- "
                f"Turnos disponibles: {disponibles_martes}"
            )

            if ocupados_lunes > ocupados_martes:
                print("El dia mas ocupado es el Lunes")
            elif ocupados_lunes < ocupados_martes:
                print("El dia mas ocupado es el Martes")
            else:
                print("Empate")

        case "5":
            print("Hasta Luego")
            break

# Ejercicio 4 ==> "Escape Room: La Bóveda"
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

while True:
    nombre_agente = input("Ingrese nombre del agente ==> ")
    if nombre_agente.isalpha():
        break
    print("Dato incorrecto")

cerradura_forzada = 0

while True:
    print(
        f"ESTADO: energia={energia} -- tiempo={tiempo} -- "
        f"cerraduras_abiertas={cerraduras_abiertas} -- "
        f"alarma={'ACTIVADA' if alarma else 'DESACTIVADA'} -- "
        f"codigo={codigo_parcial}"
    )
    print("1_Forzar cerradura")
    print("2_Hackear panel")
    print("3_Descansar")

    # Se valida que el usuario elija una opcion valida
    while True:
        opcion_usuario = input("Elija una opcion ==> ")
        if opcion_usuario.isdigit() and (opcion_usuario in ("1", "2", "3")):
            break
        print("Elija una opcion valida")


    match opcion_usuario:
        case "1":
            energia -= 20
            tiempo -= 2
            cerradura_forzada += 1

            if cerradura_forzada == 3:
                alarma = True
                print("Se trabo la cerradura")
            else:
                if energia < 40 and not alarma:
                    while True:
                        opcion_alarma = input("Elija una opcion (1 - 3)")
                        if (
                            opcion_alarma.isdigit()
                            and opcion_alarma in ("1", "2", "3")
                        ):
                            break
                        print("Elija una opcion valida")
                    if opcion_alarma == "3":
                        alarma = True

                if not alarma:
                    cerraduras_abiertas += 1
        case "2":
            energia -= 10
            tiempo -= 3
            cerradura_forzada = 0

            for _ in range(4):
                codigo_parcial += "A"
                print(codigo_parcial)

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1

        case "3":
            tiempo -= 1
            energia += 15
            cerradura_forzada = 0

            if energia > 100:
                energia = 100

            if alarma:
                energia -= 10

    if cerraduras_abiertas == 3 and tiempo > 0 and energia > 0:
        print("VICTORIA")
        break
    elif alarma and tiempo <= 3:
        print("Sistema Bloqueado")
        print("DERROTA")
        break
    elif energia <= 0 or tiempo <= 0:
        print("DERROTA")
        break

# Ejercicio 5 ==> "Escape Room:"La Arena del Gladiador"

# Valido nombre de gladiador
while True:
    gladiador = input("Ingrese nombre del gladiador ==> ")
    if gladiador.isalpha():
        break
    print("Error: Solo se permiten letras")

# Inicializo variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"""
            Vidas actuales ==> GLADIADOR={vida_gladiador} ENEMIGO={vida_enemigo}
            Pociones ==> {pociones_vida}
        """)
        print(f"""
            1_Ataque Pesado
            2_Rafaga Veloz
            3_Curar
        """)

        # Valido opcion usuario
        while True:
            opcion_usuario = input("Elija una accion ==> ")
            if opcion_usuario.isdigit() and opcion_usuario in ("1", "2", "3"):
                break
            print("Error: Opcion Invalida")

        # Acciones gladiador
        match opcion_usuario:
            case "1":
                if vida_enemigo < 20:
                    print("GOLPE CRITICO")
                    daño_inflijido = daño_ataque_pesado * 1.5
                else:
                    daño_inflijido = daño_ataque_pesado

                vida_enemigo -= daño_inflijido
                print(f"Atacaste al enemigo por {daño_inflijido} puntos de daño")

            case "2":
                for _ in range(3):
                    vida_enemigo -= 5
                    print("Golpe conectado por 5 de daño")

            case "3":
                if pociones_vida > 0:
                    if vida_gladiador + 30 > 100:
                        vida_gladiador = 100
                    else:
                        vida_gladiador += 30
                    pociones_vida -= 1
                else:
                    print("¡No quedan pociones!")
        turno_gladiador = False
    else:
        # Acciones enemigo
        vida_gladiador -= daño_enemigo
        turno_gladiador = True
        print(f"El enemigo te ataco por {daño_enemigo} puntos de daño")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla")
else:
    print("DERROTA. Has caido en combate")