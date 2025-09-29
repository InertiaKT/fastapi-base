**镜像构建**

docker build -f docker/Dockerfile -t algo-platform:v0.0.1 .

**镜像导出**

docker save -o docker/algo-platform.v001.tar algo-platform:v0.0.1

**镜像启动**

docker run -d -p 30021:30021 --name algo-platform algo-platform:v0.0.1

**版本信息**

v0.0.1: 初次构建
