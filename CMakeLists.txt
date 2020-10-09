cmake_minimum_required(VERSION 3.17)
project(Vodka)

set(CMAKE_CXX_STANDARD 20)

file(GLOB cmakeDependenciesCollection "${PROJECT_SOURCE_DIR}/cmake/*.cmake")
foreach(includeFile ${cmakeDependenciesCollection})
    include(${includeFile})
    message("Adding ${includeFile} to cmake")
endforeach()

# Init our own submodules
find_package(Git QUIET)
if(GIT_FOUND AND EXISTS "${PROJECT_SOURCE_DIR}/.git")
    option(GIT_SUBMODULE "Check for submodules during build" ON)
    if(GIT_SUBMODULE)
        message(STATUS "Submodule update began")
        execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                RESULT_VARIABLE GIT_SUBMOD_RESULT)
        if(NOT GIT_SUBMOD_RESULT EQUAL "0")
            message(FATAL_ERROR "git submodule update --init failed with ${GIT_SUBMOD_RESULT}, please checkout submodules")
        endif()
    endif()
endif()

SUBDIRLIST(SUBDIRECTORIES ${PROJECT_SOURCE_DIR}/extern)
FOREACH(subdir ${SUBDIRECTORIES})
    if(NOT EXISTS "${PROJECT_SOURCE_DIR}/extern/${subdir}/CMakeLists.txt")
        message(FATAL_ERROR "The submodules were not downloaded! GIT_SUBMODULE was turned off or failed. Please update submodules and try again.")
    endif()
endforeach()


FOREACH(subdir ${SUBDIRECTORIES})
    add_subdirectory("${PROJECT_SOURCE_DIR}/extern/${subdir}")
endforeach()
add_subdirectory(lib)
add_subdirectory(src)

