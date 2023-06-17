from infra.celery_gateway.worker import app


@app.task()
def process_personal_loan():
    pass
