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

7，添加路径导航，指定的目录被解释成当前源码路径的相对路径，找头文件专用，.cpp文件一般是libraries

include_directories("/usr/include/eigen3")

8，自动找包，找到库就把头文件路径和库文件路径赋值给下面两个语句中的  定义名_INCLUDE_DIRS、 定义名_LIBRARIES

find_package(Pangolin REQUIRED) //找包并赋予给句柄（定义名）
                                               
include_directories(${Pangolin_INCLUDE_DIRS})//头文件  

target_link_libraries(6 ${Pangolin_LIBRARIES})//库（源文件）
