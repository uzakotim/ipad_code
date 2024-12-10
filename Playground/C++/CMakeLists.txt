# Minimum required version of CMake
cmake_minimum_required(VERSION 3.16)

# Project name and version
project(MyProject VERSION 1.0 LANGUAGES CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable (replace main.cpp with your source files)
add_executable(run_me 
    src/main.cpp
)

# Include directories for header files
target_include_directories(run_me PRIVATE include)

# Link libraries if needed (example: linking with math library)
# target_link_libraries(run_me PRIVATE m)

# Enable warnings
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    target_compile_options(run_me PRIVATE -Wall -Wextra -Wpedantic)
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    target_compile_options(run_me PRIVATE /W4)
endif()
