class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

  def mostra_no(self):
    print(self.valor)
class ArvoreBinariaBusca:
  def __init__(self):
    self.raiz = None

  def inserir(self, valor):
    novo = No(valor)

    if self.raiz == None:
      self.raiz = novo
    else:
      atual = self.raiz
      while True:
        pai = atual
        # Esquerda
        if valor < atual.valor:
          atual = atual.esquerda
          if atual == None:
            pai.esquerda = novo
            return
        # Direita
        else:
          atual = atual.direita
          if atual == None:
            pai.direita = novo
            return

arvore = ArvoreBinariaBusca()

arvore.inserir(54)
arvore.inserir(20)
arvore.inserir(25)
arvore.inserir(1)