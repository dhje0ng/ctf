FROM php:7.4-apache

COPY ./maindomain /var/www/maindomain
COPY ./subdomain /var/www/subdomain
COPY ./stuff/apache.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./stuff/fullchain.pem /etc/apache2/ssl/4z.is/fullchain.pem
COPY ./stuff/privkey.pem /etc/apache2/ssl/4z.is/privkey.pem


