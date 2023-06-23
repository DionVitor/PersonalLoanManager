<h1 align="center">PersonalLoanManager</h1>
<p align="center"> System to manage personal loans.</p>

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

English | [Português](https://github.com/DionVitor/PersonalLoanManager/blob/master/docs/README-pt_BR.md)

## :package: Instructions for run the app

- Download docker and compose [here](https://docs.docker.com/engine/install/)
- Clone the repository ```git clone https://github.com/DionVitor/PersonalLoanManager/```
- Go to repository ```cd PersonalLoanManager/```
- Build and create containers ```docker-compose up -d```
- Migrate tables ```make migrate```
- Populate database ```make populate```

## :keyboard: How to use the system

- Enter in [personal loan offer page](http://localhost:7050/) in order to create a new loan offer
- See all registered loan offers and edit which fields will be appeared on personal loan offer page accessing [admin](http://localhost:8000/admin).
  - user: admin
  - password: admin
- In order to see all the processed tasks by celery, access [flower](http://localhost:8888).

## :hammer: Tech stack

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)
- [RabbitMQ](https://www.rabbitmq.com)

## :smile: Author

Make by Dion Vítor, Contact:

[![Gmail Badge](https://img.shields.io/badge/-dionvictor11@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dionvictor11@gmail.com)](mailto:dionvictor11@gmail.com)
[![WhatsApp Badge](https://img.shields.io/badge/-WhatsApp-green?style=flat-square&logo=WhatsApp&logoColor=white&link=https://api.whatsapp.com/send?phone=5561998822233)](https://api.whatsapp.com/send?phone=5561998822233)
[![Linkedin Badge](https://img.shields.io/badge/-Dion%20V%C3%ADtor-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)](https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)