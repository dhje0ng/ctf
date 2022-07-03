FROM python:3

RUN mkdir /app
ADD app.py /app/
ADD requirement.txt /app/

WORKDIR /app
RUN pip3 install -r requirement.txt
ADD ./entrypoint.sh /

RUN chmod a+x /entrypoint.sh

ENTRYPOINT '/entrypoint.sh'