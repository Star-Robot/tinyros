from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os


class TinyRosConan(ConanFile):
    name = "TinyRos"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = (
        "grpc/1.50.1",
        "protobuf/3.21.12",
    )
    tool_requires = (
        "protobuf/3.21.12",
        "grpc/1.50.1",
    )

    def layout(self):
        cmake_layout(self)

    def generate(self):
        # 生成 Protobuf 和 gRPC 文件
        proto_dir = os.path.join(self.source_folder, "src/proto")
        proto_src_dir = os.path.join(self.build_folder, "proto-src")
        os.makedirs(proto_src_dir, exist_ok=True)

        protoc = os.path.join(
            self.dependencies["protobuf"].package_folder, "bin", "protoc"
        )
        grpc_cpp_plugin = os.path.join(
            self.dependencies["grpc"].package_folder, "bin", "grpc_cpp_plugin"
        )

        for proto in os.listdir(proto_dir):
            if proto.endswith(".proto"):
                proto_file = os.path.join(proto_dir, proto)
                self.run(
                    f"{protoc} --proto_path={proto_dir} --grpc_out={proto_src_dir} --plugin=protoc-gen-grpc={grpc_cpp_plugin} {proto_file}"
                )
                self.run(
                    f"{protoc} --proto_path={proto_dir} --cpp_out={proto_src_dir} {proto_file}"
                )

        # 设置 CMake 变量
        cmake_file = os.path.join(self.build_folder, "conanbuildinfo.cmake")
        with open(cmake_file, "a") as f:
            f.write(f'set(PROTO_SRC_DIR "{proto_src_dir}")\n')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")  # Windows 下复制 DLL 文件
        self.copy("*.dylib*", dst="lib", src="lib")  # macOS 下复制 dylib 文件
