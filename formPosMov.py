import tkinter
class FormPosMov():
    """ 
    Def: Clase que define un formulario tKinter para hacer una doble conexion cliente-servidor
    con sockets para poder enviar mensajes de texto y archivos y emojis en una red local.
    """
    coorX=0
    coorY=0
    esExpandido=False       # Booleano para indicar si la ventana (formulario) está visible o escondido.
    VISIBLEPIX=40           # Cuanto espacio visible de la ventana quiero cuando esté cerrada.
    PADX=10                 # Espacio entre el limite derecho de la pantalla y la ventana
    PADY=100                # Desde la parte inferior de la pantalla al borde inferior de la ventana
    # ____________________________
    # ==== Constructor de la clase
    def __init__(self, root, ancho=300, alto=150, posY=None):
        """ 
        Def: Constructor de la clase FormPosMov()
        Args:
        [root]: ventana instanciada
        [ancho=300]: ancho de la ventana por defecto
        [alto=300]: alto de la ventana por defecto
        [posY]=None: posicion Y inicial(altura) de la ventana. Si se pasa None, situa la ventana a 100px de la esquina derecha abajo.
        """
        self.root = root        
        # ==== Tamaño (ventana) xa geometry >>>
        # ===================================        
        self.formWidth = ancho
        self.formHeight = alto
        # ==== Posicion (ventana) xa geometry >>>
        # ====================================
        # Obtiene el tamaño de la pantalla Xa calcular la posicion (coorX, coorY) 
        self.screenWidth  = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        pass
        # ___________
        # Calcula la posición inicial (40 píxeles visibles)
        # Configura la geometría inicial de la ventana (40 píxeles visibles en el ejeX) (derecha-Abajo-100)
        FormPosMov.coorX = self.screenWidth - 40                             # 40 píxeles visibles al inicio
        if posY==None:
            FormPosMov.coorY = self.screenHeight - self.formHeight - FormPosMov.PADY         # 100 de la barra inferior. 
        else:
            FormPosMov.coorY = posY
        pass
        # __________
        # str -> " Ancho x Alto + coordenadaX + coordenadaY "
        self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormPosMov.coorX}+{FormPosMov.coorY}')
        pass
        # ==== Movimiento 
        # =======================
        # Detecta el doble clic en la ventana para expandir o contraer
        self.root.bind('<Double-1>', self.formRoot_dblClick)
        # Al hacer doble clic, expandir o contraer la ventana
    # ___________________
    # Evento Doble Click sobre el formulario
    def formRoot_dblClick(self, event):        
        if FormPosMov.esExpandido:
            self.desplazar(mostrar_completa=False)
        else:
            self.desplazar(mostrar_completa=True)
    # ____________________
    # Mueve la ventana con el metodo de root after
    def desplazar(self, mostrar_completa=True):
        # global coorX, esExpandido
        if mostrar_completa:
            # Expande la ventana hacia el centro de la pantalla
            if FormPosMov.coorX > self.screenWidth - self.formWidth - 10:
                FormPosMov.coorX -= 10
                self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormPosMov.coorX}+{FormPosMov.coorY}')
                self.root.after(20, self.desplazar)
            else:
                FormPosMov.esExpandido = True  # Indica que la ventana está completamente expandida
        else:       # Oculta la ventana(40 píxeles visibles)            
            if FormPosMov.coorX < self.screenWidth - 40:
                FormPosMov.coorX += 10
                self.root.geometry(f'{self.formWidth}x{self.formHeight}+{FormPosMov.coorX}+{FormPosMov.coorY}')
                self.root.after(20, self.desplazar, False)
            else:
                FormPosMov.esExpandido = False  # Indica que la ventana está contraída
