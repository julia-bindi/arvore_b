class Item:
    def __init__(self,val):
        self.val = val
    
    def compara(self, n):
        return self.val-n

class ArvoreB:
    def __init__(self,m:int):
        self.raiz:Pagina
        self.m:int = m
        self.mm:int = 2 * m
    
    class Pagina:
        def __init__(self,mm):
                self.r = []
                self.max_r = mm
                self.n = len(self.r)
                self.p = []
                self.max_p = mm + 1
        
    def pesquisa(self, reg:Item, ap:Pagina) -> Item:
        if ap is None:
            return None
        else:
            i = 0
            while (i < ap.n-1) and (reg.compara(ap.r[i] > 0)):
                i += 1
            if reg.compara(ap.r[i] == 0):
               return ap.r[i]
            elif reg.compara(ap.r[i]) < 0:
                return self.pesquisa(reg, ap.p[i])
            else:
                return self.pesquisa(reg, ap.p[i+1])
    
    def insereNaPagina(self, ap:Pagina, reg:Item, apDir:Pagina):
        k:int = ap.n-1
        while (k >= 0) and reg.compara(ap.r(k) < 0):
            ap.r[k+1] = ap.r[k]
            ap.p[k+2] = ap.p[k+1]
            k -= 1
        ap.r[k+1] = reg
        ap.p[k+2] = apDir
        ap.n += 1

    def insere(self, reg:Item):
        regRetorno:list[Item]
        cresceu:list[bool]
        apRetorno:Pagina = self.insere(reg, self.raiz, regRetorno, cresceu)
        if cresceu[0]:
            apTemp = Pagina(self.mm)
            apTemp.r[0] = regRetorno[0]
            apTemp.p[0] = self.raiz
            apTemp.p[1] = apRetorno
            self.raiz = apTemp
        else:
            self.raiz = apRetorno
    
    def insere(self, reg:Item,ap:Pagina,regRetorno:list[Item],cresceu:list[bool]) -> Pagina:
        apRetorno:Pagina = None
        if ap is None:
            cresceu[0] = True
            regRetorno[0] = reg
        else:
            i:int = 0
            while (i < ap.n-1) and (reg.compara(ap.r[i]) > 0):
                i += 1
            if reg.compara(ap.r[i]) is 0:
                print("Erro: Registro ja existente")
                cresceu[0] = False
            else:
                if reg.compara(ap.r[i]) > 0:
                    i += 1
                apRetorno = self.insere(reg, ap.p[i], regRetorno, cresceu)
                if cresceu[0]:
                    if ap.n < self.mm:
                        self.insereNaPagina(ap, regRetorno[0], apRetorno)
                        cresceu[0] = False
                        apRetorno = ap
                    else:
                        apTemp = Pagina(self.mm)
                        apTemp.p[0] = None
                        if i <= self.m:
                            self.insereNaPagina(apTemp, ap.r[self.mm-1], ap.p[self.mm])
                            ap.n -= 1
                            self.insereNaPagina(ap, regRetorno[0], apRetorno)
                        else:
                            self.insereNaPagina(apTemp, regRetorno[0], apRetorno)
                        for j in range(self.m+1, self.mm):
                            self.insereNaPagina(apTemp, ap.r[j], ap.p[j+1])
                            ap.p[j+1] = None
                        ap.n = self.m
                        apTemp.p[0] = apTemp.p[self.m+1]
                        regRetorno[0] = ap.r[self.m]
                        apRetorno = apTemp
        if cresceu[0]:
            return apRetorno
        else:
            return ap
