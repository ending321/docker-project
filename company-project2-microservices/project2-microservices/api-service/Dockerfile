# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 创建并写入新的 sources.list（适用于 slim 镜像）
RUN echo "deb http://mirrors.aliyun.com/debian bookworm main contrib non-free" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian bookworm-updates main contrib non-free" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian-security bookworm-security main contrib non-free" >> /etc/apt/sources.list\
    && sed -i '/deb.debian.org/d' /etc/apt/sources.list


# 设置工作目录
WORKDIR /app

# 安装系统依赖（使用国内源加速）
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*  # 清理缓存，减小镜像体积

# 替换 pip 源为国内镜像（阿里云）
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip config set global.trusted-host mirrors.aliyun.com

# 安装 Python 依赖（通过国内源加速）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
