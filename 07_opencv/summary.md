# OpenCV `01_start` 内容总结

本文件夹按功能整理 OpenCV 入门示例与练习。`01_start` 包含原始综合 Notebook 和按功能拆分的 02–16 号 Notebook；`02_excrcise` 包含清晰度评价、模板匹配、特征匹配和图像拼接练习；图片统一放在 `img`。图像操作使用 OpenCV，结果显示使用 Matplotlib。

## 共用数据与运行约定

图片统一放在与 `01_start` 同级的 `07_opencv/img` 文件夹。以下相对路径以 Notebook 所在目录为基准；代码也兼容从工作区根目录或 `07_opencv` 目录运行。

- `img`：彩色图像，路径为 `../img/img1.jpg`。
- `img1`：灰度图像，路径为 `../img/img1.jpg`。
- `img2`：灰度图像，路径为 `../img/img2.jpg`。
- `LinuxLogo.jpg`：轮廓检测示例图，供 `15_contour_inspect.ipynb` 使用。
- `smarties.png`：彩色直方图示例图，供 `16_histogram.ipynb` 使用。
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
| 13 | `13_morphology.ipynb` | 创建 `15×15` 的 `uint8` 结构元素，演示腐蚀 `cv2.erode`、膨胀 `cv2.dilate`、开运算 `MORPH_OPEN`、闭运算 `MORPH_CLOSE`，以及形态学梯度和原图与闭运算结果的差异。 |
| 14 | `14_edge_detect.ipynb` | 使用 Canny 检测边缘并膨胀结果；使用 Sobel 分别计算 x、y 方向梯度和组合梯度；使用 Laplacian 计算二阶边缘响应，并统计响应的最大值、均值和形状。 |
| 15 | `15_contour_inspect.ipynb` | 将 `LinuxLogo.jpg` 二值化后查找轮廓，查看层级关系，绘制轮廓，按面积筛选轮廓，计算周长，并演示外接矩形、最小外接旋转矩形和最小外接圆。 |
| 16 | `16_histogram.ipynb` | 计算灰度直方图，演示直方图均衡化；分别统计彩色图像的 B、G、R 直方图；转换到 YCrCb 空间观察亮度通道处理；使用 `cv2.compareHist` 计算两张灰度图直方图的相关性。 |

## `02_excrcise` 练习

| 文件 | 内容总结 |
| --- | --- |
| `01_laplacian.py` | 从 `img1.jpg` 截取 ROI（行 `600:2000`、列 `3000:4000`），计算原图和不同高斯核（3、7、11、15、19、23）模糊结果的 Laplacian 方差，并通过 OpenCV 窗口显示最后一次结果。 |
| `02_template_match.ipynb` | 读取 `cards.png` 和 `poker.png`，按 ROI 尺寸缩放模板，使用 `cv.matchTemplate` 做灰度模板匹配，并尝试旋转模板后比较匹配分数。 |
| `03_match_test.py` | 将 `cards.png` 中的模板按 0–359 度旋转，使用带掩膜的 `cv.matchTemplate` 计算匹配分数并输出最高分角度。 |
| `04_img_joint.py` | 将 `pic1.png` 切成上下两个区域，使用 SIFT 提取特征并通过 BFMatcher 的 KNN 比率测试筛选匹配点；当前脚本仍使用 `cv.imshow`，需要 GUI 环境。 |

## 新增练习的输入与状态

| 输入图片 | 用途 |
| --- | --- |
| `cards.png`、`poker.png` | 模板匹配 |
| `pic1.png` | SIFT 特征匹配与图像拼接练习 |

这些练习使用与 `01_start` 相同的 OpenCV 内核。运行前请确认当前工作目录能解析到 `07_opencv/img`；Notebook 推荐在 `07_opencv` 目录或仓库根目录启动。模板匹配 Notebook 已保留实验代码，旋转模板部分会产生较多候选角度，适合逐步查看分数而不是一次性绘制所有结果。

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

边缘与结构
  ├─ 边缘检测：Canny / Sobel / Laplacian
  ├─ 轮廓分析：findContours / contourArea / arcLength
  ├─ 几何包围：boundingRect / minAreaRect / minEnclosingCircle
  └─ 清晰度评价：Laplacian 方差

灰度分布
  ├─ 直方图：calcHist
  ├─ 对比度增强：equalizeHist
  ├─ 彩色通道统计：B / G / R
  └─ 图像比较：compareHist

场景选择
  ├─ 椒盐噪声 -> 中值滤波
  ├─ 高频随机噪声 -> 高斯滤波
  ├─ 光照不均 -> 自适应阈值 / 背景校正
  ├─ 小黑点 -> 开运算等
  ├─ 小孔洞 -> 闭运算 / fill
  ├─ 对比度很差 -> 中值滤波
  ├─ 灰度分布太集中 -> 均衡化可能有用
  ├─ 前景背景灰度明显不同 -> threshold
  ├─ 成像质量监控 -> Mean | StdDev | CompareHist | Laplacian 方差
  └─ 不知道阈值选多少 -> 直方图 / Otsu
```

## 运行注意事项

1. `cv2.imread` 返回 `None` 时应先检查路径，再进行 `cvtColor`、切片或滤波。
2. OpenCV 的彩色通道顺序是 BGR，Matplotlib 的常用显示顺序是 RGB，二者不能直接混用。
3. 自适应阈值的窗口大小必须是大于 1 的奇数；中值滤波的核大小也应使用正奇数。
4. 图像加减和加权融合要求输入图像尺寸一致；不同尺寸需要先用 `cv2.resize` 对齐。
5. 形态学操作的结构元素大小决定处理范围；结构元素越大，腐蚀、膨胀和开闭运算效果越明显。
6. `13_morphology.ipynb` 中图像由 `cv2.imread` 读取，若按 OpenCV 的实际通道顺序处理，彩色转灰度建议使用 `cv2.COLOR_BGR2GRAY`。
7. `14–16` 和 `02_excrcise/01_laplacian.py` 当前包含以工作区根目录为基准的图片路径；从其他目录启动 Notebook 或脚本前，应先确认 `07_opencv/img` 能被读取。
8. `15_contour_inspect.ipynb` 的最小外接矩形示例应将角点数组转换为整数后再绘制；常用写法是 `bx = bx.astype(np.int32)`。
9. `02_excrcise/01_laplacian.py` 使用 `cv2.imshow`、`waitKey` 和 `destroyAllWindows`，需要支持 GUI 的运行环境。
