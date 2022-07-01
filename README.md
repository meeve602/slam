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

5，添加库(静态库)

      add_library( 2 2.cpp ) 

共享库

      add_library( 2 SHARED 2.cpp ) 

6，添加库需要连接库

      target_link_libraries( 1 2 )

7，添加路径导航，指定的目录被解释成当前源码路径的相对路径，找头文件专用，.cpp文件一般是libraries

      include_directories("/usr/include/eigen3")

8，自动找包，找到库就把头文件路径和库文件路径赋值给下面两个语句中的  定义名_INCLUDE_DIRS、 定义名_LIBRARIES

      find_package(Pangolin REQUIRED) //找包并赋予给句柄（定义名）
                                               
      include_directories(${Pangolin_INCLUDE_DIRS})//头文件  

      target_link_libraries(6 ${Pangolin_LIBRARIES})//库（源文件）

9，设置目标的属性，该命令的语法是列出想要更改的所有目标，然后提供接下来想要设置的值。您可以使用该命令任何所需的键值对，然后使用get_property()或get_target_property()命令提取它

按照一般的习惯，静态库名字跟动态库名字应该是一致的，只是扩展名不同；
 
即：静态库名为 libhello.a； 动态库名为libhello.so ；
 
所以，希望 "hello_static" 在输出时，不是"hello_static"，而是以"hello"的名字显示，故设置如下：
 
      SET_TARGET_PROPERTIES (hello_static PROPERTIES OUTPUT_NAME "hello")
 
      GET_TARGET_PROPERTY (OUTPUT_VALUE hello_static OUTPUT_NAME)
 
      MESSAGE (STATUS "This is the hello_static OUTPUT_NAME: " ${OUTPUT_VALUE})

可以拥有属性(property)的主体有以下几种：

源文件(source file)

目录(directory)

target：cmake可构建三种 target files : archive, library, 和 runtime. 

Executables 总是 runtime targets. 

Static libraries 总是 archive targets. 

Module libraries总是 library targets. 

对 non-DLL 平台，shared libraries 是 library targets. 

对 DLL 平台, DLL 是 runtime target, 对应的导入库是 archive target. All Windows-based systems including Cygwin 都是 DLL 平台.

全局属性(global)

源文件属性：

COMPILE_DEFINITIONS 编译此源文件时的预处理定义

COMPILE_FLAGS 编译此源文件时的编译选项

目录属性：

EXCLUDE_FROM_ALL 将此目录排除在默认build target以外

target属性：

RUNTIME_OUTPUT_DIRECTORY runtime target 的输出目录

全局属性：

PACKAGES_FOUND cmake运行过程中找到的包

PACKAGES_NOT_FOUND cmake运行过程中没有找到的包

例如：CMake 中像我们提供了 CMAKE_CXX_FLAGS、CMAKE_C_FLAGS 这样的标志来选择C++/C版本的编译标志

set_target_properties(Acrodictlibre PROPERTIES COMPILE_FLAGS "-DUSE_ACRODICT" )

10，选择编译

      option(<variable> "<help_text>" [value])

      option(A "option_complie_and_<A>_value_is_<NO>" NO)//除了ON其他都是OFF
   
11，分支语句（配合option，也可通过set）

      if (A)
   
         message(STATUS "TEST_OPTION defined: " ${TEST_OPTION})
   
      else ()
   
         message(STATUS "TEST_OPTION un-defined: " ${TEST_OPTION})
   
      endif()
   
可以使用-D+选项名称，修改选项的值
   
      cmake  .. -DA=OFF
   
通过判断选项的值，可以通过 add_definitions()定义相关的宏，已达到控制C程序条件编译流程   
   
如果TEST_OPTION选项的值是ON，那么就会定义TEST_OPTION宏，这样在test.c中就可以通过判断TEST_OPTION的声明情况，来控制编译流程。

      #ifdef TEST_OPTION
              printf("Hello, CMake.\n");
      #endif

这里，如果TEST_OPTION宏被定义，那么test就会打印"Hello，CMake.

12,INSTALL命令

见install command.md

concept:指定路径把源文件安装在指定目录下，如 头文件 usr/include...... 缓存文件 /bin...... 使其类似于apt-get install 安装路径 

      install(TARGETS Acrodictlibre acrodict 
          RUNTIME DESTINATION bin 
          LIBRARY DESTINATION lib
          ARCHIVE DESTINATION lib/static)
      install(FILES acrodict.h DESTINATION include)
13,控制安装路径 （Controlling installation destination）

command:

      cmake --help-variable CMAKE_INSTALL_PREFIX
      
CMakeList.txt:  

      set(CMAKE INSTALL PREFIX /home/eric/testinstal)
      
      
