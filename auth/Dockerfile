FROM 832266673134.dkr.ecr.us-east-1.amazonaws.com/socialbase/python3:latest

RUN apk add --no-cache libcurl curl-dev openssl

WORKDIR /usr/src/app/

COPY entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 81

CMD ["entrypoint.sh"]
