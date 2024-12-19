FROM ubuntu

RUN apt update && apt install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip3 install django

WORKDIR /app

COPY . .

CMD ["python3 manage.py runserver 8000", "/app/menu_system"]
