add_executable(vodkacli main.cpp)
target_compile_features(vodkacli PRIVATE cxx_std_20)

target_link_libraries(vodkacli PRIVATE nlohmann_json nlohmann_json::nlohmann_json)
target_link_libraries(vodkacli PRIVATE libvodka)