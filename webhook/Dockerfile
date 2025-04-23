FROM python:3.10

WORKDIR /app
COPY webhook.py .
COPY ansible /ansible

RUN pip install flask ansible

CMD ["python", "webhook.py"]

