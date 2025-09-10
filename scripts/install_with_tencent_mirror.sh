#!/bin/bash

# 使用腾讯镜像安装Python包的示例脚本

# 示例：使用腾讯镜像安装包
pip install -i https://mirrors.cloud.tencent.com/pypi/simple/ $1

# 或者设置环境变量
# export PIP_INDEX_URL=https://mirrors.cloud.tencent.com/pypi/simple/