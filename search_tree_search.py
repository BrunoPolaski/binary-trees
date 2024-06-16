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
    self.ligacoes = []

  def inserir(self, valor):
    novo = No(valor)
    # Se a árvore estiver vazia
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
            self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
            return
        # Direita
        else:
          atual = atual.direita
          if atual == None:
            pai.direita = novo
            self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
            return

  def pesquisar(self, valor):
    atual = self.raiz
    while atual.valor != valor:
      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita
      if atual == None:
        return None
    return atual

  # Raiz, esquerda, direita
  def pre_ordem(self, no):
    if no != None:
      print(no.valor)
      self.pre_ordem(no.esquerda)
      self.pre_ordem(no.direita)

  # Esquerda, raiz, direita
  def em_ordem(self, no):
    if no != None:
      self.em_ordem(no.esquerda)
      print(no.valor)
      self.em_ordem(no.direita)

  # Esquerda, direita, raiz
  def pos_ordem(self, no):
    if no != None:
      self.pos_ordem(no.esquerda)
      self.pos_ordem(no.direita)
      print(no.valor)

### Inserção e visualização
arvore = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)
arvore.raiz.esquerda.valor
arvore.raiz.direita.valor
arvore.inserir(100)
arvore.ligacoes
### Pesquisar
arvore.pesquisar(39)
arvore.pesquisar(84)
if arvore.pesquisar(101) == None:
  print('Elemento não localizado')
else:
  print('Elemento localizado')
### Travessia
arvore.pre_ordem(arvore.raiz)
arvore.em_ordem(arvore.raiz)
arvore.pos_ordem(arvore.raiz)