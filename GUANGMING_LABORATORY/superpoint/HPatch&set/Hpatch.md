# HPatch测试使用手册

--jx

检测描述子的性能

## 1.数据集介绍

**测试任务**

图像补丁验证 verification 衡量描述符区分程度

 图像匹配衡量描述子匹配程度

补丁检索衡量从大集合中检索的性能

## 2.数据集结构

**hpatches-sequences-release文件夹** 
i代表light光照变化 v代表viewpoint视角变化
每一个子文件,是一个图片序列,像Mikolajczyk数据集一样,含有H矩阵

**hpatches-release文件夹**

116个子文件夹(和hpatches-sequences-release一样),代表116个图像序列提取的patches

从sequences文件夹中第一张参考图像提取的patches保存为ref.png

ref.png:宽度表示patches的边长，高度/边长=patches的个数

e\h\t前缀分别表示噪声程度easy、hard和tough

jitter文件包含给patch添加的几何噪声，

rot --rotation

ani --anisotropic各向异性

sc --scale

tr --translation 

**descriptor文件夹**

保存各类算法提出的描述子，每个csv都是N*D的文件，N是patch数量，D是描述子维度



## 3.数据集使用

使用splits.json进行数据集拆分

| 分割名称 | 训练集       | 测试集                 |
| -------- | ------------ | ---------------------- |
| a        | 随机混合     | 随机混合               |
| b        | 随机混合     | 随机混合               |
| c        | 随机混合     | 随机混合               |
| illum    | viewpoint    | illumination           |
| view     | illumination | viewpoint              |
| full     | --           | viewpoint+illumination |

### 3.1 自带特征测试

```shell
pip install -r utils/requirements.txt --user
sudo apt-get install libopencv-dev python-opencv
```
加载/可视化数据集
```shell
python hpatches_vis.py
```
评估描述符

```
python hpatches_eval.py --descr-name=sift --task=verification --delimiter=";"
```

查看结果

```
python hpatches_results.py --descr=sift --results-dir=results/ --task=verification
```

SIFT - Balanced variant (auc) 
Noise       Inter     Intra

-------  --------  --------
Easy     0.930915  0.909937
Hard     0.823407  0.795857
Tough    0.730735  0.705034
SIFT - Imbalanced variant (ap) 
Noise       Inter     Intra
-------  --------  --------
Easy     0.84945   0.783138
Hard     0.656835  0.569733
Tough    0.512454  0.42948



### 3.2 添加自定义特征测试

测试superpoint

i_leuven is error

