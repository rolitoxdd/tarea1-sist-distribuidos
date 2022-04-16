FROM python:3.10
WORKDIR /app
COPY requirements.txt example.proto ./
RUN pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. example.proto
CMD ["python3", "-u", "server.py"]