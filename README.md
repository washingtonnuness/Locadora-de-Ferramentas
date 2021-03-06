# Locadora

Projeto para Locadora de ferramentas TCC.


Este projeto foi feito com:

* Python 3.9.8
* Django 4.0
* Bootstrap 4.0
* htmx


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.


```
git clone https://github.com/washingtonnuness/Locadora-de-Ferramentas.git
cd exame-inline
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
python manage.py seed cliente --number=10
python manage.py seed fornecedor --number=10
python manage.py seed orcamento --number=10
python manage.py corrige_dados
```



## isort

```
isort -m 3 *
```

## Modelagem

![orcamentos_modelagem2.png](img/orcamentos_modelagem2.png)

![models.png](img/models.png)

https://www.dicas-de-django.com.br/36-django-visualizando-seus-modelos-com-graph-models


![diagrama_ER_DBeaver.png](img/diagrama_ER_DBeaver.png)

## branch

### Criando uma nova branch

```
git checkout -b nova-branch
```

### Fazendo as alterações

```
# altere seu código
git add .
git commit -m 'Mensagem do commit.'
git push
# talvez você tenha que fazer
# git push --set-upstream origin nova-branch
```

### Criando o Pull request no Github

No Github clique em Pull requests e clique no botão **New pull request**.

Escolha a branch que você quer mergear com a branch *main*.

Depois clique no botão **Create pull request**.


#### Fazendo o Merge requests

Outra pessoa da equipe vai abrir o PR e conferir os commits.

Depois é só clicar em **Merge pull request**.

### Atualizando a branch main na máquina local

```
git checkout main
git pull origin main
```

**Obs:** Caso você tenha feito mais commits depois de ter feito o Merge do PR, então você vai precisar fazer o merge manualmente.

Considere que você esteja na nova-branch e você já fez

```
git commit -m 'Nova alteração depois do merge'
git push
```

Fazendo o merge manualmente

```
git checkout main
git merge nova-branch
git push
```