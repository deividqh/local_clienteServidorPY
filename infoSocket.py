import socket
import re

class infoSocket():
    # Solo es para funcionar en red Local, con lo que se escanea esta base y 
    # se le añade el último cuadrante
    # Esto podría ser un iterable, donde se puede poner baseIP=("192.168.0.", "192.168.1.")
    # Este iterable se recoge y si es igual a la direccion base de red pasada, se completa.

    baseIP="192.168.1."

    # regIp=r'^([0-255].[0-255].[0-255].[0-255])$'
    regIp = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'


    # Nombre del Host
    hostName=''

    # esto puede ser una lista [direccion de red local, localhost, 127.0.0.1, direccion IPV4]
    ipLocal=''              

    def __init__(self, puertoScan=5000):
        infoSocket.hostName = socket.gethostname()             # Obtiene el nombre del host
        infoSocket.obtener_ip_local()
        self.puertoScan=puertoScan

    def __str__(self):
        return f'{infoSocket.hostName} ({infoSocket.ipLocal}) [{self.puertoScan}]'

    # ___________________________________
    def info(self, strDominio=None):
        # gethostbyname(): Devuelve la dirección IP de un host dado su nombre.
        # ip = socket.gethostbyname('www.google.com')
        # print(ip)
        # ip = socket.gethostbyname('www.laforjadeprometeo.com')
        # print(ip)
        ipRemota = socket.gethostbyname(strDominio)
        print(ip)
        # Si no existe provoca una excepcion que hay que tratar.(try-catch)
        # ip = socket.gethostbyname('www.lafadeproo.com')
        # print(ip)

        # settimeout(): Establece un tiempo de espera (timeout) para las operaciones del socket.
        # socket.socket.settimeout(10)  # 10 segundos de espera
        # socket.timeout = 3  # 10 segundos de espera
    
    # ______________________________________
    def getInfo(self, strDominio=None):
        # addrinfo = socket.getaddrinfo('localhost', 5000)
        # print(addrinfo)
        # addrinfo = socket.getaddrinfo('laforjadeprometeo.com', 80)
        # print(addrinfo)

        # ____________________
        # Si no existe provoca una excepcion que hay que tratar.(try-catch)
        try:
            ipRemota = socket.gethostbyname(strDominio)
            print(ip)
        except Exception as e:
            print(f'{strDominio} no encontrado.{e} - {e.__cause__}')

        # Si no existe NO provoca una excepcion. Devuelve el Error
        ipRemota=socket.gethostbyname_ex(strDominio)
        # ____________________
        # getaddrinfo(): Devuelve información sobre direcciones de red.
        addrinfo = socket.getaddrinfo(strDominio, self.puertoScan)
        print(addrinfo)        
        
        return addrinfo
    # ______________________________________
    # -- check  de un puerto----------------
    def esOpenPort(self, ip, Puerto):        
        # AF_INET       = IPV4 <-> # SOCK_STREAM   = TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Tiempo máximo de espera
        sock.settimeout(0.01)  
        # Conecta con el servidor y retorna el error o 0(conectado).
        result = sock.connect_ex((ip, Puerto))
        # Cierra la Conexion , solo queremos testear el puerto.
        # sock.close()   
             
        if result == 0:
            # print(f"El puerto {Puerto} en {ip} está abierto.")
            return True
        else:
            # print(f"El puerto {Puerto} en {ip} está cerrado o filtrado.\n{result}")
            return False
    # ______________________________________
    # -- check  de un puerto----------------
    def checkRedLocalFromTo(self, FromIP=0, ToIP=255):
        """ 
        Hace un check de las direcciones de la red en el puerto de Escucha de Servidores.        
        """        
        ipCompleta=''
        for i in range(FromIP, ToIP):
            ipCompleta=str(infoSocket.baseIP+str(i))

            if self.esOpenPort(ipCompleta, self.puertoScan):
                print(f"({ipCompleta}) [{self.puertoScan}] Abierto")
                print("Ahora tengo que meterlo en un iterable para darselo al listBox")
            else:
                print(f"({ipCompleta}) [{self.puertoScan}] Cerrado")


    def esIPValida(ip='127.0.0.1'):
        regIp = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
        if re.search(regIp, ip):
            return True
        else:
            return False

    def partirIP(ip='127.0.0.1'):
        """ 
        Def: Entra una ip y la descompongo en los 4 grupos que tiene.
        Args: [ip]: Una ip
        Return: return grupo_1, grupo_2, grupo_3, grupo_4 
        """
        regIp = r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
        if infoSocket.esIPValida():
            match = re.match(regIp, ip)
            if match:
                grupo_1 = match.group(1)
                grupo_2 = match.group(2)
                grupo_3 = match.group(3)
                grupo_4 = match.group(4)            
                return grupo_1,grupo_2, grupo_3, grupo_4
            else:
                return None
    # ------------------------------------------------------
    @classmethod
    def obtener_ip_local(cls):        
        cls.ipLocal = socket.gethostbyname(cls.hostName)   # Obtiene la dirección IP
        # return hostname, ip_local


