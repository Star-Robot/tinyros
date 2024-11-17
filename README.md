# TinyRos

TinyRos 是一个使用 Conan 和 CMake 构建的项目。本指南将详细介绍如何构建这个工程。

## 先决条件

在开始之前，请确保您的系统已经安装了以下工具：

- [Conan](https://conan.io/)
- [CMake](https://cmake.org/)
- [GCC](https://gcc.gnu.org/) 或其他兼容的 C++ 编译器

## 构建步骤

### 1. 克隆仓库

首先，克隆 TinyRos 仓库到本地：

```bash
git clone https://github.com/yourusername/tinyros.git
cd tinyros
```

### 2. 安装 Conan 依赖项

使用 Conan 安装项目所需的依赖项：

```bash
conan install . --output-folder=build/conan --build=missing -s build_type=Debug
```

### 3. 配置项目

使用 CMake 配置项目：

```bash
cmake -B build -S . -DCMAKE_BUILD_TYPE=Debug -DCMAKE_TOOLCHAIN_FILE=build/conan/build/Debug/generators/conan_toolchain.cmake
```

### 4. 编译项目

使用 CMake 编译项目：

```bash
cmake --build build -j4
```


## 目录结构

项目的主要目录结构如下：

```
tinyros/
├── build/                  # 构建输出目录
├── src/                    # 源代码目录
│   ├── proto/              # Protobuf 文件目录
│   └── ...                 # 其他源文件
├── CMakeLists.txt          # CMake 配置文件
├── conanfile.py            # Conan 配置文件
├── build.sh                # 构建脚本
└── README.md               # 项目说明文件
```

## 贡献

欢迎贡献代码！请 fork 本仓库并提交 pull request。

## 许可证

此项目使用 MIT 许可证。详情请参阅 LICENSE 文件。
