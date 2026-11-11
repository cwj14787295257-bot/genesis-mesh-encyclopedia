# NIRVANA · 网子雾化器图鉴 · Genesis Mesh Atomizer Encyclopedia

[![Deploy to GitHub Pages](https://github.com/cwj14787295257-bot/genesis-mesh-encyclopedia/actions/workflows/deploy.yml/badge.svg)](https://github.com/cwj14787295257-bot/genesis-mesh-encyclopedia/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-31%2F31%20PASS-brightgreen.svg)](scratch/verify_and_audit_catalog.py)

**在线访问地址**：[https://cwj14787295257-bot.github.io/genesis-mesh-encyclopedia/](https://cwj14787295257-bot.github.io/genesis-mesh-encyclopedia/)

---

## 项目简介

本项目收录并整理了全球经典 Genesis（纯金属网导油）雾化器的机械结构、规格参数、做芯指南与历史出处。全馆共收录 80 款正品独立工坊代表型号，涵盖早期拓荒鼻祖、俄系钛合金代表作、欧美独立工坊作品以及国内独立原创设计。

每款雾化器均包含：
- **物理规格**：外形直径、本体高度、油仓容量、主体材质、导油介质与孔径、进气规格、电极平台形式等；
- **真实影像**：单款收录 3 至 6 张高清单体棚拍、甲板微距与爆炸拆解实拍；
- **做芯指南**：针对不同型号油路与导电特性的卷网氧化操作说明与发热丝缠绕建议；
- **文献出处**：溯源自 eCigTalk、ECF、UK Vapers、Modder 官方手作工坊论坛档案，提供一手历史出厂信息与交叉验证材料。

---

## 核心功能

1. **双模浏览视图**：
   - **卡片网格模式**：适合快速浏览图库、规格参数与品牌分类；
   - **时间轴编年史模式**：按 2012 至 2024 年真实历史演进排布，支持年份吸顶快速导航与时间正逆序切换，附设年代待考证专区。
2. **多维检索与分类**：
   - 品牌快捷筛选（Paravozz、BLM、国内原创、欧美高阶等）；
   - 全局模糊搜索（支持型号名、别名、工坊主理人、材质与技术规格）。
3. **沉浸式交互模态窗**：
   - 支持键盘方向键切换多角度实拍图与全屏灯箱放大；
   - 参数面板、设计亮点、双模做芯指南与文献考据证据链分区清晰。

---

## 项目结构

```text
genesis-mesh-encyclopedia/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions 自动化测试与 Pages 发布工作流
├── images/                     # 282 张全实拍图库
├── scratch/
│   └── verify_and_audit_catalog.py  # 29 大质量验收与数据规范自动化测试套件
├── .gitignore                  # Git 忽略配置
├── .nojekyll                   # 禁用 Jekyll 纯静态发布标记
├── generate_html.py            # 数据字典与静态网页编译生成脚本
├── index.html                  # 编译生成的全功能单页静态展示站点
├── LICENSE                     # MIT 开源许可证
└── README.md                   # 项目说明文档
```

---

## 本地运行与开发

无需安装第三方依赖，仅需系统自带 Python 3 环境：

1. **克隆仓库**：
   ```bash
   git clone https://github.com/cwj14787295257-bot/genesis-mesh-encyclopedia.git
   cd genesis-mesh-encyclopedia
   ```

2. **重新编译静态页面**：
   ```bash
   python3 generate_html.py
   ```

3. **运行全馆 29 大质量验收测试**：
   ```bash
   python3 scratch/verify_and_audit_catalog.py
   ```

4. **本地预览**：
   直接在浏览器中打开 `index.html`，或启动本地 HTTP 服务：
   ```bash
   python3 -m http.server 8080
   ```
   随后在浏览器访问 `http://localhost:8080`。

---

## 质量把控标准

项目设置了 29 项自动化校验规则，持续集成于 GitHub Actions：
- 全馆 80 款数据字段完整性与双源交叉验证；
- 282 张图片 100% 纯实拍与跨型号 MD5 碰撞审查（杜绝跨型号重图）；
- 严格杜绝仿品黑话与克隆混淆，维护独立工坊原创设计记录；
- 遵循严谨客观的技术说明文风，清理主观夸大与 AI 写作痕迹。

---

## 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。
