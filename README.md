# SEARCH BINARY TREE

# Search

In this part of the code, we need to go through the tree's nodes trying to find the value we want. We do this by verifying if the node values are smaller or greater than our current search value;

```py
def pesquisar(self, valor):
    atual = self.raiz
    while atual.valor != valor:
      if valor < atual.valor: ----------HERE----------
        atual = atual.esquerda -----------------------
      else: ----------AND HERE------------------------
        atual = atual.direita ------------------------
      if atual == None:
        return None
    return atual
```

this will make we decide if we go to the left or the right in the tree - as the code's comment shows. The ```atual``` variable means the current tree node that we are comparing. When it reaches the same value, it returns it, otherwise it returns ```None```.


## Insert into the tree

First, we create a new node:

```py
novo = No(valor)
```

Then, we check if the root is null and, if it isnt, we start the search to where we will insert the new node. We do this by creating two new values: ```atual``` and ```pai```, which at first are both the root node.
Now, after we do the search for where the node would go:
```py
if valor < atual.valor:
    atual = atual.esquerda
else:
    atual = atual.direita
```

We just instantiate our ```pai``` node's side variable with the address of our new Node and return the function:

```py
if atual == None:
    pai.esquerda = novo //esquerda ou direita
    return
```

And this is the end of the function.