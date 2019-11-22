FROM python:3.7-alpine
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]