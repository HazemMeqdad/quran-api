FROM python:3.10


WORKDIR /opt/quran-api

COPY requirements.txt /opt/quran-api/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/quran-api/

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "--workers", "4", "app:app"]
