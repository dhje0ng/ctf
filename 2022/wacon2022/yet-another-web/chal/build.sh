docker build --tag yet-another-web:latest --platform linux/amd64 .
docker run -itd -p 9193:80 yet-another-web
