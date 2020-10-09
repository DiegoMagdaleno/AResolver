cmake_minimum_required(VERSION 3.17)
project(Vodka)

set(CMAKE_CXX_STANDARD 20)

add_executable(Vodka main.cpp lib/extensions.cpp lib/extensions.h)

find_package(nlohmann_json 3.2.0 REQUIRED)
target_link_libraries(Vodka PRIVATE nlohmann_json::nlohmann_json)