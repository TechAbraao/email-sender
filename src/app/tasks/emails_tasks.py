from src.app.celery_app import celery_app
from src.app.services.emails_services import EmailsService
from src.app.repository.emails_repository import EmailsRepository

service = EmailsService()
repository = EmailsRepository()

@celery_app.task(bind=True)
def send_email_task(self, email_body: dict) -> tuple[bool, dict]:
    success, result = service.send_email(email_body)
    
    if not success:
        raise Exception(f"Failed to send e-mail")
    
    if isinstance(result, dict):
        result['task_id'] = self.request.id
    return success, result

@celery_app.task
def update_database_status_success_task(result: any) -> bool:
    try:
        success, data = result
        task_id = data.get('task_id')
        if not task_id:
            raise ValueError("Task ID not found in result data.")
        
        """ Update the email status in the database to 'SENT' """
        success_update, message = repository.update_status_by_task_id(task_id, "SENT")
        if not success_update:
            raise Exception(f"Failed to update e-mail status: {message}")
        return True
    except Exception as err: 
        return False, str(err)


@celery_app.task()
def update_database_status_failure_task(result):
    try:
        if isinstance(result, tuple) and len(result) == 1:
            task_id = result[0]
        elif isinstance(result, dict):
            task_id = result.get("task_id")
        else:
            task_id = str(result) 

        if not task_id:
            raise ValueError("No task_id provided in result.")

        return repository.update_status_by_task_id(task_id, "FAILED")

    except Exception as err:
        return False, str(err)
