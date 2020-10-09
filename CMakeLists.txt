cmake_minimum_required(VERSION 3.17)
project(Vodka)

set(CMAKE_CXX_STANDARD 20)

file(GLOB cmakeDependenciesCollection "./cmake/*.cmake")
include(${cmakeDependenciesCollection})


add_subdirectory(lib)
add_subdirectory(src)
