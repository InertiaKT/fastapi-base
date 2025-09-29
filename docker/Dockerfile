FROM ubuntu:22.04

WORKDIR /app

COPY . .

# 安装 uv
RUN apt update && apt install -y curl && curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH=/root/.local/bin:$PATH

# python 环境搭建
RUN echo $PATH && \
    uv sync && \
    uv pip install torch torchcodec torchvision --index-url https://download.pytorch.org/whl/cu128

CMD ["uv", "run", "main.py"]
