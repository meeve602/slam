cmake_minimum_required( VERSION 2.8 )

project( 5 )

add_executable( 5 5.cpp )

set(CMAKE_CXX_COMPILER "g++")

#add_library( 2 2.cpp )

#target_link_libraries( 1 2 )

set( CMAKE_BUILD_TYPE "Debug")

include_directories("/usr/include/eigen3")

include_directories("/root/slam/lambook2-master/3rdparty/Pangolin/Pangolin/")

find_package(Pangolin REQUIRED)                                                 
include_directories(${Pangolin_INCLUDE_DIRS})  

#add_executable(plotTrajectory plotTrajectory.cpp)

target_link_libraries(5 ${Pangolin_LIBRARIES})
