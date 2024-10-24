import socket
import threading


# def __init__(self):
#     self.servSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     self.myName = socket.gethostname()
    
class ServerChat():

    # ip no tengo que pasarla, puedo cacharla de infoSocket
    # port si tengo que pasarlo pq es el puerto donde tengo que escuchar.    
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port

    # Pongo el servidor a escuchar. Trato las excepciones. 
    # De momento escucho 1 solo cliente por vez.
    def initServidor(ip, port):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((ip, port))
            server_socket.listen(1)
            print(f"Servidor escuchando en ({ip})[{port}]")

        except socket.error as e:
            print(f"Error al iniciar el servidor: {e}")
            return

        # Si llega una solicitud de conexion de algún cliente entra por aquí
        while True:
            try:
                cnx, ipCliente = server_socket.accept()            
                print(f"Conectado a ({ipCliente})[{port}] ")
            except socket.error as e:
                print(f"Error en Aceptar conexión:\nMensaje Error: {e}")
                continue

            # ----- Manejo de la conexión de cliente -----
            # Tiene que ser While True pq si se envía un archivo o un mensaje largo, se enviaría en 
            # varios paquetes de 1024(averiguar otras cantidades)
            while True:
                try:
                    data = cnx.recv(1024).decode()
                    # if not data:
                    # Si el cliente envía <<>> es que quiere desconectar ordenadamente.
                    # Tb puede desconectar a lo bruto(cerrando programa), por lo que cacharía excepcion.
                    if data =='<<>>':
                        print(f"Conexion Cerrada X Cliente {ipCliente}")
                        break
                    else:
                        print(f"Recibido de {ipCliente} <<< {data}")
                except ConnectionResetError:
                    print("El Cliente cerró inesperadamente la conexión.")
                    break
                except socket.error as e:
                    print(f"Error al recibir datos de {ipCliente}: {e}")    
                    break

        # Cierra la Conexion con el cliente, 
        # pero el servidor no deja de querer escuchar.??       
        cnx.close()

    # Iniciar el servidor en un hilo
    def indexServer(self, ip, port):
        server = threading.Thread(target=self.initServidor, args=(ip, port))
        server.start()
        server.join()


