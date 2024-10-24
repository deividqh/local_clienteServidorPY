import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from formPosMov import FormPosMov
# _____________________
# Para enviar parametros al command y bind
# from functools import partial
# -----------------------
class FormularioServerAvanza():
# class FormularioServerAvanza(FormPosMov):
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """
    coorX=0
    coorY=0
    esExpandido=False
    def __init__(self, root, title="Formulario Servidor de Chat", ancho=300, alto=150):
        self.root = root
        self.root.title(title)
        
        # super().__init__(self.root,300, 150)

        # Configurar que el Frame se expanda con la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # ==========================
        # ==== Tamaño y Posicion >>>
        # ==========================
        # Tamaño del Formulario(ventana) Servidor xa geometry
        self.formWidth = ancho
        self.formHeight = alto

        # Obtiene el tamaño de la pantalla Xa calcular la posicion (coorX, coorY) 
        self.screenWidth  = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        # Calcula la posición inicial (40 píxeles visibles)
        # Configura la geometría inicial de la ventana (40 píxeles visibles en el ejeX) (derecha-Abajo-100)
        FormularioServerAvanza.coorX = self.screenWidth - 40                             # 40 píxeles visibles al inicio
        FormularioServerAvanza.coorY = self.screenHeight - self.formHeight - 100         # 100 de la barra inferior. 
        # ________________________
        # str -> " Ancho x Alto + coordenadaX + coordenadaY "
        root.geometry(f'{self.formWidth}x{self.formHeight}+{FormularioServerAvanza.coorX}+{FormularioServerAvanza.coorY}')
        # ==========================
        # ==== Tamaño y Posicion ]]]
        # ==========================
        # __________________________________
        # Detecta el doble clic en la ventana para expandir o contraer
        root.bind('<Double-1>', self.formRoot_dblClick)

        # *************************************************************************
        # ----- WIDGETS DE FRAME SERVIDOR(El que muestra lo que le envian)
        # *************************************************************************
        self.frameServidor=tk.Frame(root,name="frameservidor")     

        # self.frameServidor.grid_columnconfigure(0, weight=1)
        # self.frameServidor.grid_rowconfigure(0, weight=1)        
        self.frameServidor.pack()

        # ====================================
        # ----- widgets PARA EL FRAME SERVIDOR(El que recibe mensajes o Archivos de otro Pc)
        # self.lbxMensajesRecibidos=tk.Listbox(self.frameServidor, width=30, height=5)
        filaServer=0
        # ______________________________
        # Crear una variable de control para almacenar el estado del Checkbutton
        self.chkBttnServer_valor = tk.IntVar()  # 0 = desmarcado, 1 = marcado
        # Crear el Checkbutton y enlazar la función chkBttnServer_Check al evento de cambio
        self.chkBttnServer = tk.Checkbutton(self.frameServidor, text="Servidor Activo", 
                                                                variable=self.chkBttnServer_valor, 
                                                                command=self.chkBttnServer_Check)
        self.chkBttnServer.grid(row=filaServer, column=0 )
        # _____________________________
        filaServer=1
        self.lbxMensajesRecibidos=tk.Listbox(self.frameServidor)
        self.lbxMensajesRecibidos.grid(row=filaServer, column=0, columnspan=3 )
        # self.lbxMensajesRecibidos.grid(row=filaServer, column=0, pady=10)
        # self.lbxMensajesRecibidos.pack()
        # _____________________________
        filaServer=2
        # ----- Label para el equipo que nos conecta.
        self.lblPcCnx=tk.Label(self.frameServidor, text="Equipo X")
        self.lblPcCnx.grid(row=filaServer, column=0)
        # ----- Label para el estado de la conexión
        self.lblStCnxServ=tk.Label(self.frameServidor, text="Estado X")
        self.lblStCnxServ.grid(row=filaServer, column=1)          
        
        
        # Hilos para el cliente y servidor
        # self.hiloServidorChat = threading.Thread(target=servidorChat.indexServer, args=(IP_ServidorPC1, PORT_ServerPC1))
        # self.hiloServidorChat.start()
        # No tengo que esperar a que el hilo de servidor Termine?
        # self.hiloServidorChat.join()

        

    # ==================================    
    # METODOS FUNDAMENTALES DE SERVIDOR (Es el receptor de mensajes y archivos)
    # ----------------------------------
    def recibirMsg():
        messagebox.showinfo("Recibir Msg")
        pass
    def recibirArchivo():
        messagebox.showinfo("Recibir Archivo\nMostrar nombreArchivo\n1-BtnGuardar Archivo\n2-BtnVer Archivo en RAM")
        pass
    def recibirEmoji():
        messagebox.showinfo("Archivo Seleccionado", f"Has seleccionado: {archivo}")
        pass
    # ____________________
    # Función que manejará el evento de cambio en el Checkbutton
    # Tiene que poner el Servidor en escucha
    def chkBttnServer_Check(self):
        if self.chkBttnServer_valor.get() == 1:  # Si el Checkbutton está marcado
            print("""1- Aqui tengo que crear un hilo Xa el socketServidor Xa Independizar el servidor del Formulario
2- Tengo que ponerlo en escucha.
3- Notificarlo en el Formulario con un semaforo Canvas(este me gusta)
                     """)
        else:
            print("""1- Notificar al cliente que corto la Conexion
2- Cortar la Conexion o Matar el hilo del socket.
3- Notificar en el Formulario con un Semaforo.
                """)
    
    # =======================    
    # ACCIONES COMUNES
    # ------------------------
    # ___________________
    # Al hacer doble clic, expandir o contraer la ventana
    def formRoot_dblClick(self, event):
        if FormularioServerAvanza.esExpandido:
            self.desplazaFormRoot(mostrar_completa=False)
        else:
            self.desplazaFormRoot(mostrar_completa=True)
    # ____________________
    # Mueve la ventana con el metodo de root after
    def desplazaFormRoot(self, mostrar_completa=True):
        # global coorX, esExpandido
        if mostrar_completa:
            # Expande la ventana hacia el centro de la pantalla
            if FormularioServerAvanza.coorX > self.screenWidth - self.formWidth - 10:
                FormularioServerAvanza.coorX -= 10
                self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormularioServerAvanza.coorX}+{FormularioServerAvanza.coorY}')
                self.root.after(20, self.desplazaFormRoot)
            else:
                FormularioServerAvanza.esExpandido = True  # Indica que la ventana está completamente expandida
        else:
            # Contrae la ventana de nuevo hacia los 40 píxeles visibles
            if FormularioServerAvanza.coorX < self.screenWidth - 40:
                FormularioServerAvanza.coorX += 10
                self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormularioServerAvanza.coorX}+{FormularioServerAvanza.coorY}')
                self.root.after(20, self.desplazaFormRoot, False)
            else:
                FormularioServerAvanza.esExpandido = False  # Indica que la ventana está contraída


    def closeConection_click(self):      
        """     
        Def: Cierra una conexion
        """
        messagebox.showinfo("Conexión", "Conexión cortada.")
    # --------------------------

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

