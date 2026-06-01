FROM python
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD [ "flask", "run" ]