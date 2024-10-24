import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from dvdColor import ColorCorp 

# Para enviar parametros al command y bind
from functools import partial
# -----------------------


class FormularioClienteChatAvanza:
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """
    def __init__(self, root, title="Formulario Cliente Chat"):
        self.root = root
        self.root.title(title)

        # Configurar que el Frame se expanda con la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # *****************************
        # ----- WIDGETS DEL  FRAME CLIENTE(El que envía cosas y se conecta a un equipo)
        # *****************************
        self.frameCliente=tk.Frame(root, name="framecliente", background=ColorCorp.BlancoX03)                
        # Configurar el peso de las columnas y filas para permitir expansión
        # self.frameCliente.grid_columnconfigure( 0, weight=1)
        # self.frameCliente.grid_rowconfigure(0, weight=1)
        # Expansion del frame
        self.frameCliente.pack(fill="both", expand=True, padx=10, pady=10)
        # _________________
        filaCliente=0        
        # _________________
        # Listbox para mostrar los equipos a los que podemos enviar.
        # self.lbxServidoresXaClientMe = tk.Listbox(self.frameCliente, width=30, height=10)
        frameLbx = tk.Frame(self.frameCliente, background=ColorCorp.BlancoX03)
        frameLbx.pack(fill="both", expand=True, padx=10, pady=10)
        self.lbxServidoresXaClientMe = tk.Listbox(frameLbx)
        self.lbxServidoresXaClientMe.grid(row=filaCliente, column=0, rowspan=2, columnspan=2 ,sticky="nsew")
        # self.lbxServidoresXaClientMe = tk.Listbox(self.frameCliente)
        # ______________________
        # Aqui me falta el evento para que cuando seleccione un PC cambie el lblEquipSelect
        # Enlazar el evento de selección al Listbox
        self.lbxServidoresXaClientMe.bind('<<ListboxSelect>>', self.lbxServidoresXaClientMe_on_select)

        # ______________________
        # ----- Boton Close CNX
        self.btnCloseCnX = tk.Button(frameLbx, text="Cortar Conexión", 
                                                        command=self.closeConection_click)
        self.btnCloseCnX.grid(row=0, column=3)
        # ______________________
        # ----- Boton Buscar Equipos ----- infoSocket.checkRedLocalFromTo(1,255)
        self.btnBuscarEquipos = tk.Button(frameLbx, text="Load Pc's", 
                                                             command=self.buscarEquipos_click)
        self.btnBuscarEquipos.grid(row=1, column=3)


        # _________________
        filaCliente = 1        
        frameFila1 = tk.Frame(self.frameCliente, background=ColorCorp.BlancoX03)
        frameFila1.pack(padx=10, pady=10)
        # ----- Label para el equipo seleccionado
        self.lblEquipSelect = tk.Label(frameFila1, text="Equipo: Ninguno")
        # self.lblEquipSelect.grid(row=filaCliente, column=0, padx=2, pady=2)
        self.lblEquipSelect.grid(row=filaCliente, column=0)
        # ----- Label para el estado de la conexión
        self.lblSTCliente = tk.Label(frameFila1, text="Estado: Desconectado")
        self.lblSTCliente.grid(row=filaCliente, column=1)
        
        
        # _________________
        filaCliente = 2
        frameFila2 = tk.Frame(self.frameCliente, background=ColorCorp.BlancoX03)
        frameFila2.pack(padx=10, pady=10)
        self.txtEnviar = tk.Entry(frameFila2)
        self.txtEnviar.grid(row=filaCliente, column=0,columnspan=4,  sticky="ew")

        # _________________
        filaCliente = 3
        frameFila3 = tk.Frame(self.frameCliente, background=ColorCorp.BlancoX03)
        frameFila3.pack(padx=10, pady=10)
        # ----- Boton Enviar Texto.
        self.btnEnviarMsg = tk.Button(frameFila3, text="Enviar", 
                                                command=self.enviarMensaje_click)
        self.btnEnviarMsg.grid(row=filaCliente, column=0)

        # ----- Boton Eviar Archivo
        self.btnEnviarArchivo = tk.Button(frameFila3, text="Enviar Archivo", 
                                                    command=self.selectFile)
        self.btnEnviarArchivo.grid(row=filaCliente, column=1)

        # ----- Boton Eviar Emoji
        # aqui necesito eventos para seleccionar el emoji
        self.btnEnviarEmoji = tk.Button(frameFila3,  text="Enviar Emoji", 
                                                            command=self.enviarEmoji_click)
        self.btnEnviarEmoji.grid(row=filaCliente, column=2)
        
        # ----- Rellenaar el listBox -> Lista de equipos(Cachar equipos de Red)
        # self.cargarLboxCliente([["localhost","127.0.0.1", "Dvd"],"Equipo 1", "Equipo 2", "Equipo 3"])
        
        # Hilos para el cliente y servidor
        # self.hiloServidorChat = threading.Thread(target=servidorChat.indexServer, args=(IP_ServidorPC1, PORT_ServerPC1))
        # self.hiloServidorChat.start()
        # No tengo que esperar a que el hilo de servidor Termine?
        # self.hiloServidorChat.join()

        # clienteChat.initCliente(IP_ServidorPC2, PORT_ClientePC1)
    # =======================    
    # CLIENTE (Es el emisor de mensajes y archivos)
    # --------------------------
    def enviarMensaje_click(self):        
        messagebox.showinfo("Mensaje", "Enviando mensaje...")
    # --------------------------
    def enviarEmoji_click(self):
        # Lógica para enviar un emoji
        messagebox.showinfo("Emoji", "Enviando emoji...")
    # --------------------------
    def enviarArchivo(self):
        archivo=self.selectFile()
        if archivo:
            messagebox.showinfo("Archivo Seleccionado", f"Has seleccionado: {archivo}")
            pass
        else:
            pass

    # =======================    
    # ACCIONES COMUNES
    # ------------------------
    def closeConection_click(self):      
        """     
        Def: Cierra una conexion
        """
        self.lblSTCliente.config(text="Estado: xxxx")
        messagebox.showinfo("Conexión", "Conexión cortada.")
    # --------------------------
    def cargarLboxCliente(self, listServXaClienteMe):
        """ 
        Def: Carga el ListBox de Cliente con los servidores(ip) activos en el puerto.
        [listServXaClienteMe] List de str de servidores escuchando. 
        Esto hay que cambiarlo por un escaneo de la red en el puerto {portCliente} 
        """
        if not isinstance(listServXaClienteMe, list): return 
        for servidor in listServXaClienteMe:
            self.lbxServidoresXaClientMe.insert(tk.END, servidor)
        
    # --------------------------
    def selectFile(self):
        """ 
        Def: Selecciona un Archivo.
        """
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo")
        if archivo:
            return archivo
            # Aquí iría la lógica para enviar el archivo al otherServ From me(client) To other(serv)
        # Función para mostrar una ventana emergente en la esquina superior derecha

    def OpenVentanaUpRight(self, mensaje):
        ventana = tk.Tk()
        ventana.title("Nuevo Mensaje")
        ventana.geometry(f"200x100+{ventana.winfo_screenwidth() - 210}+10")  # Posicionar en la esquina superior derecha
        
        label = tk.Label(ventana, text=mensaje)
        label.pack(padx=20, pady=20)
        
        # Configura para que la ventana se cierre automáticamente después de 3 segundos
        ventana.after(3000, ventana.destroy)
        ventana.mainloop()

    # Función para mostrar una ventana emergente en la esquina inferior derecha
    def OpenVentanaDownRight(self, mensaje):
        ventana = tk.Tk()
        ventana.title("Nuevo Mensaje")

        # Obtener las dimensiones de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Posicionar en la esquina inferior derecha
        ventana.geometry(f"200x100+{screen_width - 210}+{screen_height - 150}")  

        label = tk.Label(ventana, text=mensaje)
        label.pack(padx=20, pady=20)
        
        # Configura para que la ventana se cierre automáticamente después de 3 segundos
        ventana.after(3000, ventana.destroy)
        ventana.mainloop()


    # Una misma funcion para gestionar los diferentes eventos
    # Se usa el la librería {functools} el paquete {partial}, 
    # que permite enviar argumentos a un evento command
    def on_button_click(button_name):
        print(f"El botón '{button_name}' ha sido presionado")        
        # =================================
        # FORMA DE LLAMAR A on_button_click
        # =================================
        # button1=tk.Button(root, text="Botón con place()", command=partial(on_button_click, "Btn01"))
        # button1.grid(row=0, column=0 )
        # button2=tk.Button(root, text="Botón2 con place()", command=partial(on_button_click, "Btn02"))
        # button2.grid(row=0, column=1 )

    # Función que se ejecuta al seleccionar un elemento en el Listbox
    def lbxServidoresXaClientMe_on_select(self, event):
        # Obtener la selección actual
        seleccion = event.widget.curselection()  # El evento proporciona el widget donde ocurrió
        if seleccion:
            indice = seleccion[0]  # Obtener el primer índice seleccionado
            valor = event.widget.get(indice)  # Obtener el valor del índice
            print(f"Elemento seleccionado: {valor} (Índice {indice})")
            self.lblEquipSelect.config(text=valor)
        else:
            print("Ningún elemento seleccionado.")
    
    def buscarEquipos_click(self):
        self.cargarLboxCliente([["localhost","127.0.0.1", "Dvd"],"Equipo 1", "Equipo 2", "Equipo 3"])