class Item:
    def __init__(self,val:int):
        self.val:int = val

    def __eq__(self, outro:"Item"):
        return self.val == outro.val
    
    def __lt__(self,  outro:"Item") -> bool:
        if self.val < outro.val:
            return True
        return False
    
    def __str__(self):
        ret = str(self.val)
        return ret

    def compara(self, n):
        return self.val-n

class Pagina:
    def __init__(self,mm):
            self.r:["Item"] = []
            self.max_r = mm
            self.n = 0
            self.p:["Pagina"] = []
            self.max_p = mm + 1
            self.raiz:bool = False
    
    def __str__(self):
        ret = "["
        ret += str(self.r[0].val)
        for i in range(1, len(self.r)):
            ret += ", "
            ret += str(self.r[i].val)
        ret += "]" + " - Tamanho desta pagina: " + str(self.n)
        return ret

    def atualiza_n(self):
        self.n = len(self.r)    

    def verifica(self) -> bool:
        if self.raiz:
            if self.n <= self.max_r:
                for i in self.p:
                    if not self.p[i].verivica():
                        return False
                return True
            else:
                return False
        else:
            if self.n <= self.max_r and self.n >= self.max_r/2:
                for i in self.p:
                    if not self.p[i].verivica():
                        return False
                return True
            else:
                return False

class ArvoreB:
    def __init__(self,m:int):
        self.m:int = m
        self.mm:int = 2 * m
        self.raiz = Pagina(self.mm)
        self.raiz.raiz = True

    def __str__(self):
        ret = "Arvore b com m = " + str(self.m) + "\n"
        return ret

    def imprime(self):
        print(self.__str__())
        print(self.raiz.__str__())
        for i in range(len(self.raiz.p)):
            self._imprime(self.raiz.p[i])

    def _imprime(self, pag:Pagina):
        print(pag.__str__())
        for i in range(len(pag.p)):
            self._imprime(pag.p[i])

    def insere(self, reg:Item):
        if self.raiz.n < self.mm and len(self.raiz.p) == 0:
            self.raiz.r.append(reg)
            self.raiz.r.sort()  
            self.raiz.atualiza_n()
        elif len(self.raiz.p) == 0:
            self.raiz.r.append(reg)
            self.raiz.r.sort()
            self.raiz.atualiza_n()
            termo_medio = self.raiz.r[self.m]
            p1 = Pagina(self.mm)
            p2 = Pagina(self.mm)
            for i in range(self.m):
                p1.r.append(self.raiz.r[i])
            for i in range(self.m+1, self.mm+1):
                p2.r.append(self.raiz.r[i])
            for i in range(self.raiz.n):
                self.raiz.r.pop()
            self.raiz.r.append(termo_medio)
            self.raiz.atualiza_n()
            p1.atualiza_n()
            p2.atualiza_n()
            self.raiz.p.append(p1)
            self.raiz.p.append(p2)
        else:
            self._insere(reg, self.raiz)

    def _insere(self, reg:Item, pag:Pagina):
        if not pag.raiz and pag.n < self.mm and pag.n >= self.m and len(pag.p) == 0:
            pag.r.append(reg)
            pag.r.sort()  
            pag.atualiza_n()
        elif not pag.raiz and len(pag.p) == 0:
            pag.r.append(reg)
            pag.r.sort()
            pag.atualiza_n()
            termo_medio = pag.r[self.m]
            p1 = Pagina(self.mm)
            p2 = Pagina(self.mm)
            for i in range(self.m):
                p1.r.append(pag.r[i])
            for i in range(self.m, self.mm+1):
                p2.r.append(pag.r[i])
            for i in range(pag.n):
                pag.r.pop()
            pag.r.append(termo_medio)
            pag.atualiza_n()
            p1.atualiza_n()
            p2.atualiza_n()
            pag.p.append(p1)
            pag.p.append(p2)
        else:
            for i in range(pag.n):
                if reg < pag.r[i]:
                    self._insere(reg, pag.p[i])
                elif reg > pag.r[i]:
                    self._insere(reg, pag.p[i+1])
    
    def remover(self, reg:Item):
        pag = self.pesquisa(reg)
        if pag.raiz and pag.n > 1 and len(pag.p) == 0:
            for i in range(pag.n):
                if pag.r[i] == reg:
                    pag.r.pop(i)
                    pag.atualiza_n()
                    break
        elif not pag.raiz and pag.n > pag.max_r/2 and len(pag.p) == 0:
            for i in range(pag.n):
                if pag.r[i] == reg:
                    pag.r.pop(i)
                    pag.atualiza_n()
                    break
        else:
            pass
        
    def pesquisa(self, reg:Item) -> Pagina:
        if reg in self.raiz.r:
            return self.raiz
        else:
            return self._pesquisa(reg, self.raiz)

    def _pesquisa(self, reg:Item, pag:Pagina) -> Pagina:
        for i in range(len(pag.p)):
            if reg in pag.p[i].r:
                return pag.p[i]
            else:
                self._pesquisa(reg, pag.p[i])

    def giro_esquerda(self, reg:Item):
        pag = self.pesquisa(reg)
        for i in range(pag.n):
            if pag.r[i] == reg:
                break
        pag.p[i].r.append(reg)
        pag.p[i].r.sort()
        pag.p[i].atualiza_n()
        pag.r.pop(i)
        pag.r.append(pag.p[i+1].r[0])
        pag.r.sort()
        pag.atualiza_n()
        pag.p[i+1].r.pop(0)
        pag.p[i+1].r.sort()
        pag.p[i+1].atualiza_n()

    def giro_direita(self, reg:Item):
        pag = self.pesquisa(reg)
        for i in range(pag.n):
            if pag.r[i] == reg:
                break
        pag.p[i+1].r.append(reg)
        pag.p[i+1].r.sort()
        pag.p[i+1].atualiza_n()
        pag.r.pop(i)
        pag.r.append(pag.p[i].r[pag.p[i].n-1])
        pag.r.sort()
        pag.p[i].r.pop()
        pag.p[i].r.sort()
        pag.p[i].atualiza_n()

    def verifica(self) -> bool:
        return self.raiz.verifica()

