#!/bin/bash

build_type=Debug

# 安装 Conan 依赖项，指定输出目录和构建类型
conan install . --output-folder=build/conan --build=missing -s build_type=${build_type}

# 使用正确的工具链文件路径配置项目
cmake -B build -S . -DCMAKE_BUILD_TYPE=${build_type} -DCMAKE_TOOLCHAIN_FILE=build/conan/build/Debug/generators/conan_toolchain.cmake

# 编译项目
cmake --build build -j4

# 安装项⽬
cmake --install build