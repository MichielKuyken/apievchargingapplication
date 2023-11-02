FROM python:3.11.0-alpine
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./EV_Chargin_Application/myproject /code/myproject
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "myproject.main:app", "--host", "0.0.0.0", "--port", "8000"]