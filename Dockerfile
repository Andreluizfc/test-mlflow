FROM python:3.9
COPY /models /models
COPY /src /src

WORKDIR /models/model_v1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /src/models
EXPOSE 8080

#CMD ["gunicorn", "-b", "0.0.0.0:8080", "api"]
CMD ["python", "./api.py"]
