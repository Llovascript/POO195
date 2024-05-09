class Mes:
    def __init__(self):
        self.meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
                      "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

    def obtener_nombre(self, numero):
        try:
            mes = self.meses[numero - 1]
            return mes
        except:
            return "numero invalido"
