#!/bin/bash

# 配置pip使用腾讯镜像源

# 创建pip配置目录
mkdir -p ~/.pip

# 创建或覆盖pip配置文件
cat > ~/.pip/pip.conf << EOF
[global]
index-url = https://mirrors.cloud.tencent.com/pypi/simple/

[install]
trusted-host = mirrors.cloud.tencent.com
EOF

echo "已配置pip使用腾讯镜像源"