FROM python:alpine
COPY . /image_for_result_server 
WORKDIR /image_for_result_server 
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./phonebook_search.py