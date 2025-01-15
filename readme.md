# 软件介绍
- 生成DNA barcode 序列，并生成对应的 txt 文件
- 用户指定 DNA barcode 的序列长度，并指定 DNA barcode 的序列数量, 并指定 DNA barcode 之间的最小距离
- GUI 界面

# 依赖
- ArnaudDroitLab/DNABarcodes R 包
- python 3.10
- R 4.3.1

# 安装说明
- ## 1. 安装 R 4.3.1
+ ## 1. 使用 Anaconda 安装环境
+ 推荐使用 Anaconda 安装所有依赖，这样可以更好地管理环境。
+ 
+ ### 创建新环境
+ 在 Windows PowerShell 中运行：
+ ```powershell
+ # 创建新的环境
+ conda create -n dna_barcode python=3.10 r-base=4.3.1 r-essentials rpy2
+ 
+ # 激活环境
+ conda activate dna_barcode
+ ```
+ 
+ ### 或在现有环境中安装
+ ```powershell
+ # 在现有环境中安装依赖
+ conda install -c conda-forge python=3.10 r-base=4.3.1 r-essentials rpy2
+ ```

## 2. 安装 R 包
在激活的环境中运行 R：
```powershell
R
```

在 R 控制台中运行：
```R
install.packages("DNABarcodes")
# 如果弹出镜像选择窗口，选择一个距离近的镜像即可
```

## 3. 验证安装
在 PowerShell 中运行：
```powershell
# 确保在正确的环境中
conda activate dna_barcode

# 启动 Python
python
```

然后运行以下代码验证安装：
```python
import rpy2.robjects as robjects
# 如果没有报错，说明 rpy2 安装成功

# 测试 R 包是否可用
robjects.r('library(DNABarcodes)')
# 如果没有报错，说明 R 包安装成功
```

# 使用说明
[这里添加如何使用软件的基本步骤]

# 注意事项
[这里添加使用软件时需要注意的事项]

# 开发者文档

详细的开发文档请参见 [开发文档](docs/development.md)

## 项目结构
请参考开发文档中的项目结构说明。



