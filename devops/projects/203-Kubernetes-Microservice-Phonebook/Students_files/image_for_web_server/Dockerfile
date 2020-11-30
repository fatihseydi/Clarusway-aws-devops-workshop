FROM python:alpine
COPY . /image_for_web_server 
WORKDIR /image_for_web_server 
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./phonebook-upd-del-add.py