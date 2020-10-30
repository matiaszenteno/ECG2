from tkinter import Tk, Button, Label, Toplevel, Frame, Entry, StringVar, ttk
from PIL import ImageTk, Image

#Ruta de la foto de portada
path = "landpic.jpeg"

def set_entries(frame, width, *fields_list):

    entries = dict()

    #Iteramos sobre los conjuntos de campos ingresados
    for num_field, fields in enumerate(fields_list):
        rows = list()

        #Si el conjunto de campos incluye dos columnas
        if len(fields) > 1:
            for rowindex in range(max(len(fields[0][1]),len(fields[1][1])) + 1):
                row = Frame(frame)
                row.pack(side='top', padx=5, pady=3, fill='x')
                rows.append(row)

        #Si el conjunto de campos incluye una sola columna
        else:
            for rowindex in range(len(fields[0][1]) + 1):
                row = Frame(frame)
                row.pack(side='top', padx=5, pady=3, fill='x')
                rows.append(row)

        #Seteamos los títulos para cada columna
        for titleindex in range(len(fields)):
            if (fields[titleindex][0]):
                side_row = Frame(rows[0], height=25, width=width[0])
                side_row.pack(side='left', padx=5, pady=(15,0), fill='x')
                side_row.propagate(0)

                titleLabel = Label(side_row, text=fields[titleindex][0], font='Helvetica 18 bold', anchor='w')
                titleLabel.pack(side='left')

        #Escribimos los campos para cada columna
        for column in range(len(fields)):
            for num, field in enumerate(fields[column][1]):
                complete_row = rows[num + 1]

                side_row = Frame(complete_row, height=22, width=width[0])
                side_row.pack(side='left', padx=5, fill='x')
                side_row.propagate(0)

                #Si el campo corresponde a una etiqueta con entrada
                if field[1] == 0:
                    lab = Label(side_row, width=width[1], text=field[0]+": ", anchor='w')
                    ent = Entry(side_row)

                    lab.pack(side='left')
                    ent.pack(side='left')
                    entries[field[0]] = ent

                #Si el campo corresponde a una etiqueta de solo lectura (output)
                elif field[1] == 1:
                    lab = Label(side_row, width=width[1], text=field[0]+": ", anchor='w')
                    entry_var = StringVar()
                    ent = Entry(side_row, textvariable=entry_var)
                    ent.configure(state='readonly')

                    lab.pack(side='left')
                    ent.pack(side='left')
                    entries[field[0]] = entry_var

                #Si el campo corresponde a un botón
                else:
                    startAnalysisButton = Button(side_row,
                          text = field[0],
                          command = field[1])
                    startAnalysisButton.pack(side='left', pady=1)

    return entries

def start_analysis():
    pass

def start_analysis_2():
    pass

def get_indicators():
    pass

class FirstFrame(ttk.Frame):
    
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

        self.width = [400,25]

        fields1 = [['Condiciones Iniciales', [['Temperatura Interior',0], ['Temperatura Ambiente',0], ['Temperatura Agua',0] ,['Temperatura Agua Caliente',0], ['Consumo Agua',0]]],
                  ['',[['Vida del Proyecto',0], ['Cantidad Total de Familias',0]]]]

        fields2 = [['Condiciones Colector Solar', [['Fr (tau alpha)',0], ['Fr (UL)',0], ['Área Colector Solar',0]]],
                  ['Condiciones Combustible',[['Poder Calorífico Combustible',0], ['Precio Combustible',0], ['Densidad del Combustible',0]]]]

        self.entries = set_entries(self, self.width, fields1, fields2)

        #Sección de detalle de material
        rows = list()

        for rowindex in range(2):
            row = Frame(self)
            row.pack(side='top', padx=5, pady=3, fill='x')
            rows.append(row)

        side_row = Frame(rows[0], height=25, width=self.width[0])
        side_row.pack(side='left', padx=5, pady=(15,0), fill='x')
        side_row.propagate(0)

        titleLabel = Label(side_row, text='Materiales', font='Helvetica 18 bold', anchor='w')
        titleLabel.pack(side='left')

        side_row = Frame(rows[1], height=22, width=self.width[0])
        side_row.pack(side='left', padx=5, fill='x')
        side_row.propagate(0)

        lab = Label(side_row, width=25, text='Detalles del Material'+": ", anchor='w')
        ent = ttk.Combobox(side_row, state="readonly")
        ent["values"] = ['Poliestireno Extruido', 'Poliestireno Expandido', 'Lana de Vidrio', 'Lana de Roca', 'Poliuretano', 'Paneles Sandwich', 'Corcho', 'Celulosa']

        lab.pack(side='left')
        ent.pack(side='left')

        self.entries['Detalles del Material'] = ent

        self.labelframe1 = ttk.LabelFrame(self, width=800, height=150)
        self.labelframe1.pack(side='top', anchor='w', padx=5, pady=3)

        #Botón de salida
        self.exitProgramButton = Button(self,
                            text = 'Salir del Programa',
                            command=self.root.quit,
                            bg='red')
        self.exitProgramButton.pack(side='bottom', pady='5', anchor='e')

