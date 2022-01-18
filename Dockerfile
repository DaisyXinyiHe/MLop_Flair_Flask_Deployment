FROM python:3.8
RUN apt-get update
RUN cd $HOME
RUN git clone https://github.com/DaisyXinyiHe/MLop_Flair_Flask_Deployment.git
RUN cd MLop_Flair_Flask_Deployment
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 app.py
EXPOSE 8000
CMD ["python3", "app.py", "serve"]
