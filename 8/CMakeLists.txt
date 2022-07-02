cmake_minimum_required( VERSION 2.8 )

project( 8 )

add_executable( 8 8.cpp )

set(CMAKE_CXX_COMPILER "g++")

set( CMAKE_BUILD_TYPE "Debug")

include_directories("/usr/include/eigen3")

#include_directories("/root/slam/lambook2-master/3rdparty/Pangolin/Pangolin/")

find_package(Pangolin REQUIRED)  
                                               
#include_directories(${Pangolin_INCLUDE_DIRS})  

#target_link_libraries(8 ${Pangolin_LIBRARIES})

find_package(Sophus REQUIRED)  

include_directories(${Sophus_INCLUDE_DIRS} ${Pangolin_INCLUDE_DIRS})  

target_link_libraries(8 ${Sophus_LIBRARIES} ${Pangolin_LIBRARIES} ) 

message("cmake_module_path: " ${CMAKE_MODULE_PATH})

#include_directories("/root/slam/slambook2-master/3rdparty/Sophus/Sophus-13fb3288311485dc94e3226b69c9b59cd06ff94e/sophus")  
target_link_libraries(8 Sophus::Sophus)