class SecondFrame(ttk.Frame):
    
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

        self.width = [550,45]

        fields1 = [['', [['Coeficiente Convectivo Exterior (h)',0], ['Coeficiente Convectivo Interior (h)',0], ['Iniciar Análisis',self.start_analysis]]]]

        fields2 = [['Parades Paralelas', [['Resistencia a la Conducción (P)',1], ['Resistencia a la Convección Externa (P)',1], ['Resistencia a la Convección Interna (P)',1] ,['Resistencia a la Radiación (P)',1]]],
                  ['Paredes Transversales',[['Resistencia a la Conducción (T)',1] ,['Resistencia a la Convección Externa (T)',1], ['Resistencia a la Convección Interna (T)',1] ,['Resistencia a la Radiación (T)',1]]]]

        fields3 = [['Calefacción del Agua', [['Flujo Másico Agua Caliente',1] ,['Energía Necesaria para Calentar el Agua en el Día',1] ,['Energía Suministrada por Colector Solar',1] ,['Energía a Suministrar por Combustible por Familia',1], ['Energía a Suministrar por Combustible en Complejo',1]]],
                  ['Calectores Solares', [['Cantidad Colectores por Familia',1] ,['Cantidad Colectores por Complejo Habitacional',1]]]]

        self.entries = set_entries(self, self.width, fields1, fields2, fields3)

        row = Frame(self)
        row.pack(side='top', padx=5, pady=5, fill='x')

        side_row = Frame(row, height=25, width=self.width[0])
        side_row.pack(side='left', padx=5, pady=(15,0), fill='x')
        side_row.propagate(0)

        titleLabel = Label(side_row, text='Calculos Energéticos Totales', font='Helvetica 18 bold', anchor='w')
        titleLabel.pack(side='left')

        self.labelframe1 = ttk.LabelFrame(self, width=700, height=150)
        self.labelframe1.pack(side='left', anchor='w', padx=5, pady=3, fill='y')

        #Botón de salida
        self.exitProgramButton = Button(self,
                            text = 'Salir del Programa',
                            command=self.root.quit,
                            bg='red')
        self.exitProgramButton.pack(side='bottom', pady='5', anchor='e')

    def start_analysis(self):
        pass

class ThirdFrame(ttk.Frame):
    
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

        self.width = [350,20]

        fields1 = [['', [['Factor de Emisión',0],['Iniciar Análisis',self.start_analysis]]]]

        self.entries = set_entries(self, self.width, fields1)

        self.labelframe1 = ttk.LabelFrame(self, width=500, height=150)
        self.labelframe1.pack(side='top', anchor='w', padx=5, pady=3)

        self.labelframe2 = ttk.LabelFrame(self, width=500, height=150)
        self.labelframe2.pack(side='top', anchor='w', padx=5, pady=3)

        #Botón de salida
        self.exitProgramButton = Button(self,
                            text = 'Salir del Programa',
                            command=self.root.quit,
                            bg='red')
        self.exitProgramButton.pack(side='bottom', pady='5', anchor='e')

    def start_analysis(self):
        pass


class FourthFrame(ttk.Frame):
    
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

        self.width = [520,40]

        fields1 = [['Parámetros Financieros', [['Tasa de Descuento Social',0], ['Salario Ingeniería',0], ['Precio Electricidad',0], ['Obtener Indicadores',self.get_indicators]]],
                  ['',[['Vida Útil del Colector',0], ['Precio del Colector',0]]]]

        fields2 = [['Costos Financieros', [['Costo Energía',1], ['Costo Materiales',1], ['Costo Ingeniería',1]]],
                  ['Costos Combustibles',[['Costo Energía Suministrada por Colector Solar',1], ['Costo por Combustible Suministrado',1]]]]

        self.entries = set_entries(self, self.width, fields1, fields2)

        #Seccion
        row = Frame(self)
        row.pack(side='top', padx=5, pady=25, fill='x')

        side_row = Frame(row, height=22, width=self.width[0])
        side_row.pack(side='left', padx=5, fill='x')
        side_row.propagate(0)

        lab = Label(side_row, width=self.width[1], text='VAC', anchor='w')
        entry_var = StringVar()
        ent = Entry(side_row, textvariable=entry_var)
        ent.configure(state='readonly')

        lab.pack(side='left')
        ent.pack(side='left')

        self.entries['VAC'] = entry_var

        #Botón de salida
        self.exitProgramButton = Button(self,
                            text = 'Salir del Programa',
                            command=self.root.quit,
                            bg='red')
        self.exitProgramButton.pack(side='bottom', pady='5', anchor='e')

    def get_indicators(self):
        pass


class Display():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

        self.valor='GOAAAAA'

        self.initWindow = Toplevel(self.root)
        self.initWindow.title('Proyecto Gestión Energética 2')
        self.initWindow.geometry("1062x730")

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))

        self.panel = Label(self.initWindow, image = img)
        self.panel.pack(side='top', fill='x')

        self.membersLabel = Label(self.initWindow,
                          text = 'Integrantes: Claudia Fuentealba. Paola Núñez. Claudia Quilodrán. Ángela Valdés.',
                          font='Helveltica 12 bold')
        self.membersLabel.pack(pady=(15,10))

        self.initProgramButton = Button(self.initWindow,
                          text = 'Iniciar programa',
                          command=lambda: self.init_program())
        self.initProgramButton.pack(pady='5')

        self.root.mainloop()

    def init_program(self):
        self.initWindow.destroy()

        self.programWindow = Toplevel(self.root)
        self.programWindow.title('Proyecto Gestión Energética 2')
        self.programWindow.geometry("1200x700")

        self.notebook = ttk.Notebook(self.programWindow, width=1200, height=700)

        self.first_frame = FirstFrame(self, self.notebook)
        self.notebook.add(
            self.first_frame, text="Condiciones Iniciales Proyecto", padding=10)

        self.second_frame = SecondFrame(self, self.notebook)
        self.notebook.add(
            self.second_frame, text="Análisis Energético", padding=10)

        self.third_frame = ThirdFrame(self, self.notebook)
        self.notebook.add(
            self.third_frame, text="Emisiones Gases Efecto Invernadero", padding=10)

        self.fourth_frame = FourthFrame(self, self.notebook)
        self.notebook.add(
            self.fourth_frame, text="Análisis Financiero y Costos", padding=10)

        self.notebook.pack(padx=10, pady=10)

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    app = Display()