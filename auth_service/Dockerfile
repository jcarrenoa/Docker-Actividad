FROM python:3.9-alpine
WORKDIR /app
COPY app.py /app
COPY template /app/template/
RUN pip install flask
CMD ["python", "app.py"]