<h1 align="center">PersonalLoanManager</h1>
<p align="center"> Sistema para gerenciar propostas de empréstimo pessoal.</p>

<p align="center">
  <a>
    <img src="https://img.shields.io/badge/progress-100%25-brightgreen.svg" alt="progress">
  </a>
  <a>
    <img src="https://img.shields.io/badge/contribuition-welcome-brightgreen.svg" alt="contribution">
  </a>
  <a>
    <img src="https://img.shields.io/badge/version-1.0-brightgreen.svg" alt="version">
  </a>
</p>

[English](https://github.com/DionVitor/PersonalLoanManager/blob/master/README.md) | Português

## :package: Instruções para rodar o app

- Instale o docker e compose [aqui](https://docs.docker.com/engine/install/)
- Clone o repositório ```git clone https://github.com/DionVitor/PersonalLoanManager/```
- Vá para o repositório ```cd PersonalLoanManager/```
- Crie os containers ```docker-compose up -d```
- Migre as tabelas ```make migrate```
- Popule o banco de dados ```make populate```

## :keyboard: Como usar o sistema

- Entre na [página de preenchimento de proposta de empréstimo](http://localhost:7050/) para criar uma nova proposta de empréstimo
- Veja todas as propostas de emprétimo e edite quais campos irão aparecer na página de preenchimento de prosposta de empréstimo acessando o [admin](http://localhost:8000/admin).
  - usuário: admin
  - senha: admin
- Para ver todas as tarefas processadas pelo celery, acesse o [flower](http://localhost:8888).

## :hammer: Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)
- [RabbitMQ](https://www.rabbitmq.com)

## :smile: Autor

Feito por Dion Vítor, contatos:

[![Gmail Badge](https://img.shields.io/badge/-dionvictor11@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dionvictor11@gmail.com)](mailto:dionvictor11@gmail.com)
[![WhatsApp Badge](https://img.shields.io/badge/-WhatsApp-green?style=flat-square&logo=WhatsApp&logoColor=white&link=https://api.whatsapp.com/send?phone=5561998822233)](https://api.whatsapp.com/send?phone=5561998822233)
[![Linkedin Badge](https://img.shields.io/badge/-Dion%20V%C3%ADtor-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)](https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)