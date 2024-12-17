call activate.cmd
set OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:19192
set OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument --traces_exporter otlp --logs_exporter console,otlp --metrics_exporter otlp python app2.py