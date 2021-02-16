import unittest
from arvore_b import Item, Pagina, ArvoreB

def teste_insere():
	print("\nTESTE INSERE")
	arvore = ArvoreB(2)
	i1 = Item(4)
	i2 = Item(2)
	i3 = Item(3)
	i4 = Item(0)
	i5 = Item(1)
	arvore.insere(i1)
	arvore.insere(i2)
	arvore.insere(i3)
	arvore.insere(i4)
	arvore.insere(i5)
	arvore.imprime()

def teste_pesquisa():
	print("\nTESTE PESQUISA")
	arvore = ArvoreB(2)
	i1 = Item(4)
	i2 = Item(2)
	i3 = Item(3)
	i4 = Item(0)
	i5 = Item(1)
	arvore.insere(i1)
	arvore.insere(i2)
	arvore.insere(i3)
	arvore.insere(i4)
	arvore.insere(i5)
	print("Item pesquisado: " + str(i1))
	print(arvore.pesquisa(i1))

def teste_remover():
	print("\nTESTE REMOVER")
	arvore = ArvoreB(2)
	i1 = Item(4)
	i2 = Item(2)
	i3 = Item(3)
	i4 = Item(0)
	i5 = Item(1)
	i6 = Item(5)
	arvore.insere(i1)
	arvore.insere(i2)
	arvore.insere(i3)
	arvore.insere(i4)
	arvore.insere(i5)
	arvore.insere(i6)
	arvore.imprime()
	arvore.remover(i3)
	arvore.imprime()

def main():
	teste_insere()
	teste_pesquisa()
	teste_remover()

if __name__ == '__main__':
	main()