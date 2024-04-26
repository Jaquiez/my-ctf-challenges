FROM python:alpine3.19
RUN apk update
RUN apk add curl-dev gcc libc-dev supervisor
RUN pip3 install flask gunicorn pycurl websockets
COPY config/supervisord.conf /etc/supervisord.conf
RUN chmod 750 /etc/supervisord.conf
WORKDIR /planktonsrouter1ba8b69e
COPY router .
COPY cleanup.sh /
COPY entrypoint.sh /
RUN chmod +x /cleanup.sh
RUN chmod +x /entrypoint.sh
RUN echo "UMASS{W3lC0m3_t0_Th3_FuTur3_Kr4bS_c28e1089b2}" > /flag53958e73c5ba4a66
RUN adduser sheldonjplankton -D
EXPOSE 8000
EXPOSE 9000
ENTRYPOINT [ "/entrypoint.sh" ]
