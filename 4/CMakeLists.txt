cmake_minimum_required( VERSION 2.8 )

project( 4 )

add_executable( 4 4.cpp )

set(CMAKE_CXX_COMPILER "g++")

#add_library( 2 2.cpp )

#target_link_libraries( 1 2 )

set( CMAKE_BUILD_TYPE "Debug")

include_directories("/usr/include/eigen3")
