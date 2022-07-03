docker build --tag yet-another-web-flag:latest --platform linux/amd64 .
docker run -itd -p 31337:31337 yet-another-web-flag