FROM python:rc-alpine

WORKDIR /usr/src/app/

COPY entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 81

CMD ["entrypoint.sh"]
