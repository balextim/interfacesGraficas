
class Alumno():
    listaAlumnos=[]
    def __init__(self, nombre="", apellido="", edad=0, documento="", curso=1):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
        self.__documento=documento
        self.__curso=curso

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido

    def getedad(self):
        return self.__edad

    def getdocumento(self):
        return self.__documento

    def getcurso(self):
        return self.__curso

    def setnombre(self, nombre):
        self.__nombre=nombre

    def setapellido(self, apellido):
        self.__apellido=apellido

    def setedad(self, edad):
        self.__edad=edad

    def setdocumento(self, docuemto):
        self.__documento=docuemto

    def setcurso(self, curso):
        self.__curso=curso

    def tostring(self):
        return "Nombre:" + str(self.__nombre)+ " Apellido:" +str(self.__apellido)+ " Edad:" +str(self.__edad)+ " Documento:" +str(self.__documento)+ " Curso:" +str(self.__curso)


