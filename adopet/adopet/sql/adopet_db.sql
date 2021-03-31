DROP DATABASE IF EXISTS adopet_django;
CREATE DATABASE adopet_django;
CREATE USER 'pet'@'%' IDENTIFIED BY 'pet';
GRANT ALL PRIVILEGES ON adopet_django.* TO 'pet'@'%';
GRANT ALL PRIVILEGES ON adopet_django.* TO 'pet'@'localhost';
