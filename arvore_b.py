class ArvoreB:
    def __init__(self):
        self.raiz:'Pagina'
        self.m:int
        self.mm:int
    class Pagina:
        def __init__(self,mm):
                self.n = 0
                self.r(mm)
                self.p = Pagina(mm+1)