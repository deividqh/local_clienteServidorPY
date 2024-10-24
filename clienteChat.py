import socket

class ClienteChat():
    def __init__(self, ipRemoto, portRemoto):
        self.ipRemoto=ipRemoto
        self.portRemoto=portRemoto
        

    def initCliente(self, ip, port, max_reCnx=5, retry_delay=2, timeOut=2):
        """ 
        Def:  Incia un socket Cliente e intenta conectarse a un servidor(ip, port)
            Las caracteristicas de la conexion son opcionales y son:
            max_reCnx=5,    Numero de veces que intento reconectarme si el servidor me rechaza.
            retry_delay=2,  Retardo en sg entre intento de conexion e intento de conexion
            timeOut=2       Tiempo de retardo en Recibir la respuesta del servidor.
        """
        # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        try:
            client_socket = self.startClient_ReCnx(ip=ip, port=port, max_reCnx=5, retry_delay=2, timeOut=2)
        except ConnectionRefusedError:
            print(f"No se pudo conectar al servidor en ({ip}):[{port}]")
            return
        except socket.timeout:
            print(f"Conexión a {ip}:{port} ha expirado.")
            return
        except socket.gaierror:
            print(f"Error en la resolución de IP o nombre de host: {ip}")
            return
        # ---- Si he llegado hasta aquí, es que estoy conectado con el servidor, en el puerto.
        # Ahora hay que enviar mensajes.    
        while True:
            try:
                msgToServer = input(f"From(Me-Client) To({ip}) >> ")
                # ---- ESC de envío de mensajes
                if msgToServer.lower()=='<<>>':
                    break
                # ---- envío  mensaje
                client_socket.send(msgToServer.encode())
            except socket.error as e:
                print(f"Error al enviar datos: {e}")
                break

            try:
                # Al ser TCP, despues de que le llegue el mensaje al servidor, 
                # el servidor da una respuesta de confirmacion. Esto nos asegura que ha llegado nuestro msg.
                response = client_socket.recv(1024).decode()            
                print(f"Servidor: {response}")
            except socket.error as e:
                print(f"Error al recibir respuesta del servidor: {e}")
                break

        client_socket.close()

    # ------------------------------------
    import time

    def startClient_ReCnx(self, ip, port, max_reCnx=5, retry_delay=5, timeOut=2):
        """ 
        Def: Conecta con un servior(ip, port) con varios intentos (max_reCnx) , 
            También se establece un retardo de (retry_delay segundos ) entre reCnx y reCnx.
            Antes de enviar el mensaje esperamos x segundos(timeOut)
        Retorno: El socket Conectado 
                None si no se Puede conectar.
        """
        reCnx = 0   
        while reCnx < max_reCnx:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(timeOut)
            try:
                client_socket.connect((ip, port))
                print(f"Conectado al servidor en {ip}:{port}")
                # ---- Devuelve el socket si se conectó correctamente
                return client_socket  
            except ConnectionRefusedError as errCR:
                print(f"No se pudo conectar al servidor en ({ip}):[{port}] >> {errCR}")
            except socket.timeout as errT:
                print(f"Conexión a {ip}:{port} ha expirado\n>>> {errT}")
            except socket.gaierror as errG:
                print(f"Error en la resolución de IP o nombre de host: {ip}\n>>>{errG}")
            finally:            
                reCnx += 1
                time.sleep(retry_delay)
                print(f'>>> {reCnx}/{max_reCnx}')
        
        print(f">>> No se pudo conectar al servidor después de {max_reCnx} intentos.... Bye! ")
        return None

# Uso del cliente con reintentos
# client_socket = start_client_with_reCnx('192.168.1.6', 5001)
# if client_socket:
#     # Una vez conectado, puedes continuar enviando y recibiendo datos
#     while True:
#         msgToServer = input("Tú: ")
#         if not msgToServer:
#             break
#         client_socket.send(msgToServer.encode())
#         response = client_socket.recv(1024).decode()
#         print(f"Servidor: {response}")
