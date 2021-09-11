FROM python:3.8-slim-buster

#RUN apk add --no-cache python3-dev && \
#    pip install --upgrade pip

WORKDIR /app

COPY ./api /app

COPY ./model /app 

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

