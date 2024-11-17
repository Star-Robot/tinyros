cmake_minimum_required(VERSION 3.10)
project(TinyRosTest)

# 设置编译器和编译选项
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall -fPIC -w -fopenmp")
set(CMAKE_BUILD_TYPE "Release")

# 添加本地生成的第3方库路径
list(APPEND CMAKE_PREFIX_PATH "/home/tiger/workspace/tinyros_conan/build/install/share/cmake/")

# 查找 TinyRos 库
find_package(TinyRos REQUIRED)

# 查找 gRPC 库
find_package(gRPC REQUIRED)

# 包含头文件路径
include_directories(${TinyRos_INCLUDE_DIRS})

# 添加源文件
add_executable(listener src/listener.cpp)
add_executable(talker src/talker.cpp)

# 链接 TinyRos 和 gRPC 库
target_link_libraries(listener ${TinyRos_LIBRARIES} gRPC::grpc gRPC::grpc++)
target_link_libraries(talker ${TinyRos_LIBRARIES} gRPC::grpc gRPC::grpc++)
