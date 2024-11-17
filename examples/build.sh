# 
build_type=Debug

# 安装 Conan 依赖项，指定输出目录和构建类型
conan install . --output-folder=build/conan

# 生成构建文件
cmake -B build -S . -DCMAKE_BUILD_TYPE=${build_type} -DCMAKE_TOOLCHAIN_FILE=./build/conan/conan_toolchain.cmake

# 编译项目
cmake --build build -j4