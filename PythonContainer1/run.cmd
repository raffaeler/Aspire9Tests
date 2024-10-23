call activate.cmd
opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp python app2.py