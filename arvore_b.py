class Item:                                                          #Classe a ser inserido das páginas da árvore
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
        return self.val-n.val

class Pagina:                                                        #Desrive o comportamento de uma página da árvore
    def __init__(self,mm):
            self.r:["Item"] = []
            self.max_r = mm
            self.n = 0
            self.p:["Pagina"] = []
            self.max_p = mm + 1
            self.raiz:bool = False
    
    def __str__(self):
        if self.n > 0:
            ret = "["
            ret += str(self.r[0].val)
            for i in range(1, len(self.r)):
                ret += ", "
                ret += str(self.r[i].val)
            ret += "]" + " - Tamanho desta pagina: " + str(self.n)
            return ret
    
    def __eq__(self, outro:"Pagina"):
        for i in range(self.n):
            if self.r[i] != outro.r[i]:
                return False
        return True

    def atualiza_n(self):
        self.n = len(self.r)

    def verifica(self) -> bool:                                           #Faz uma chamada recursiva para verifica se a árvore 
        if self.raiz:                                                     #está seguindo os padrões especificados
            if self.n <= self.max_r:
                for i in range(len(self.p)):
                    if not(self.p[i].verifica()):
                        return False
                return True
            else:
                return False
        else:
            if self.n <= self.max_r and self.n >= self.max_r/2:
                for i in range(len(self.p)):
                    if not(self.p[i].verifica()):
                        return False
                return True
            else:
                return False
    
    def procura(self) -> "Pagina":                                          #Retorna uma página que não esteja seguindo a regra de 
        if not self.raiz and self.n < self.max_r/2:                       #su existência dentro de uma árvore do tipo b
            return self
        else:
            for i in range(len(self.p)):
                 ret = self.p[i].procura()
                 if ret != None:
                     return ret

class ArvoreB:
    def __init__(self,m:int):
        self.m:int = m
        self.mm:int = 2 * m
        self.raiz = Pagina(self.mm)
        self.raiz.raiz = True

    def __str__(self):
        ret = "Arvore b com m = " + str(self.m) + "\n"
        return ret

    def imprime(self):                                                    #Imprime toda a árvore
        print(self.__str__())
        print(self.raiz.__str__())
        for i in range(len(self.raiz.p)):
            self._imprime(self.raiz.p[i])

    def _imprime(self, pag:"Pagina"):
        print(pag.__str__())
        for i in range(len(pag.p)):
            self._imprime(pag.p[i])

    def insere(self, reg:"Item"):                                         #Insere um elemento do tipo Item na árvore
        if self.raiz.n < self.mm and len(self.raiz.p) == 0:               #caso: inserção na raiz
            self.raiz.r.append(reg)                                       #           ou
            self.raiz.r.sort()                                            #      inserção em uma folha sem filhos
            self.raiz.atualiza_n()
        elif len(self.raiz.p) == 0:                                       #caso: inserção em uma folha porém estrapolando
            self.raiz.r.append(reg)                                       #o número máximo de Itens
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
        while not self.verifica():                                       #Reconstrução da árvore caso necessário
            self.reconstruir()

    def _insere(self, reg:"Item", pag:"Pagina"):
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
            for i in range(self.m+1, self.mm+1):
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
        while not self.verifica():
            self.reconstruir()
    
    def remover(self, reg:"Item"):
        pag = self.pesquisa(reg)
        if pag.raiz and pag.n > 1 and len(pag.p) == 0:                      #Remoção de um item na raiz
            for i in range(pag.n):
                if pag.r[i] == reg:
                    pag.r.pop(i)
                    pag.atualiza_n()
                    break
        elif not pag.raiz and pag.n > pag.max_r/2 and len(pag.p) == 0:      #Remoção de um item em uma página com mais de m Itens
            for i in range(pag.n):
                if pag.r[i] == reg:
                    pag.r.pop(i)
                    pag.atualiza_n()
                    break
        else:                                                               #Demais casos (necessitam de reconstrução)
            pag.pop()
            self.reconstruir()          
        while not self.verifica():
            self.reconstruir()

    def reconstruir(self):                                                  #Reconstroi a árvore dentre os casos descritos
        procurado = self.pai(None)                                          #nos slides teóricos 
        giro = 0
        if procurado != None:
            for i in range(len(procurado.p)+1):
                if procurado.p[i] == None:
                    giro = 1
                    break
            if giro == 1:
                if procurado.p[i-1].n > self.m:
                    self.giro_direita(procurado.r[i-1])
                elif  procurado.p[i+1].n > self.m:
                    self.giro_esquerda(procurado.r[i])
                else:
                    self.reconstruir_m(procurado,i)
        elif self.raiz.procura() != None:
            pag = self.raiz.procura()
            for i in range(len(procurado.p)+1):
                if procurado.p[i] == pag:
                    giro = 1
                    break
            if giro == 1:
                if procurado.p[i-1].n > self.m:
                    self.giro_direita(procurado.r[i-1])
                elif  procurado.p[i+1].n > self.m:
                    self.giro_esquerda(procurado.r[i])
                else:
                    self.reconstruir_m(procurado,i)


    def reconstruir_m(self, pag:"Pagina", i:int):
        if (pag.raiz and pag.n > 1) or (not pag.raiz and pag > self.m):
            if i == pag.n:
                for j in range(pag.p[i].n):
                    pag.p[i-1].append(pag.p[i].r[j])
                pag.p[i-1].append(pag.r[i-1])
                pag.r.pop(i-1)
                pag.p.pop(i)
            else:
                for j in range(pag.p[i].n):
                    pag.p[i+1].append(pag.p[i].r[j])
                pag.p[i+1].append(pag.r[i])
                pag.r.pop(i)
                pag.p.pop(i)
        else:
            pai = self.pai(pag)
            for j in range(len(pai.p)):
                if pai.p[j] == pag:
                    break
            self.reconstruir_m(pai,j)
    

    def pesquisa(self, reg:"Item") -> Pagina:                              #Retorna a página cujo item esppecificado está
        if reg in self.raiz.r:
            return self.raiz
        else:
            return self._pesquisa(reg, self.raiz)

    def _pesquisa(self, reg:"Item", pag:"Pagina") -> Pagina:
        for i in range(len(pag.p)):
            if reg in pag.p[i].r:
                return pag.p[i]
            else:
                self._pesquisa(reg, pag.p[i])

    def giro_esquerda(self, reg:"Item"):                                   #Realiza um movimento auxiliar na reconstruçao
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

    def giro_direita(self, reg:"Item"):                                   #Realiza um movimento auxiliar na reconstruçao
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

    def pai(self,pag:"Pagina") -> Pagina:                                 #Retorna a página pai da passada como parâmetro
        if pag in self.raiz.p:
            return self.raiz
        else:
            for i in range(len(self.raiz.p)):
                return self.pai(self.raiz.p[i])

    def subir_item(self,reg:"Item"):                                      #Realiza um movimento auxiliar na reconstruçao
        pag = self.pesquisa(reg)
        print(pag)
        p_pag = self.pai(pag)
        i = 0
        for i in range(pag.n):
            if pag.r[i] == reg:
                break
        p_pag.r.append(pag.r[i])
        p_pag.r.sort()
        p_pag.atualiza_n()
        pag.r.pop(i)
        pag.atualiza_n()

    def verifica(self) -> bool:                                          #Realiza a verificação da árvore
        return self.raiz.verifica()
