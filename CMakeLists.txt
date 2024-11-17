cmake_minimum_required(VERSION 3.15)
project(TinyRos)
set(PROJECT_VERSION 1.0)

# 设置 C++ 编译器和编译选项
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall -msse4.2 -fPIC -O3 -w -fopenmp -mavx2")
# set(CMAKE_BUILD_TYPE "Release")

# 设置库输出目录
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/libs/)

# 包含源代码目录
include_directories(./src)

# 查找 Protobuf 和 gRPC 包
find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

# 设置生成的 proto 文件目录
include(${CMAKE_BINARY_DIR}/conan/build/${CMAKE_BUILD_TYPE}/conanbuildinfo.cmake)
include_directories(${PROTO_SRC_DIR})

# 收集源文件
file(GLOB_RECURSE SOURCES src/*.cpp ${PROTO_SRC_DIR}/*.pb.cc ${PROTO_SRC_DIR}/*.grpc.pb.cc)

# 添加共享库
add_library(tinyros SHARED ${SOURCES})
target_link_libraries(tinyros ${Protobuf_LIBRARIES} gRPC::grpc gRPC::grpc++)

# 查找所有工具程序
file(GLOB TOOLS exe/*.cpp)
foreach(TOOL ${TOOLS})
  message(STATUS "TARGET:" ${TOOL})
  get_filename_component(PREFIX ${TOOL} NAME_WE)
  add_executable(${PREFIX} ${TOOL} ${SOURCES})
  target_link_libraries(${PREFIX} ${Protobuf_LIBRARIES} gRPC::grpc gRPC::grpc++)
  add_dependencies(${PREFIX} tinyros) 
  list(APPEND BINS ${PREFIX})
endforeach()

##################
##### install ####
##################
# 设置安装前缀
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install" CACHE PATH "Installation Directory" FORCE)
# 安装头文件
install(DIRECTORY "${CMAKE_SOURCE_DIR}/src/" # 源目录
        DESTINATION "include" # 目标目录
        FILES_MATCHING # 只安装匹配的文件
        PATTERN "*.hpp" # 选择所有头文件
        PATTERN "proto" EXCLUDE
)
# 安装库文件
install(TARGETS tinyros
        EXPORT TinyRosTargets
        LIBRARY DESTINATION lib
)
# 安装可执行文件
install(TARGETS ${BINS} 
        RUNTIME DESTINATION bin
)
# 导出目标文件
install(EXPORT TinyRosTargets DESTINATION share/cmake)
# 生成 TinyRosConfig.cmake
configure_file(${CMAKE_SOURCE_DIR}/TinyRosConfig.cmake.in 
               ${CMAKE_BINARY_DIR}/cmake/TinyRosConfig.cmake @ONLY
)
install(FILES ${CMAKE_BINARY_DIR}/cmake/TinyRosConfig.cmake 
        DESTINATION share/cmake
)