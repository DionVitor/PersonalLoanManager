from celery import Celery


app = Celery(
    "worker",
    broker="amqp://rabbit_personal_loan_manager:rabbit_personal_loan_manager@rabbitmq:5672",
    include=["infra.celery_gateway.tasks"]
)

app.conf.task_routes = {"infra.celery_gateway.tasks.process_personal_loan": {"queue": "personal_loan_manager"}}
