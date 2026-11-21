# 第三方素材与许可说明 · Third-Party Notices

本项目源码以 MIT 许可发布（见 `LICENSE`）。但 `index.html` 是单文件分发，里面内联了若干第三方资源，**这些资源不适用 MIT 许可**，商业使用或再分发前请逐项确认。

---

## 1. Three.js

- 文件：`index.html` 内联的压缩构建（`<script>` 中 `three` bundle）
- 许可：MIT License — https://github.com/mrdoob/three.js/blob/dev/LICENSE
- 用法：3D 场景、几何体、材质与渲染管线
- 要求：保留版权与许可声明（MIT 原文已包含在上游 LICENSE 中）

## 2. 元素影像精灵图（element specimen images）

- 文件：`index.html` 中的 `window.ELEMENT_SPRITE`（data URL，JPEG 精灵图，4000×3000）
- 来源：**images-of-elements.com**（https://images-of-elements.com/），每张图片的原始页面记录在 `window.ELEMENT_IMAGES[*].page` 中，并在应用内元素详情面板的「来源」链接处可点击跳转
- 许可：**上游站点对图片的使用条款需自行核验**；本仓库不为其授予任何许可，也未做二次创作声明
- 建议：
  - 个人学习 / 展示用途：保留来源链接与署名
  - 商业 / 公开发行：请替换为自己拍摄或明确可商用的图片（CC0 / Public Domain），或直接删除影像模块（`renderElementPhoto` 会因缺少 `meta` 自动降级隐藏）

## 3. HarmonyOS Sans 字体

- 文件：`index.html` 中的两处 `@font-face` data URL（`font/woff2`）
- 版权：华为技术有限公司
- 许可：**不是开源字体**。华为对外提供下载并允许在华为设备生态内使用，但字体的再分发 / 内嵌到公开仓库 / 商用需要按其许可条款确认
- 建议：
  - 公开仓库可保留（用于演示），但请在 README 与本文件中明确标注来源与版权
  - 若要发布到应用商店或商业产品：替换为开源字体（如 Noto Sans SC、思源黑体 / Source Han Sans，SIL OFL）或直接回退系统字体
- 替换方式：删除两段 `@font-face` 的 `src: url(data:font/woff2;base64,...)`，`font-family` 声明保留，浏览器会自动回退到 `PingFang SC` / `Microsoft YaHei` 等系统字体

## 4. 元素数据

- 元素符号、中英文名、原子序数、相对原子质量、电子排布、发现年代与发现者、相态温度阈值等，整理自公开资料（IUPAC 元素数据、公开百科条目）
- 化合物条目（名称、化学式、类别、用途）为整理性描述，未逐条引用单一来源
- 这些数据本身通常不受版权保护（事实性数据），但**汇编结构**可能涉及数据库权利，商用前请自行评估

## 5. 其他

- 图标、渐变、动效均为本项目自行绘制 / 生成（Canvas 或 CSS），未使用第三方图标库
- 若你 fork 本仓库并替换了上述素材，建议在 README 中同步更新本节说明

---

最后更新：2026-11
