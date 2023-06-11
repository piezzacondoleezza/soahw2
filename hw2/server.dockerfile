FROM python:3.11
RUN pip install grpcio-tools
COPY . .
CMD ["python3", "server.py"]