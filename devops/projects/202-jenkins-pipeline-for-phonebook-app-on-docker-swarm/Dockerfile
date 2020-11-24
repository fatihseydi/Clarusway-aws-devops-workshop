FROM python:alpine
COPY . /app
WORKDIR /app
ADD templates templates
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["phonebook-app.py"]