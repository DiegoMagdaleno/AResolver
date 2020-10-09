cmake_minimum_required(VERSION 3.17)
project(Vodka)

set(CMAKE_CXX_STANDARD 20)
file(GLOB_RECURSE fileCollection "src/*.cpp")


add_executable(Vodka ${fileCollection})

# Packages, this are managed by VCPKG, see documentation for more information
find_package(nlohmann_json CONFIG REQUIRED)
target_link_libraries(Vodka PRIVATE nlohmann_json nlohmann_json::nlohmann_json)