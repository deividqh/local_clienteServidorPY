import threading
# import socket
import os

import tkinter as tk

# -----------------------

import clienteChat              # El cliente para enviar msg/File/emoji
import infoSocket               # El que me va a dar la informacion de la red y yo.
# import FormularioChat as FCA    # El Formulario tkinter desde donde se ejecuta todo.

import formServerAvz as  formSAvz
import formClienteAvz as formCAvz

# =====================================================
# ---- Configuración de IP y Puertos
# ---- Tengo que cachar mi ip y el puerto es cte y elegido por mi.
# ---- Tengo que cachar la red local (192.168.0.[0-255]) y mostrar los equipos
# ---- De momento esto son constantes

# IP_ServidorPC1 = '192.168.1.10'
# IP_ServidorLocal = '127.0.0.1'
IP_ServidorLocal = 'localhost'
PORT_ServerLocal = 5000

# # IP_ServidorPC2 = '192.168.1.20'
# # IP_ServidorPC2 = '127.0.0.1'
# IP_ServidorPC2 = 'localhost'
PORT_ClientePC1 = 5001


def main():

    # ============= raiz para el SERVIDOR
    rootS = tk.Tk()
    rootS.title("Formulario Servidor de Chat")

    # ============= Formulario Vacío en movimiento y posicionado 
    # import formPosMov
    # Formmove= formPosMov.FormPosMov(rootS)
    # # Borrar, solo para pruebas
    # rootS.mainloop()

    FServidor=formSAvz.FormularioServerAvanza(rootS)
    # FServidor.OpenVentanaDownRight("Servidor Creado pero no mainloop aun")    
    
    # ========= raiz para el FormCLIENTE
    rootC = tk.Tk()
    rootC.title("Formulario Cliente de Chat")    
    FCliente=formCAvz.FormularioClienteChatAvanza(rootC)

    # =================================    
    # Muestra el Formulario Cliente y servidor en hilos separados para que se ejecuten al mismo tiempo. 
    # Esto lo hago pq el Formulario Toma el Control al hacer mainloop y no puedo tener los dos a la vez.
    hiloServidor = threading.Thread(target=rootS.mainloop())
    hiloCliente  = threading.Thread(target=rootC.mainloop())

    # Esto puede no ponerse???
    hiloServidor.start()
    hiloCliente.start()

    # Esto puede no ponerse???
    hiloServidor.join()
    hiloCliente.join()

    print("The End Chat")
    # ____________________
    # rootS.mainloop()
    # rootC.mainloop()
    # ____________________
    # Hasta que no se cierra el formulario no se ejecuta este código.
    # Y Cada ventana Toma el Control (Luego se ejecuta una después de la otra)
    # app.OpenVentanaUpRight("Que Pacha!!")
    # app.OpenVentanaDownRight("Que Que Pacha!!")
# ====================================================================



# Uso obtener ip
# ip_local, nombreHost = obtener_ip_local()
# print(f"Nombre host: {nombreHost} \nIP local :{ip_local}")
# ******************************

if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main()
    
