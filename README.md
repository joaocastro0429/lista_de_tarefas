# 📝 Lista de Tarefas - Django

Um projeto simples e funcional desenvolvido com Django, que permite ao usuário **cadastrar, editar, listar e excluir tarefas**. Ideal para praticar conceitos de CRUD, formulários, rotas, templates e uso de Bootstrap.



---

## ⚙️ Funcionalidades

- ✅ Listagem de tarefas
- 🆕 Criação de nova tarefa
- 📝 Edição de tarefa
- 🗑️ Exclusão de tarefa
- 📌 Marcar tarefa como concluída
- 🎨 Interface com Bootstrap 5

---

## 💡 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Django 4+](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## 📦 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd seu-repositorio

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
