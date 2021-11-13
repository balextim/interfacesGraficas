import tkinter
from tkinter import *
from tkinter import ttk


from modelo.gestionMatricula import Alumno


class VentanaOpciones():
    def __init__(self):
        self.ventaPrincipal=Tk()
        self.ventaPrincipal.geometry("728x600")
        self.ventaPrincipal.title("REGISTRO ALUMNO")
        self.ventaPrincipal.config(bg="#89A5C9")
        self.ventaPrincipal.resizable(width=0, height=0)
        self.frame=Frame(self.ventaPrincipal, bg="#B9DADD", width=690, height=570)
        self.frame.grid(padx=4, pady=4)
        self.frame.place(relx=.02, rely=.03)
        labelInformacionApp=Label(self.frame, text="Registro Alumnos")
        labelInformacionApp.place(relx=.30, rely=.040, relwidth=.4, relheight=.05)
        labelInformacionApp.config(bg="#89A5C9")
        labelInformacionApp.config(font=('Italic',14))
        self.tabla = ttk.Treeview(self.frame, columns=("1", "2","3","4"), height=18, selectmode="extended")
        self.tabla.heading("#0", text="DOCUMENTO")
        self.tabla.heading("#1", text="NOMBRE")
        self.tabla.heading("#2", text="APELLIDO")
        self.tabla.heading("#3", text="EDAD")
        self.tabla.heading("#4", text="CURSO")
        self.tabla.column("#0", stretch=tkinter.NO, width=120)
        self.tabla.column("#1", stretch=tkinter.NO, width=120)
        self.tabla.column("#2", stretch=tkinter.NO, width=120)
        self.tabla.column("#3", stretch=tkinter.NO, width=120)
        self.tabla.column("#4", stretch=tkinter.NO, width=120)
        self.tabla.grid(row=0, column=0, columnspan=2, padx=8, pady=8)
        self.tabla.place(relx=.07, rely=.15)
        self.botones()
        self.ventaPrincipal.mainloop()

    def botones(self):
        botonAñadir=Button(self.frame, text="AÑADIR", command=lambda:self.aniadir())
        botonAñadir.config(bg="#89A5C9")
        botonAñadir.place(relx=.07, rely=.85, relwidth=.12, relheight=.06)
        botonModificar=Button(self.frame, text="MODIFICAR", command=lambda:self.modificar())
        botonModificar.config(bg="#89A5C9")
        botonModificar.place(relx=.20, rely=.85, relwidth=.12, relheight=.06)
        botonBorrar=Button(self.frame, text="BORRAR", command=lambda:self.borrar())
        botonBorrar.config(bg="#89A5C9")
        botonBorrar.place(relx=.33, rely=.85, relwidth=.12, relheight=.06)
        botonGuardar=Button(self.frame, text="GUARDAR", command=self.guardarDocumento)
        botonGuardar.config(bg="#89A5C9")
        botonGuardar.place(relx=.82, rely=.85, relwidth=.12, relheight=.06)

    """Funcion para guardar en un documento txt"""
    def guardarDocumento(self):
        linea=""
        i=0
        for filaTabla in self.tabla.get_children():
            i+=1
            datosFila=self.tabla.item(filaTabla,option="text")
            datosFila2=self.tabla.item(filaTabla,option="values")
            lineaDocumento="Alumno " +str(datosFila)+ " | " +str(datosFila2)+ "\n"
            linea=linea+lineaDocumento
        documento=open('../documentos/registro_alumnos.txt'+str(i),'w')
        documento.writelines(linea)
        documento.close()
        labelErrores = Label(self.frame, text="DOCUMENTO GUARDADO", fg="blue")
        labelErrores.place(relx=.55, rely=.85, relwidth=.25, relheight=.06)
        labelErrores.config(bg="#B9DADD")
        labelErrores.config(font=('Italic', 10))

    def aniadir(self):
        ventanaAniadir=Tk()
        ventanaAniadir.geometry("500x400")
        ventanaAniadir.title("AÑADIR ALUMNO")
        ventanaAniadir.config(bg="black")

        """Crear una especie de ventana dentro de la venta principal"""
        frame = Frame(ventanaAniadir, bg="grey", width=480, height=380)
        frame.grid(padx=5, pady=5)
        frame.place(relx=.02, rely=.03)

        """Funcion para destruir la ventana cuando pulsas el boton volver"""
        def destroyAniadir():
            ventanaAniadir.destroy()
        def aniadirDatos():
            try:
                Label(frame, bg="#808080", font=('Italic', 8), text="",
                      fg="red").place(relx=.10, rely=.70, relwidth=.60, relheight=.07)
                self.tabla.insert("","end",text=cDocumento.get(),values=(cNombre.get(),
                                       cApellido.get(), cEdad.get(),cCurso.get()),iid=cDocumento.get())
            except:
                """Etiqueta para señalar errores"""
                Label(frame,bg="#808080",font=('Italic', 11), text="Debe rellenar los datos correctamente",
                      fg="red").place(relx=.03, rely=.70, relwidth=.65, relheight=.08)

        def comprobarDatos():
            nombre=cNombre.get()
            apellido=cApellido.get()
            edad=cEdad.get()
            documento=cDocumento.get()
            curso=cCurso.get()
            if not nombre or not apellido or not edad or not documento or not curso:
                Label(frame, bg="#808080", font=('Italic', 11), text="Debe rellenar los datos correctamente",
                      fg="red").place(relx=.03, rely=.70, relwidth=.65, relheight=.08)
            else:
                aniadirDatos()
        """creacion y configuracion de la etiqueta datos """
        labelDatos=Label(frame, text="DATOS DEL ALUMNO")
        labelDatos.place(relx=.28, rely=.05, relwidth=.50, relheight=.06 )
        labelDatos.config(font=('Italic', 14))
        labelDatos.config(bg="#A5CFF0")

        """creacion y configuracion de la etiqueta nombre """
        labelDocumento=Label(frame, text="DOCUMENTO:")
        labelDocumento.place(relx=.10, rely=.20, relwidth=.15, relheight=.06)
        labelDocumento.config(bg="#BCC2C6")
        labelDocumento.config(font=('Italic', 8))
        """Boton para recoger los datos desde la pantalla (NOMBRE)"""
        cDocumento=Entry(frame)
        cDocumento.place(relx=.28, rely=.20, relwidth=.50, relheight=.06)


        """creacion y configuracion de la etiqueta apellido """
        labelNombre = Label(frame, text="NOMBRE:")
        labelNombre.place(relx=.10, rely=.30, relwidth=.15, relheight=.06)
        labelNombre.config(bg="#BCC2C6")
        labelNombre.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (APELLIDO)"""
        cNombre = Entry(frame)
        cNombre.place(relx=.28, rely=.30, relwidth=.50, relheight=.06)


        """creacion y configuracion de la etiqueta edad """
        labelApellido = Label(frame, text="APELLIDO:")
        labelApellido.place(relx=.10, rely=.40, relwidth=.15, relheight=.06)
        labelApellido.config(bg="#BCC2C6")
        labelApellido.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (EDAD)"""
        cApellido = Entry(frame)
        cApellido.place(relx=.28, rely=.40, relwidth=.50, relheight=.06)


        """creacion y configuracion de la etiqueta documento """
        labelEdad = Label(frame, text="EDAD:")
        labelEdad.place(relx=.10, rely=.50, relwidth=.15, relheight=.06)
        labelEdad.config(bg="#BCC2C6")
        labelEdad.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (DOCUMENTO)"""
        cEdad = Entry(frame)
        cEdad.place(relx=.28, rely=.50, relwidth=.50, relheight=.06)


        """creacion y configuracion de la etiqueta curso """
        labelCurso = Label(frame, text="CURSO:")
        labelCurso.place(relx=.10, rely=.60, relwidth=.15, relheight=.06)
        labelCurso.config(bg="#BCC2C6")
        labelCurso.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (CURSO)"""
        cCurso = Entry(frame)
        cCurso.place(relx=.28, rely=.60, relwidth=.50, relheight=.06)

        """Bototon para añadir registros"""
        botonAniadir = Button(frame, text="AÑADIR", command=comprobarDatos)
        botonAniadir.place(relx=.46, rely=.85, relwidth=.15, relheight=.06)
        botonAniadir.config(font=('Italic', 8))

        """Bototon para volver a la pantalla principal"""
        botonVolver = Button(frame, text="VOLVER", command=destroyAniadir)
        botonVolver.place(relx=.63, rely=.85, relwidth=.15, relheight=.06)
        botonVolver.config(font=('Italic', 8))
        ventanaAniadir.mainloop()

    def borrar(self):
        ventanaBorrar=Tk()
        ventanaBorrar.geometry("480x245")
        ventanaBorrar.title("BORRAR ALUMNO")
        ventanaBorrar.config(bg="black")

        """Funcion para destruir la ventana cuando pulsas el boton volver"""
        def destroyBorrar():
            ventanaBorrar.destroy()
        """Funcion para borrar el registro"""

        def borrarRegistro():
            labelErrores = Label(frame, text="", fg="red")
            labelErrores.place(relx=.03, rely=.50, relwidth=.65, relheight=.08)
            labelErrores.config(bg="#808080")
            labelErrores.config(font=('Italic', 11))
            documento=cDocumento.get()
            if not documento:
                labelErrores = Label(frame, text="Debe escribir el documento", fg="red")
                labelErrores.place(relx=.03, rely=.50, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
            else:
                for fila in self.tabla.get_children():
                    if (self.tabla.item(fila)["text"]==cDocumento.get()):
                        self.tabla.delete(cDocumento.get())
                labelErrores = Label(frame, text="REGISTRO BORRADO", fg="blue")
                labelErrores.place(relx=.03, rely=.55, relwidth=.58, relheight=.06)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))

        """Funcion para buscar el registro con el documento del parametro"""
        def buscarDocumento():
            labelErrores = Label(frame, text="", fg="red")
            labelErrores.place(relx=.03, rely=.50, relwidth=.65, relheight=.08)
            labelErrores.config(bg="#808080")
            labelErrores.config(font=('Italic', 11))
            datos=cDocumento.get()
            contenidoRegistro=self.tabla.item(datos,option="values")
            labelErrores = Label(frame, text=contenidoRegistro, fg="blue")
            labelErrores.place(relx=.03, rely=.55, relwidth=.58, relheight=.06)
            labelErrores.config(bg="#808080")
            labelErrores.config(font=('Italic', 11))

        """Funcion para controlar que se escriba solo el documento"""
        def comprobarDocumento(cDocumento):
            documento=cDocumento.get()
            if (documento):
                labelErrores = Label(frame, text="", fg="red")
                labelErrores.place(relx=.03, rely=.58, relwidth=.58, relheight=.06)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
                buscarDocumento()

            else:
                labelErrores = Label(frame, text="Debe escribir el documento", fg="red")
                labelErrores.place(relx=.03, rely=.50, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))

        """Crear una especie de ventana dentro de la venta principal"""
        frame = Frame(ventanaBorrar, bg="grey", width=450, height=220)
        frame.grid(padx=2, pady=2)
        frame.place(relx=.02, rely=.04)

        """creacion y configuracion de la etiqueta datos """
        labelDatos=Label(frame, text="BORRAR ALUMNO")
        labelDatos.place(relx=.28, rely=.09, relwidth=.50, relheight=.10 )
        labelDatos.config(font=('Italic', 14))
        labelDatos.config(bg="#A5CFF0")

        """creacion y configuracion de la etiqueta nombre """
        labelDocumento=Label(frame, text="DOCUMENTO:")
        labelDocumento.place(relx=.11, rely=.35, relwidth=.15, relheight=.11)
        labelDocumento.config(bg="#BCC2C6")
        labelDocumento.config(font=('Italic', 8))
        """Boton para recoger los datos desde la pantalla (NOMBRE)"""
        cDocumento=Entry(frame)
        cDocumento.place(relx=.28, rely=.35, relwidth=.50, relheight=.11)

        """Etiqueta para señalar errores"""

        labelErrores = Label(frame, text="", fg="red")
        labelErrores.place(relx=.05, rely=.53, relwidth=.50, relheight=.11)
        labelErrores.config(bg="#808080")
        labelErrores.config(font=('Italic', 9))

        botonBuscar=Button(frame, text="BUSCAR", command=lambda:comprobarDocumento(cDocumento))
        botonBuscar.place(relx=.82,rely=.35, relwidth=.15, relheight=.11)
        botonBuscar.config(font=('Italic', 8))

        """Bototon para añadir registros"""
        botonBorrar = Button(frame, text="BORRAR", command=borrarRegistro)
        botonBorrar.place(relx=.46, rely=.65, relwidth=.15, relheight=.11)
        botonBorrar.config(font=('Italic', 8))

        """Bototon para volver a la pantalla principal"""
        botonCancelar = Button(frame, text="CANCELAR", command=destroyBorrar)
        botonCancelar.place(relx=.63, rely=.65, relwidth=.15, relheight=.11)
        botonCancelar.config(font=('Italic', 8))
        ventanaBorrar.mainloop()


    """Constructor de la clase modificar. crea una ventana para modificar los registros"""

    def modificar(self):
        ventanaModificar=Tk()
        ventanaModificar.geometry("500x400")
        ventanaModificar.title("MODIFICAR ALUMNO")
        ventanaModificar.config(bg="black")

        """Funcion para destruir la ventana cuando pulsas el boton volver"""
        def destroyModificar():
            ventanaModificar.destroy()
        def modificarDatos():
            documento=cDocumento.get()
            nombre=cNombre.get()
            apellido=cApellido.get()
            edad=cEdad.get()
            curso=cCurso.get()
            if not documento or not nombre or not apellido or not edad or not curso:
                labelErrores = Label(frame, text="Deber rellenar los todos los datos correctamente", fg="red")
                labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
            else:
                labelErrores = Label(frame, text="", fg="blue")
                labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
                for fila in self.tabla.get_children():
                    if (self.tabla.item(fila)["text"]==cDocumento.get()):
                        self.tabla.item(fila, text=cDocumento.get(), values=(cNombre.get(), cApellido.get(),cEdad.get(),cCurso.get()))
                datos = cDocumento.get()
                contenidoRegistro = self.tabla.item(datos, option="values")
                labelErrores = Label(frame, text=contenidoRegistro, fg="blue")
                labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
        """Funcion para buscar el registro con el documento del parametro"""
        def buscarDocumento():
            datos=cDocumento.get()
            contenidoRegistro=self.tabla.item(datos,option="values")
            labelErrores = Label(frame, text=contenidoRegistro, fg="blue")
            labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
            labelErrores.config(bg="#808080")
            labelErrores.config(font=('Italic', 11))
        """Funcion para controlar que se escriba solo el documento"""
        def comprobarDocumento(cDocumento,cNombre,cApellido,cEdad,cCurso):
            documento=cDocumento.get()
            nombre=cNombre.get()
            apellido=cApellido.get()
            edad=cEdad.get()
            curso=cCurso.get()
            if (documento and not nombre and not apellido and not edad and not curso):
                labelErrores = Label(frame, text="", fg="red")
                labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))
                buscarDocumento()

            else:
                labelErrores = Label(frame, text="Debe rellenar solo el campo documento", fg="red")
                labelErrores.place(relx=.03, rely=.80, relwidth=.65, relheight=.08)
                labelErrores.config(bg="#808080")
                labelErrores.config(font=('Italic', 11))

        """Crear una especie de ventana dentro de la venta principal"""
        frame = Frame(ventanaModificar, bg="grey", width=480, height=380)
        frame.grid(padx=5, pady=5)
        frame.place(relx=.02, rely=.03)

        """creacion y configuracion de la etiqueta datos """
        labelDatos=Label(frame, text="DATOS DEL ALUMNO")
        labelDatos.place(relx=.28, rely=.06, relwidth=.50, relheight=.06 )
        labelDatos.config(font=('Italic', 14))
        labelDatos.config(bg="#A5CFF0")

        """creacion y configuracion de la etiqueta nombre """
        labelDocumento=Label(frame, text="DOCUMENTO:")
        labelDocumento.place(relx=.10, rely=.25, relwidth=.15, relheight=.06)
        labelDocumento.config(bg="#BCC2C6")
        labelDocumento.config(font=('Italic', 8))
        """Boton para recoger los datos desde la pantalla (NOMBRE)"""
        cDocumento=Entry(frame)
        cDocumento.place(relx=.28, rely=.25, relwidth=.50, relheight=.06)
        """creacion y configuracion de la etiqueta apellido """
        labelNombre = Label(frame, text="NOMBRE:")
        labelNombre.place(relx=.10, rely=.35, relwidth=.15, relheight=.06)
        labelNombre.config(bg="#BCC2C6")
        labelNombre.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (APELLIDO)"""
        cNombre= Entry(frame)
        cNombre.place(relx=.28, rely=.35, relwidth=.50, relheight=.06)

        """creacion y configuracion de la etiqueta edad """
        labelApellido = Label(frame, text="APELLIDO:")
        labelApellido.place(relx=.10, rely=.45, relwidth=.15, relheight=.06)
        labelApellido.config(bg="#BCC2C6")
        labelApellido.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (EDAD)"""
        cApellido = Entry(frame)
        cApellido.place(relx=.28, rely=.45, relwidth=.50, relheight=.06)

        """creacion y configuracion de la etiqueta documento """
        labelEdad = Label(frame, text="EDAD:")
        labelEdad.place(relx=.10, rely=.55, relwidth=.15, relheight=.06)
        labelEdad.config(bg="#BCC2C6")
        labelEdad.config(font=('Italic', 9))
        """Boton para recoger los datos desde la pantalla (DOCUMENTO)"""
        cEdad =Entry(frame)
        cEdad.place(relx=.28, rely=.55, relwidth=.50, relheight=.06)

        """etiqueta informativa para la venta modificar (indica el campo que debe rellenar)"""
        labelBuscarDocumento = Label(frame, text="Introduzca el documento del alumno a modificar")
        labelBuscarDocumento.place(relx=.09, rely=.17, relwidth=.50, relheight=.06)
        labelBuscarDocumento.config(font=('Italic', 8))
        labelBuscarDocumento.config(bg="#808080")

        """creacion y configuracion de la etiqueta curso """
        labelCurso = Label(frame, text="CURSO:")
        labelCurso.place(relx=.10, rely=.65, relwidth=.15, relheight=.06)
        labelCurso.config(bg="#BCC2C6")
        labelCurso.config(font=('Italic', 9))

        """Boton para recoger los datos desde la pantalla (CURSO)"""
        cCurso = Entry(frame)
        cCurso.place(relx=.28, rely=.65, relwidth=.50, relheight=.06)

        """Etiqueta para señalar errores"""
        labelErrores = Label(frame, text="", fg="red")
        labelErrores.place(relx=.05, rely=.80, relwidth=.50, relheight=.06)
        labelErrores.config(bg="#808080")
        labelErrores.config(font=('Italic', 8))

        """Bototon para añadir registros"""
        botonModificar = Button(frame, text="MODIFICAR", command=modificarDatos)
        botonModificar.place(relx=.46, rely=.90, relwidth=.15, relheight=.06)
        botonModificar.config(font=('Italic', 8))

        """Bototon para volver a la pantalla principal"""
        botonVolver = Button(frame, text="VOLVER", command=destroyModificar)
        botonVolver.place(relx=.63, rely=.90, relwidth=.15, relheight=.06)
        botonVolver.config(font=('Italic', 8))

        """Boton para buscar el alumno por el documento"""
        botonBuscar = Button(frame, text="BUSCAR", command=lambda:comprobarDocumento(cDocumento,cNombre,cApellido,cEdad,cCurso))
        botonBuscar.place(relx=.29, rely=.90, relwidth=.15, relheight=.06)
        botonBuscar.config(font=('Italic', 8))

        ventanaModificar.mainloop()

