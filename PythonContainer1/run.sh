#!/bin/sh

. .venv/bin/activate
#.venv/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp python -m app
#.venv/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp gunicorn app:app

#.venv/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp gunicorn -b 0.0.0.0:8111 app:app
.venv/bin/opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp gunicorn app2:app
