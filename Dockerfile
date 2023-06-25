FROM python:3.9
#RUN apt-get update && apt-get install -y python3.9 python3.9-dev
COPY /models /models
COPY /src /src

WORKDIR /models/model_v1
RUN pip install -r requirements.txt

WORKDIR /src/models
EXPOSE 8080

#CMD ["gunicorn", "-b", "0.0.0.0:8080", "api"]
CMD ["python", "./api.py"]
