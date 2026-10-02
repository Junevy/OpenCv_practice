# OpenCV 入门示例

按 `01_start.ipynb` 的 Markdown 功能标题拆分，原文件保留。
每个文件都包含自己的导入及图像读取代码，可重启内核后直接“运行全部”，无需先运行其他 Notebook。

## 运行环境

选择 **OpenCV (Python 3.14.7)** 内核，对应 `07_opencv/.venv/Scripts/python.exe`。
根目录 `.venv` 没有 OpenCV，请使用上述内核。

图片统一读取与 `01_start` 同级的 `../img` 文件夹：`img` 和 `img1` 使用 `img1.jpg`，`img2` 使用 `img2.jpg`，形态学使用 `templ.png`。阈值和滤波只读取 `img1`。
代码兼容从工作区根目录、`07_opencv` 或 `01_start` 目录运行。
图片无法读取时会明确报错，不会用其他图片代替。
彩色图像保持 OpenCV 的 BGR 顺序，只在 Matplotlib 显示时转为 RGB。
保存示例会写入当前工作目录下的 `opencv_demo_output/saved_image.jpg`，重复运行会更新该演示文件。

## 文件目录

| 文件 | 功能 |
| --- | --- |
| [02_read_image.ipynb](02_read_image.ipynb) | 读取图像 |
| [03_show_image.ipynb](03_show_image.ipynb) | 显示图像 |
| [04_save_image.ipynb](04_save_image.ipynb) | 保存图像 |
| [05_pixel_value.ipynb](05_pixel_value.ipynb) | 读取和修改像素 |
| [06_roi.ipynb](06_roi.ipynb) | 图像区域 ROI |
| [07_split_bgr.ipynb](07_split_bgr.ipynb) | 拆分 BGR 通道 |
| [08_merge_bgr.ipynb](08_merge_bgr.ipynb) | 合并 BGR 通道 |
| [09_resize_translation_rotate_flip.ipynb](09_resize_translation_rotate_flip.ipynb) | 缩放、平移、旋转、翻转 |
| [10_image_calculate.ipynb](10_image_calculate.ipynb) | 相加、相减、加权融合 |
| [11_threshold.ipynb](11_threshold.ipynb) | 固定阈值、自适应阈值、Otsu 阈值 |
| [12_blurry.ipynb](12_blurry.ipynb) | 均值、高斯、中值滤波 |


## 练习目录

`../02_excrcise` 包含以下独立练习：

- `01_laplacian.py`：用 Laplacian 方差观察清晰度。
- `02_template_match.ipynb`：模板匹配与旋转模板实验。
- `03_match_test.py`：带掩膜的旋转模板匹配脚本。
- `04_img_joint.py`：SIFT 特征匹配实验；脚本包含 GUI 显示，需要桌面环境。

练习输入图片也位于 `../img`。
