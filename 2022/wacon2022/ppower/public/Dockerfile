FROM node:bullseye@sha256:6b91515d351353e47b48a2644be4f0581f921b53da0c494be176d6573fe8818e
WORKDIR /app
COPY ./stuff ./
RUN chmod +x ./index.js
RUN npm install
EXPOSE 8000
RUN useradd app
COPY ./flag /flag
COPY ./stuff/readflag /realreadflag
RUN chmod u+s /realreadflag
RUN chmod 500 /flag
USER app
ENV NODE_ENV=production
CMD "./index.js"
