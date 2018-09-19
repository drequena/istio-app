FROM python:3.6-alpine

LABEL mantainers="Daniel Requena"
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

COPY * /opt/
WORKDIR /opt/

RUN apk update && \
apk upgrade && \
apk add gcc make linux-headers musl-dev && \
pip install pip --upgrade && \
pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]