#    def pesquisa(self, reg:Item, ap:Pagina) -> Item:
#        if ap is None:
#            return None
#        else:
#            i = 0
#            while (i < ap.n-1) and (reg.compara(ap.r[i]) > 0):
#                i += 1
#            if reg.compara(ap.r[i] == 0):
#               return ap.r[i]
#            elif reg.compara(ap.r[i]) < 0:
#                return self.pesquisa(reg, ap.p[i])
#            else:
#                return self.pesquisa(reg, ap.p[i+1])
#    
#    def insereNaPagina(self, ap:Pagina, reg:Item, apDir:Pagina):
#        k:int = ap.n-1
#        while (k >= 0) and reg.compara(ap.r(k) < 0):
#            ap.r[k+1] = ap.r[k]
#            ap.p[k+2] = ap.p[k+1]
#            k -= 1
#        ap.r[k+1] = reg
#        ap.p[k+2] = apDir
#        ap.n += 1
#    
#    def insere(self, reg:Item):
#        regRetorno:list[Item] = []
#        cresceu:list[bool] = []
#        apRetorno:Pagina = self.insere2(reg, self.raiz, regRetorno, cresceu)
#        if cresceu[0]:
#            apTemp = Pagina(self.mm)
#            apTemp.r[0] = regRetorno[0]
#            apTemp.p[0] = self.raiz
#            apTemp.p[1] = apRetorno
#            self.raiz = apTemp
#        else:
#            self.raiz = apRetorno
#    
#    def insere2(self, reg:Item,ap:Pagina,regRetorno:list[Item],cresceu:list[bool]) -> Pagina:
#        apRetorno:Pagina = None
#        if ap is None:
#            cresceu[0] = True
#            regRetorno[0] = reg
#        else:
#            i:int = 0
#            while (i < ap.n-1) and (reg.compara(ap.r[i]) > 0):
#                i += 1
#            if reg.compara(ap.r[i]) == 0:
#                print("Erro: Registro ja existente")
#                cresceu[0] = False
#            else:
#                if reg.compara(ap.r[i]) > 0:
#                    i += 1
#                apRetorno = self.insere2(reg, ap.p[i], regRetorno, cresceu)
#                if cresceu[0]:
#                    if ap.n < self.mm:
#                        self.insereNaPagina(ap, regRetorno[0], apRetorno)
#                        cresceu[0] = False
#                        apRetorno = ap
#                    else:
#                        apTemp = Pagina(self.mm)
#                        apTemp.p[0] = None
#                        if i <= self.m:
#                            self.insereNaPagina(apTemp, ap.r[self.mm-1], ap.p[self.mm])
#                            ap.n -= 1
#                            self.insereNaPagina(ap, regRetorno[0], apRetorno)
#                        else:
#                            self.insereNaPagina(apTemp, regRetorno[0], apRetorno)
#                        for j in range(self.m+1, self.mm):
#                            self.insereNaPagina(apTemp, ap.r[j], ap.p[j+1])
#                            ap.p[j+1] = None
#                        ap.n = self.m
#                        apTemp.p[0] = apTemp.p[self.m+1]
#                        regRetorno[0] = ap.r[self.m]
#                        apRetorno = apTemp
#        if cresceu[0]:
#            return apRetorno
#        else:
#            return ap
#