# SLAM
SLAM follow to learn 

# CMAKE
CMAKE follow to learn
## NOTE
1，版本号

cmake_minimum_required( VERSION 2.8 )

2，项目名称 

project( 1 )

3，可执行程序

add_executable( 1 1.cpp )

4，set设置编译环境

set(CMAKE_CXX_COMPILER "g++")

   设置debug
   
set( CMAKE_BUILD_TYPE "Debug")

   设置值并打印 /////功能相当与定义一个变量并赋予值，用值${变量名}
   
set (normal_var a)

message (">>> value = ${normal_var}")

5，添加库

add_library( 2 2.cpp )

6，添加库需要连接库

target_link_libraries( 1 2 )


