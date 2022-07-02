cmake_minimum_required( VERSION 2.8 )

project( 7 )

add_executable( 7 7.cpp )

set(CMAKE_CXX_COMPILER "g++")

set( CMAKE_BUILD_TYPE "Debug")

include_directories("/usr/include/eigen3")

#include_directories("/root/slam/lambook2-master/3rdparty/Pangolin/Pangolin/")

find_package(Pangolin REQUIRED)  
                                               
include_directories(${Pangolin_INCLUDE_DIRS})  

target_link_libraries(7 ${Pangolin_LIBRARIES})

find_package(Sophus REQUIRED)  

include_directories(${Sophus_INCLUDE_DIRS})  

target_link_libraries(7 ${Sophus_LIBRARIES}) 

#include_directories("../pack/Sophus/sophus/")  
