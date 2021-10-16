FROM python:3.8.3

WORKDIR /app
ADD . /app/
RUN pip install -r ./app/requirements.txt

EXPOSE 5000
CMD ["python", "./app/main.py"]