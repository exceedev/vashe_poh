# vashe_poh
repository for practice in microservice architecture

env fastapi:\
MONGO_HOST=mongo\
MONGO_PORT=27017

RABBITMQ_DEFAULT_VHOST=vhost
RABBITMQ_DEFAULT_USER=myuser
RABBITMQ_DEFAULT_PASS=mypassword

CELERY_BROKER_URL=pyamqp://myuser:mypassword@rabbitmq/vhost
#CELERY_BROKER_URL=pyamqp://myuser:mypassword@localhost:5672/vhost
CELERY_RESULT_BACKEND=rpc://
