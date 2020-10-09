
set(CMAKE_CXX_STANDARD 20)


file(GLOB headerCollection "${Vodka_SOURCE_DIR}/include/*.hpp")
file(GLOB fileLibraryCollection "./*.cpp")

set(HEADER_LIST ${headerCollection})

add_library(libvodka ${fileLibraryCollection} ${headerCollection})
target_include_directories(libvodka PUBLIC ../include)

target_compile_definitions(libvodka PUBLIC cxx_std_20)