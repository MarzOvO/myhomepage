# MarzOvO · 李悦萌的个人主页

中英文简历网站，使用原生 HTML、CSS、JavaScript，托管于 GitHub Pages。

- 中文：https://marzovo.top/
- English: https://marzovo.top/en/
- 无后端、数据库、第三方字体、前端依赖、访客统计或跟踪脚本。
- 响应式布局、中文 / English 切换（保留所在章节）、深浅色主题、可展开详情、邮箱复制、中英文 PDF 简历下载。
- 内容来自本人提供的简历；保留真实照片。首页省略年龄、生日及政治相关信息；下载的原始中文简历包含原始完整内容。
- 英文公司及荣誉名称为对应中文内容的翻译，不代表独立核实的官方译名。

## 内容更新

在 `scripts/build.py` 中修改中英文文案，执行 `python scripts/build.py`，同时提交生成的 `index.html` 和 `en/index.html`。脚本仅使用 Python 标准库。部署直接使用已生成的静态文件，无需在 GitHub 安装 Python 或运行构建。

样式：`assets/style.css`；交互：`assets/site.js`；主题初始化：`assets/theme.js`。替换 `assets/portrait.jpg` 或 `assets/resume-zh.pdf` 即可更新照片及下载文件。

项目区包含 AI 投资研究 Agent、MEMS 单细胞研究、PLC 自适应交通信号灯、智能篮球直播四个项目。投资 Agent 的起始月份尚未指定，统一显示为 `2025 — 至今` / `2025 — Present`。

英文网页按英文阅读习惯表达。英文下载文件为 `assets/resume-en.pdf`，包含四个项目；中文下载文件仍为用户提供的原始 PDF，未随网页内容改写。英文 PDF 的内容和排版维护在 `scripts/build_resume.py` 中，与网页文案分别维护；更新后执行以下命令并提交生成的 PDF（仅 PDF 生成需要 ReportLab，网站运行及部署不需要）：

```sh
python -m pip install reportlab
python scripts/build_resume.py
```

## 本地预览

在仓库根目录运行 `python -m http.server 8080 --bind 127.0.0.1`，访问 http://127.0.0.1:8080/ 。

## GitHub Pages

沿用 main 分支根目录发布和 `CNAME` 中的 `marzovo.top`。`.nojekyll` 保证静态资源直接发布。保留现有域名 DNS 配置。更新 main 后等待 Pages 完成部署即可。若首次配置，请在仓库 Settings → Pages 中选择 Deploy from a branch、main、/(root)，填写自定义域名并开启可用的 HTTPS。

站内只在本机 localStorage 保存主题偏好 `marzovo-theme`，不会上传该偏好。联系按钮调用邮件客户端，不会自动发送邮件。
