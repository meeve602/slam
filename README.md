# SLAM
SLAM follow to learn 

# CMAKE
CMAKE follow to learn
## NOTE

cmake_minimum_required( VERSION 2.8 )

project( 1 )

add_executable( 1 1.cpp )

set(CMAKE_CXX_COMPILER "g++")

add_library( 2 2.cpp )

target_link_libraries( 1 2 )

set( CMAKE_BUILD_TYPE "Debug")
