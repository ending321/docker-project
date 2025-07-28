FROM python:3.9-slim

# 创建并写入新的 sources.list（适用于 slim 镜像）
RUN echo "deb http://mirrors.aliyun.com/debian bookworm main contrib non-free" > /etc/apt/sources.list \
	&& echo "deb http://mirrors.aliyun.com/debian bookworm-updates main contrib non-free" >> /etc/apt/sources.list \
	&& echo "deb http://mirrors.aliyun.com/debian-security bookworm-security main contrib non-free" >> /etc/apt/sources.list

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	&&rm -rf /var/lib/apt/lists/*

# 替换 pip 源为国内镜像（阿里云）
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
	&& pip config set global.trusted-host mirrors.aliyun.com

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app/app.py"]
