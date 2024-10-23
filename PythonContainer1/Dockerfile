#FROM python:latest
FROM python:alpine
COPY . /app
WORKDIR /app
#ADD *.crt /usr/local/share/ca-certificates/
#RUN update-ca-certificates
RUN chmod +x boot.sh
RUN chmod +x run.sh
RUN ./boot.sh

#ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
EXPOSE 8111

#CMD ["python", "app.py"]
#CMD ["/app/.venv/bin/opentelemetry-instrument", "--traces_exporter", "otlp", "--logs_exporter", "console,otlp", "--metrics_exporter", "otlp", "python", "-m" "app.py" ]
CMD ["./run.sh"]

