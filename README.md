# Python 学习项目

这是一个按学习路线整理的 Python 实践项目，内容从 Python 基础逐步扩展到文件处理、标准库、虚拟环境、Pillow、NumPy 和 OpenCV 图像处理。

## 目录概览

| 目录 | 内容 |
| --- | --- |
| `01Primary` | Python 基础语法、函数、高阶函数、装饰器、生成器、面向对象、枚举、异常和单元测试 |
| `02io` | 字符串 IO、字节 IO、序列化与反序列化（Marshal、JSON） |
| `03inner_module` | `datetime`、`namedtuple`、`Counter`、迭代器等 Python 标准库模块 |
| `04_venv` | Python 虚拟环境相关实验 |
| `05_pillow` | Pillow 图像处理练习 |
| `06_numpy` | NumPy 数组基础、索引、变形、拼接、广播、运算、随机数和综合练习 |
| `07_opencv` | OpenCV 图像读取、显示、保存、像素、ROI、通道、几何变换、图像运算、阈值、滤波和形态学处理 |

## 推荐学习顺序

```text
Python 基础
    ↓
文件与标准库
    ↓
虚拟环境与图像基础
    ↓
NumPy 数组
    ↓
OpenCV 图像处理
    ↓
PyTorch / YOLO 等深度学习方向
```

建议先学习 `01Primary`，再阅读 `02io` 和 `03inner_module`；完成 NumPy 基础后进入 `06_numpy`，最后使用 `07_opencv` 将数组操作应用到真实图像。

## 环境与运行

项目使用 Python 3.14 虚拟环境。根目录环境位于：

```text
.venv\Scripts\python.exe
```

在 VS Code 中打开项目根目录后，可以直接运行 `.py` 文件或打开 `.ipynb` Notebook。Notebook 建议选择与具体目录对应的虚拟环境：

- 通用 Python / NumPy：根目录 `.venv` 或对应子目录的 `.venv`
- OpenCV：`07_opencv/.venv`，选择内核 **OpenCV (Python 3.14.7)**

启动 Jupyter：

```powershell
.venv\Scripts\jupyter.exe notebook
```

## OpenCV 示例

OpenCV 示例位于 [`07_opencv/01_start`](07_opencv/01_start)。其中：

- [`summary.md`](07_opencv/summary.md) 记录 01–16 个 Notebook 和 `02_excrcise` 练习的知识点。
- `02_read_image.ipynb` 至 `16_histogram.ipynb` 按功能拆分，均可单独运行；原始综合示例 `01_start.ipynb` 保留。
- `02_excrcise` 包含清晰度评价、模板匹配、SIFT 特征匹配和图像拼接练习。
- 示例图片统一放在 [`07_opencv/img`](07_opencv/img)，包括 `img1.jpg`、`img2.jpg` 和 `templ.png`。
- 详细运行说明见 [`07_opencv/01_start/README.md`](07_opencv/01_start/README.md)。

## 说明

这是一个持续整理中的学习项目，Notebook 以实验和演示为主。运行 Notebook 时建议使用“运行全部”并从头执行，避免因前序变量尚未创建而出现 `NameError`。

## 隐私与提交规范

仓库不应提交本机绝对路径、密钥、令牌、个人数据或生成文件。示例代码使用项目相对路径；运行产物和常见凭据文件已加入 [`.gitignore`](.gitignore)。如果敏感内容已经推送到 GitHub，请先立即撤销或轮换凭据，再按下方的历史清理流程处理提交记录。
