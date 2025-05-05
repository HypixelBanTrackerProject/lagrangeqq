# 使用 Python 基础镜像
FROM python:3.9-slim

# 安装依赖
RUN apt-get update && \
    apt-get install -y libicu-dev && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

VOLUME [ "/app/lagrange/config" ]

# 启动应用
CMD ["python","app.py"]
