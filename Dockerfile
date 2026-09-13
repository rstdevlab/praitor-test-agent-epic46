FROM python:3.12-slim
COPY main.py .
EXPOSE 8080
CMD ["python", "main.py"]
