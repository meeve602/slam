cmake_minimum_required( VERSION 2.8 )

project( 6 )

add_executable( 6 6.cpp )

set(CMAKE_CXX_COMPILER "g++")

set( CMAKE_BUILD_TYPE "Debug")

include_directories("/usr/include/eigen3")

#include_directories("/root/slam/lambook2-master/3rdparty/Pangolin/Pangolin/")

find_package(Pangolin REQUIRED)  
                                               
include_directories(${Pangolin_INCLUDE_DIRS})  

target_link_libraries(6 ${Pangolin_LIBRARIES})
