from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class TinyRosTestConan(ConanFile):
    name = "TinyRosTest"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "grpc/1.50.1",
        "protobuf/3.21.12",
    )

    def layout(self):
        self.folders.build = "build"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()