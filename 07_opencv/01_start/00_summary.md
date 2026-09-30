# OpenCV `01_start` 内容总结

本文件夹按功能将 OpenCV 入门示例拆分为 01–13 个 Notebook。每个 Notebook 都可以单独运行；图像操作使用 OpenCV，结果显示使用 Matplotlib。

## 共用数据与运行约定

图片统一放在与 `01_start` 同级的 `07_opencv/img` 文件夹。以下相对路径以 Notebook 所在目录为基准；代码也兼容从工作区根目录或 `07_opencv` 目录运行。

- `img`：彩色图像，路径为 `../img/img1.jpg`。
- `img1`：灰度图像，路径为 `../img/img1.jpg`。
- `img2`：灰度图像，路径为 `../img/img2.jpg`。
- `morphology` 示例使用 `../img/templ.png`。
- `cv2.imread` 读取的彩色图像默认是 BGR 顺序；使用 Matplotlib 显示前要通过 `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` 转为 RGB。
- 图像数组的形状通常为 `height × width × channel`，像素索引采用 `image[row, column]`。
- 建议选择 `OpenCV (Python 3.14.7)` 内核，对应 `07_opencv/.venv`。

## Notebook 功能

| 编号 | 文件 | 内容总结 |
| --- | --- | --- |
| 01 | `01_start.ipynb` | 原始综合示例：导入 OpenCV、读取/显示/保存图像、读取像素、ROI、BGR 通道拆分与合并、缩放、旋转、平移、翻转、图像加减与加权融合、阈值分割和模糊滤波。 |
| 02 | `02_read_image.ipynb` | 使用 `cv2.imread` 读取彩色图像，检查读取结果、类型、形状、数据类型和 OpenCV 版本。读取失败时抛出 `FileNotFoundError`。 |
| 03 | `03_show_image.ipynb` | 将 BGR 图像转换为 RGB，并用 `plt.imshow`、`plt.axis('off')` 显示。 |
| 04 | `04_save_image.ipynb` | 使用 `cv2.imwrite` 保存图像到 `opencv_demo_output/saved_image.jpg`，再读回文件并检查形状，验证保存是否成功。 |
| 05 | `05_pixel_value.ipynb` | 通过行列坐标读取像素的 BGR 值；复制图像后将指定像素改为白色，观察像素修改结果。 |
| 06 | `06_roi.ipynb` | 使用 NumPy 切片选取中心区域 ROI，并将 ROI 填充为绿色；演示 ROI 与原图数组切片的关系。 |
| 07 | `07_split_bgr.ipynb` | 使用 `cv2.split` 拆分 B、G、R 三个单通道图像，并以灰度形式分别显示。 |
| 08 | `08_merge_bgr.ipynb` | 使用 `cv2.merge` 合并 B、G、R 通道，并用数组断言确认合并结果与原图一致。 |
| 09 | `09_resize_translation_rotate_flip.ipynb` | 使用 `cv2.resize` 缩放；使用 `cv2.getRotationMatrix2D` 和 `cv2.warpAffine` 旋转；使用平移矩阵平移；使用 `cv2.flip` 垂直翻转，并集中对比显示结果。 |
| 10 | `10_image_calculate.ipynb` | 读取两张灰度图像，使用 `cv2.add` 相加、`cv2.subtract` 相减、`cv2.addWeighted` 按权重融合。两张图像需要具有相同尺寸。 |
| 11 | `11_threshold.ipynb` | 对 `img1` 执行固定阈值、均值自适应阈值和 Otsu 自动阈值；输出均为二值图像，像素值通常为 0 或 255。 |
| 12 | `12_blurry.ipynb` | 使用均值滤波 `cv2.blur`、高斯滤波 `cv2.GaussianBlur`、中值滤波 `cv2.medianBlur` 和双边滤波 `cv2.bilateralFilter`，比较不同平滑方法的效果。 |
| 13 | `13_morphology.ipynb` | 创建 `15×15` 的 `uint8` 结构元素，演示腐蚀 `cv2.erode`、膨胀 `cv2.dilate`、开运算 `MORPH_OPEN`、闭运算 `MORPH_CLOSE`，以及原图与闭运算结果的差异。 |

## 处理流程速记

```text
彩色图像
  ├─ 读取与显示：imread → BGR/RGB 转换 → imshow
  ├─ 像素与区域：image[row, column] → ROI 切片
  ├─ 通道操作：split → 单通道处理 → merge
  └─ 几何变换：resize / rotate / translate / flip

灰度图像
  ├─ 算术运算：add / subtract / addWeighted
  ├─ 二值化：threshold / adaptiveThreshold / Otsu
  ├─ 平滑：mean / Gaussian / median / bilateral
  └─ 形态学：erosion / dilation / opening / closing
```

## 运行注意事项

1. `cv2.imread` 返回 `None` 时应先检查路径，再进行 `cvtColor`、切片或滤波。
2. OpenCV 的彩色通道顺序是 BGR，Matplotlib 的常用显示顺序是 RGB，二者不能直接混用。
3. 自适应阈值的窗口大小必须是大于 1 的奇数；中值滤波的核大小也应使用正奇数。
4. 图像加减和加权融合要求输入图像尺寸一致；不同尺寸需要先用 `cv2.resize` 对齐。
5. 形态学操作的结构元素大小决定处理范围；结构元素越大，腐蚀、膨胀和开闭运算效果越明显。
6. `13_morphology.ipynb` 中图像由 `cv2.imread` 读取，若按 OpenCV 的实际通道顺序处理，彩色转灰度建议使用 `cv2.COLOR_BGR2GRAY`。
