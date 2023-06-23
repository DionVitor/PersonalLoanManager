migrate:
	$(info Migrations tables...)
	docker exec -it personal_loan_manager_api python3 manage.py migrate
	docker exec -it personal_loan_manager_api python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else 0;"

populate:
	docker exec -it personal_loan_manager_api python3 manage.py shell -c "from loan.models import LoanField; fields = [LoanField(name=f) for f in ('Nome completo', 'CPF', 'Endereço', 'Valor do empréstimo pretendido')]; LoanField.objects.bulk_create(fields);"
