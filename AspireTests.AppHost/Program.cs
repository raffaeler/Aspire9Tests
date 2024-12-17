using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

builder.AddProject<Projects.AspireTests>("aspiretests");

//builder.AddPythonApp("Python", "../PythonService1", "hello_python.py")
//       .WithEndpoint(targetPort: 8111, scheme: "http", env: "PORT", isProxied:false)
//       .WithEnvironment("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:19192")
//       .WithEnvironment("OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED", "true")
//       .WithEnvironment("PORT", "8111")
//       //.WithEnvironment("OTEL_PYTHON_OTLP_TRACES_SSL", "false")
//       ;

//builder.AddPythonApp("Python", "../PythonService1", "app2.py")
////builder.AddPythonApp("Python", "../PythonService1", "test.py")
//       .WithEndpoint(targetPort: 8111, scheme: "http", env: "PORT")
//       .WithEnvironment("PORT", "8111")
//       .WithOtlpExporter()
//       //.WithEnvironment("OTEL_PYTHON_OTLP_TRACES_SSL", "false")
//       ;

//builder.AddExecutable("Python", "cmd", "../PythonContainer1", "/C", "run.cmd")
//       .WithEndpoint(targetPort: 8111, scheme: "http", env: "PORT")
//       .WithEnvironment("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:19192")
//       .WithEnvironment("OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED", "true");


var config = builder.Configuration;
var param1 = builder.AddParameter("envraf");
builder.AddDockerfile("pythoncontainer1", "../PythonContainer1", "Dockerfile")
        .WithOtlpExporter()
        .WithEndpoint(port: 8111, targetPort: 8111, scheme: "http", env: "PORT")
        .WithEnvironment("PORT", "8111")
        //.WithEnvironment("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:19192")
        .WithEnvironment("OTEL_EXPORTER_OTLP_ENDPOINT", "http://host.docker.internal:19192")
        //.WithEnvironment("OTEL_EXPORTER_OTLP_ENDPOINT", "https://host.docker.internal:21103")
        .WithEnvironment("OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED", "true")
        .WithEnvironment("arg1", param1)
    ;



builder.Build().Run();
