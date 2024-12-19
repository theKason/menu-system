# 拉取ubuntu容器
FROM ubuntu

# 在容器中安装python3和pip3
RUN apt update && apt install -y python3 python3-pip python3-venv && rm -rf /var/lib/apt/lists/*

# 创建并激活虚拟环境
RUN python3 -m venv /opt/venv
ENV PATH='/opt/venv/bin:$PATH'

# 安装Django
RUN pip install django

# 在容器中设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app/

CMD python3 manage.py runserver 0.0.0.0:80
