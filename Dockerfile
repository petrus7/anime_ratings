FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
EXPOSE 8082

CMD ["flask", "run", "--host=0.0.0.0"]
