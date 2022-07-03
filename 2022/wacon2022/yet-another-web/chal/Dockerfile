FROM ubuntu:20.04
ENV TZ=Asia/Seoul

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update
RUN apt install apache2 php7.4 curl -y

RUN rm /var/www/html/index.html
ADD ./index.php /var/www/html/
ADD ./entrypoint.sh /

RUN chmod a+x /entrypoint.sh

ENTRYPOINT '/entrypoint.sh'