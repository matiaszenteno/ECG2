import numpy as np
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
        ent["values"] = ['Poliestireno Extruido', 'Poliestireno Expandido', 'Poliuretano', 'Corcho', 'Lana de Roca', 'Lino', 'Lana de Vidrio', 'Celulosa', 'Lana de Oveja']

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

        fields1 = [['', [['Coeficiente Convectivo Exterior (h)',0], ['Coeficiente Convectivo Interior (h)',0], ['Iniciar Análisis',self.start_analysis]]],
                  ['', [['Grosor Ventana 1 (m)',0], ['Grosor Ventana 2 (m)',0]]]]

        fields2 = [['Resistencias por Pared', [['Resistencia Pared 1',1], ['Resistencia Pared 2',1], ['Resistencia Pared 3',1] ,['Resistencia Techo',1]]],
                  ['Radiaciones por Pared', [['Radiación Pared 1',1], ['Radiación Pared 2',1], ['Radiación Pared 3',1] ,['Radiación Techo',1]]]]

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
        self.labelframe1.pack(fill="both", expand="yes")

        self.big_var = StringVar()
        self.biglabel = ttk.Label(self.labelframe1, textvariable=self.big_var)
        self.biglabel.place(x=10)

        #Botón de salida
        self.exitProgramButton = Button(self,
                            text = 'Salir del Programa',
                            command=self.root.quit,
                            bg='red')
        self.exitProgramButton.pack(side='bottom', pady='5', anchor='e')

    def start_analysis(self):
        # Temperatura ambiente
        room_temp = self.root.first_frame.entries['Temperatura Interior'].get()
        # Temperatura interior
        indoor_temp = self.root.first_frame.entries['Temperatura Ambiente'].get()
        
        # Coef. conv. exterior
        exterior_h = self.entries['Coeficiente Convectivo Exterior (h)'].get()
        # Coef. conv. interior
        interior_h = self.entries['Coeficiente Convectivo Interior (h)'].get()

        # Grosor ventana 1
        window1_thickness = self.entries['Grosor Ventana 1 (m)'].get()
        # Grosor ventana 2
        window2_thickness = self.entries['Grosor Ventana 2 (m)'].get()

        # Aislante seleccionado
        insulator = self.root.first_frame.entries['Detalles del Material'].get()

        if not (room_temp and indoor_temp and exterior_h and interior_h and window1_thickness and window2_thickness and insulator):
            return

        room_temp = float(room_temp)
        indoor_temp = float(indoor_temp)
        
        exterior_h = float(exterior_h)
        interior_h = float(interior_h)

        # Grosor y k de los distintos aislantes
        insulators_data = {'Poliestireno Extruido': [0.025, 0.12], 
                     'Poliestireno Expandido': [0.04, 0.11], 
                     'Poliuretano': [0.022, 0.09], 
                     'Corcho': [0.045, 0.015], 
                     'Lana de Roca': [0.037, 0.08], 
                     'Lino': [0.04, 0.299], 
                     'Lana de Vidrio': [0.035, 0.1], 
                     'Celulosa': [0.038, 0.16], 
                     'Lana de Oveja': [0.033, 0.08]
        }

        # Grosor distintas estructuras/materiales
        brick_thickness = 0.12
        wood_thickness = 0.05
        zinc_thickness = 0.00044
        window1_thickness = float(window1_thickness)
        window2_thickness = float(window2_thickness)
        insulator_thickness = insulators_data[insulator][1]
        
        # Área distintas estructuras/materiales
        door_area = 1.68
        window1_area = 1
        window2_area = 0.64
        wall1_area = 482
        wall2_area = 450

        # Coeficientes k para distintos materiales
        brick_k = 0.8
        wood_k = 0.13
        zinc_k = 110
        window1_k = 1
        window2_k = 1
        insulator_k = insulators_data[insulator][0]

        # Parámetros radiación
        gs = 172.4537
        brick_alpha = 0.7
        brick_e = 0.7
        zinc_alpha = 0.55
        zinc_e = 0.55
        sigma = 5.678 * (10**(-6))
        ts = (indoor_temp + room_temp)/2

        # Resistencia pared 1
        R1 = 2 * (brick_thickness/(brick_k * wall1_area)) + (insulator_thickness/(insulator_k * wall1_area))
        PR1 = 1/((1/R1) + ((window1_k * window1_area * 40)/window1_thickness) + ((window2_k * window2_area * 40)/window2_thickness) + ((wood_k * door_area * 20)/wood_thickness))
        RT1 = 1/(interior_h * (53 * 10)) + PR1 + 1/(exterior_h * (53 * 10))
        QRES1 = round((indoor_temp - room_temp)/RT1, 2)
        # Radiación pared 1
        QRAD1 = round(brick_alpha * gs * wall1_area - brick_e * sigma * (ts**4) * wall1_area, 2)
        # Q total pared 1
        QT1 = QRES1 + QRAD1

        # Resistencia pared 2
        RT2 = 1/(interior_h * (6.25 * 10)) + brick_thickness/(brick_k * (6.25 * 10)) + 1/(exterior_h * (6.25 * 10))
        QRES2 = round(2 * ((indoor_temp - room_temp)/RT2), 2)
        # Radiación pared 2
        QRAD2 = round(2 * (brick_alpha * gs * (6.25 * 10) - brick_e * sigma * (ts**4) * (6.25 * 10)), 2)
        # Q total pared 2
        QT2 = QRES2 + QRAD2

        # Resistencia pared 3
        PR3 = 1/((window1_k * window1_area * 80)/window1_thickness + 1/(brick_thickness/(brick_k * wall2_area) + insulator_thickness/(insulator_k * wall2_area) + brick_thickness/(brick_k * wall2_area)))
        RT3 = 1/(interior_h * (53 * 10)) + PR3 + 1/(exterior_h * (53 * 10))
        QRES3 = round((indoor_temp - room_temp)/RT3, 2)
        # Radiación pared 3
        QRAD3 = round(brick_alpha * gs * wall2_area - brick_e * sigma * (ts**4) * wall2_area, 2)
        # Q total pared 3
        QT3 = QRES3 + QRAD3

        # Resistencia techo
        RT4 = 1/(interior_h * (53 * 9.47)) + zinc_thickness/(zinc_k * (53 * 9.47)) + 1/(exterior_h * (53 * 9.47))
        QRES4 = round((indoor_temp - room_temp)/RT4, 2)
        # Radiación techo
        QRAD4 = round(zinc_alpha * gs * (53 * 9.47) - zinc_e * sigma * (ts**4) * (53 * 9.47), 2)
        # Q total techo
        QT4 = QRES4 + QRAD4

        self.entries["Resistencia Pared 1"].set(QRES1)
        self.entries["Resistencia Pared 2"].set(QRES2)
        self.entries["Resistencia Pared 3"].set(QRES3)
        self.entries["Resistencia Techo"].set(QRES4)

        self.entries["Radiación Pared 1"].set(QRAD1)
        self.entries["Radiación Pared 2"].set(QRAD2)
        self.entries["Radiación Pared 3"].set(QRAD3)
        self.entries["Radiación Techo"].set(QRAD4)

        self.big_var.set(f"Resistencia + Radiación Pared 1 = {QT1}\nResistencia + Radiación Pared 2 = {QT2}\nResistencia + Radiación Pared 3 = {QT3}\nResistencia + Radiación Techo = {QT4}\nQ TOTAL = {QT1+QT2+QT3+QT4}")


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
        self.initWindow.geometry("900x750")

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        base_img = Image.open(path)
        base_img = base_img.resize((900, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(base_img)
        

        self.panel = Label(self.initWindow, image = img)
        self.panel.pack(side='top', fill='x')

        self.membersLabel = Label(self.initWindow,
                          text = '*Integrantes: Claudia Fuentealba. Paola Núñez. Claudia Quilodrán. Ángela Valdés.',
                          font='Helveltica 12 bold')
        self.membersLabel.pack(pady=(30,20))

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
