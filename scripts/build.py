"""Build the two static pages. Python 3 standard library only."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
LANG = 0

def t(zh, en):
    return zh if LANG == 0 else en

def pills(items):
    return '<div class="pills">' + ''.join(f'<span>{escape(x)}</span>' for x in items) + '</div>'

def bullets(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def heading(number, zh, en, note=''):
    return f'<div class="section-heading"><h2><span class="section-number">{number}</span>{t(zh,en)}</h2><span class="section-note">{note}</span></div>'

def entry(title, role, date, summary, details, tags=()):
    return f'''<article class="card entry"><div class="entry-heading"><div><h4>{title}</h4><p class="role">{role}</p></div><span class="date">{date}</span></div><p>{summary}</p>{pills(tags) if tags else ''}<details><summary>{t('展开详情','Read more')}<span aria-hidden="true">＋</span></summary><div class="detail-content">{bullets(details)}</div></details></article>'''

def build():
    base = '' if LANG == 0 else '../'
    locale = t('zh-CN','en')
    name = t('李悦萌','Yuemeng Li')
    nav = [('about',t('关于我','About')),('experience',t('经历','Experience')),('projects',t('项目','Projects')),('skills',t('技能','Skills')),('honors',t('荣誉','Honors')),('contact',t('联系','Contact'))]
    title = t('李悦萌 | 工程 · 研究 · 项目实践','Yuemeng Li | Engineering, Research & Projects')
    description = t('李悦萌的个人主页。北京化工大学控制科学与工程硕士生，关注 MEMS、自动化控制、数据分析与项目协作。','Yuemeng Li’s portfolio: a master’s student at BUCT with projects in microchips, automation, computer vision and AI, plus experience in product and project support.')
    educations = [
        entry(t('北京化工大学','Beijing University of Chemical Technology'), t('控制科学与工程 · 硕士 · 推免录取','Master’s in Control Science and Engineering · Admitted by recommendation'), t('2024.09 — 2027.07（预计）','Sep 2024 — Jul 2027 (expected)'),t('从控制理论出发，探索微机电系统与单细胞组学的交叉研究。','Researching microchips for single-cell RNA studies, with a background in control engineering.'),[t('GPA：3.53 / 4.00，专业排名前 5%。','GPA: 3.53 / 4.00; top 5% of the cohort.'),t('主修课程：现代传感技术、微机电系统、系统辨识与建模。','Key courses: Modern Sensing Technology, Microelectromechanical Systems, System Identification and Modeling.')],['MEMS',t('前 5%','Top 5%')]),
        entry(t('北京化工大学','Beijing University of Chemical Technology'),t('自动化 · 本科','Bachelor’s in Automation'),t('2020.09 — 2024.06','Sep 2020 — Jun 2024'),t('建立自动控制、电子技术与工程实践的系统基础。','Built a foundation in automatic control, electronics and hands-on engineering.'),[t('GPA：3.52 / 4.33，专业排名前 5%。','GPA: 3.52 / 4.33; top 5% of the cohort.'),t('主修课程：自动控制原理、现代控制理论、过程控制原理、模拟电子技术、数字电子技术。','Key courses: Automatic Control Principles, Modern Control Theory, Process Control, Analog Electronics and Digital Electronics.')])]
    internships = [
        entry(t('瑞声科技','AAC Technologies'),t('项目管理实习生','Project Management Intern'),t('2026.06 — 2026.07','Jun 2026 — Jul 2026'),t('参与麦克风模组 NPI 项目，支持工程验证到量产导入。','Helped prepare a new microphone module for production, from engineering tests to production planning.'),[t('协助维护项目排期与关键节点，跟踪设计、物料、制程、设备及产线准备状态。','Updated the project schedule and tracked key tasks across design, materials, manufacturing, equipment and production lines.'),t('整理试产良率、可靠性、测试一致性及质量验证数据，跟踪关键风险与偏差问题闭环。','Organized trial-production and quality-test results. Tracked risks and followed up on problems until they were resolved.'),t('项目样品规模由约 11.8K 提升至 20K，产品配置逐步收敛；协助支持阶段推进。','Supported the project as the sample scale grew from about 11,800 to 20,000 and the product specifications became more settled.')],['NPI',t('项目协作','Project coordination'),t('风险跟踪','Risk tracking')]),
        entry(t('富士康科技集团','Foxconn Technology Group'),t('阳极线控制实习生','Anodizing Line Control Intern'),t('2022.07 — 2023.08','Jul 2022 — Aug 2023'),t('以数据驱动自动加药逻辑，参与生产线自动化控制调试。','Developed automatic chemical dosing logic and helped test controls on an anodizing production line.'),[t('监测各工序药池化学浓度，基于采集数据构建自动加药逻辑，使浓度波动降低约 16%，减少人工加药频次。','Used chemical concentration data to build automatic dosing logic. Reduced concentration fluctuations by about 16% and lowered the need for manual dosing.'),t('参与天车自动化控制调试，测试站点停留时间与运行路径，支持产品在药池间精准搬运。','Helped test the automated crane that moves products between chemical baths, checking its routes and stop times.')],[t('自动化控制','Automation'),'−16%']),
        entry(t('深圳远森光电科技有限公司','Shenzhen Yuansen Optoelectronics Technology Co., Ltd.'),t('产品实习生','Product Intern'),t('2021.07 — 2021.08','Jul 2021 — Aug 2021'),t('调研欧洲 LED / 光电市场，将竞品分析转化为产品优化建议。','Studied competing LED and optical products in Europe and suggested product improvements.'),[t('收集 30+ 竞品参数与定价数据，开展对标测试与价格弹性分析。','Collected features and prices for over 30 competing products. Compared performance and studied how price changes could affect demand.'),t('围绕竞品短板与市场空白提出优化建议，协助新品定价策略与欧洲区推广方案。','Suggested improvements based on gaps in competing products. Helped develop pricing and promotion plans for Europe.')],[t('竞品分析','Competitive analysis'),t('产品优化','Product improvement')])]
    projects = [
        (
            '01', 'AI AGENTS / DATA ANALYSIS',
            t('基于大语言模型的个人投资研究与<br>决策支持 Agent 系统', 'AI assistant for investment<br>research and decision support'),
            t('2025 — 至今 · 独立开发', '2025 — Present · Independent Developer'),
            t('整合多源金融数据、AI 研究分析与个人持仓管理，支持市场监控、投资策略生成和风险评估。',
              'Building a personal research tool that brings together financial data, AI analysis and portfolio tracking to support investment decisions.'),
            t('研究 → 决策 → 报告', 'Research → Decision → Report'),
            t('多角色 AI 协作 · 策略回测 · Web 交互', 'AI teamwork · Backtesting · Web interface'),
            ['Python', 'pi-ai', 'LLM', 'MA / MACD / RSI', t('策略回测', 'Backtesting')],
            [
                t('负责系统架构设计与开发，基于 Python 与 pi-ai 构建 Research、Decision、Report 等多角色 AI 协作流程，实现市场研究、投资决策支持及报告生成的自动化。',
                  'Designed the system in Python with pi-ai. Set up separate Research, Decision and Report agents to automate market research, decision support and report writing.'),
                t('整合股票、ETF 行情、财经新闻及政策数据，结合 MA、MACD、RSI 等技术指标与大语言模型，形成短、中、长期市场研判及持仓调整建议。',
                  'Combined stock and ETF prices, financial news and policy updates. Used indicators such as MA, MACD and RSI with a language model to assess market trends over different time frames and suggest portfolio changes.'),
                t('结合实际持仓、资金约束与风险控制规则，设计动态仓位建议、历史策略回测和决策可追溯分析机制，并开发 Web 可视化交互界面。',
                  'Built portfolio tools that account for current holdings, available funds and risk limits. Added position-size suggestions, tests on historical data, decision records and an interactive web interface.')
            ]
        ),
        ('02','MEMS / BIOINFORMATICS',t('基于 MEMS 芯片的<br>单细胞全 RNA 组学研究','Microchips for<br>single-cell RNA research'),t('2024.09 — 至今 · 项目负责人','Sep 2024 — Present · Project Lead'),t('连接芯片设计、实验验证与测序数据分析，探索单细胞全 RNA 信息的高效采集与检测。','Designing and testing MEMS microchips to collect RNA from individual cells, then processing the sequencing data.'),t('从芯片到数据','FROM CHIP TO DATA'),t('已申请国家发明专利','Chinese invention patent application filed'),['MEMS','L-Edit','PDMS','Python','Linux'],[t('负责芯片结构设计、模具光刻、PDMS 倒模及性能测试，根据实验结果持续迭代芯片与实验方案。','Designed chip layouts, made molds, cast PDMS chips and tested their performance. Used the results to improve the chip design and experiments.'),t('编写和运行部分数据处理程序，使用 Cutadapt、STAR、featureCounts 完成测序预处理、比对、表达定量及下游分析。','Wrote Python scripts on Linux to process sequencing data. Used Cutadapt, STAR and featureCounts to clean reads, match sequences and measure gene activity.'),t('国家发明专利申请号：2025115308827。','Chinese invention patent application no. 2025115308827.')]),

        (
            '03', 'PLC / AUTOMATION',
            t('基于 PLC 的<br>自适应交通信号灯控制系统', 'Adaptive traffic lights<br>with PLC control'),
            t('2023.09 — 2023.10 · 项目负责人', 'Sep 2023 — Oct 2023 · Project Lead'),
            t('结合车辆传感器与行人按钮，实现双向道路信号时序控制、行人安全通行和基于实时交通状态的自适应控制。',
              'Built a traffic-light controller that responds to vehicles and pedestrian requests, with both timed and sensor-based modes.'),
            t('定时 / 传感器双模式', 'Timed + sensor-based control'),
            t('车辆检测 · 行人单周期响应 · 安全互锁', 'Vehicle detection · Pedestrian requests · Safety checks'),
            ['PLC', t('数字量 I/O', 'Digital I/O'), t('定时器 / 计数器', 'Timers / Counters'), t('逻辑互锁', 'Interlocks')],
            [
                t('开发 PLC 交通信号控制程序，配置车辆传感器、行人按钮及交通信号灯的数字量 I/O，实现双向道路红、黄、绿灯的周期时序控制。',
                  'Programmed the PLC and configured digital inputs and outputs for vehicle sensors, pedestrian buttons and signal lights. Set up the red, amber and green light sequence for both road directions.'),
                t('使用定时器、计数器及逻辑互锁设计行人通行功能，实现按钮触发、单周期响应和行人信号灯安全切换，并统计行人触发次数。',
                  'Used timers, counters and interlocks to handle each pedestrian button request in a single crossing cycle. Added safe signal switching and a counter for pedestrian requests.'),
                t('接入车辆检测传感器，根据车辆存在状态动态控制道路绿灯；设计定时模式与传感器模式切换逻辑，实现基于实时交通状态的自适应信号控制。',
                  'Used vehicle sensors to adjust green lights based on traffic presence. Added switching between fixed timing and sensor-based control so the lights could respond to current traffic conditions.')
            ]
        ),
        ('04','COMPUTER VISION / AUTOMATION',t('基于人机协同的<br>智能篮球直播系统','Smart camera tracking<br>for basketball broadcasts'),t('2022.11 — 2023.12 · 项目负责人','Nov 2022 — Dec 2023 · Project Lead'),t('从球员与篮球检测，到焦点计算与云台跟踪，让智能摄像装置更好地服务体育赛事直播。','Built a system that detects players and the ball, chooses where the camera should look and controls a motorized camera mount.'),'96%+',t('识别准确率 · 平均检测延迟 < 50 ms','Detection accuracy · Average detection latency < 50 ms'),['Python','YOLOv7',t('目标检测','Object detection'),t('云台控制','Gimbal control')],[t('自建篮球赛事标注数据集，使用 YOLOv7 训练球员和篮球目标检测模型，并在移动端部署。','Built a labeled basketball dataset, trained a YOLOv7 player-and-ball detection model and deployed it on a mobile device.'),t('提出基于最小外接圆拟合的焦点计算方法，通过重心与置信度生成焦点；将坐标无线传输至微控制器，驱动云台自动追踪。','Designed a method to choose a camera target from the positions and detection confidence of players and the ball. Sent the target wirelessly to a controller that moved the camera mount.'),t('获国家级大学生创新创业训练计划项目荣誉、中国国际大学生创新大赛北京赛区三等奖。','Recognized as a national-level undergraduate innovation project. Won third prize in the Beijing division of the China International College Students’ Innovation Competition.')])]
    project_html = ''
    for num,category,pname,date,desc,metric,caption,tags,detail in projects:
        project_html += f'<article class="card project"><div class="project-top"><span class="eyebrow">{category}</span><span class="project-number">{num}</span></div><h3>{pname}</h3><p class="date">{date}</p><p>{desc}</p><div class="project-result"><strong>{metric}</strong><span>{caption}</span></div>{pills(tags)}<details><summary>{t("项目详情","Project details")}<span aria-hidden="true">＋</span></summary><div class="detail-content">{bullets(detail)}</div></details></article>'
    skills = [
        (t('自动化与控制','Automation & control'),['PLC','PID','MATLAB'],t('自动控制原理、控制系统设计、倒立摆建模，以及 PID 参数整定与调试。','Control-system design, PLC programming, inverted-pendulum modeling and hands-on PID tuning.')),
        (t('芯片设计与制备','Chip design & fabrication'),['MEMS','L-Edit','AutoCAD','PDMS'],t('微芯片版图设计、软光刻、封装键合与芯片性能测试。','Chip layout design, soft lithography, packaging, bonding and performance testing.')),
        (t('编程与数据分析','Programming & data'),['Python','C','Linux','pi-ai','LLM','STAR','featureCounts'],t('数据处理程序编写、测序数据分析，以及基于大语言模型的研究分析流程开发。','Python data processing, sequencing analysis and AI-assisted research workflows.')),
        (t('沟通与协作','Communication & coordination'),['CET-4','CET-6','Office','WPS'],t('英语听说读写、项目排期与风险跟踪、跨团队沟通；持全国计算机二级证书。','English communication, project schedules, risk tracking and teamwork. Passed CET-4, CET-6 and the National Computer Rank Examination Level 2.'))]
    skill_html = ''.join(f'<article class="card skill"><span class="skill-index">0{i+1}</span><h3>{s[0]}</h3>{pills(s[1])}<p>{s[2]}</p></article>' for i,s in enumerate(skills))
    awards = [
        ('2024 — 2025',t('研究生特等、一等学业奖学金','Special-grade & First-grade Graduate Academic Scholarships'),t('北京化工大学','Beijing University of Chemical Technology')),
        ('2025',t('北京化工大学 — 万集科技奖学金','BUCT–Wanji Technology Scholarship'),t('北京化工大学','Beijing University of Chemical Technology')),
        ('2024',t('中国国际大学生创新大赛 · 北京赛区三等奖','China International College Students’ Innovation Competition · Beijing Third Prize'),t('智能篮球直播系统项目','Intelligent basketball broadcasting project'))]
    award_html = ''.join(f'<div class="award-row"><span class="award-star" aria-hidden="true">✳</span><div><h3>{a[1]}</h3><p>{a[2]}</p></div><span class="date">{a[0]}</span></div>' for a in awards)
    html = f'''<!doctype html>
<html lang="{locale}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{description}">
<meta name="theme-color" content="#f8f8f5"><meta name="color-scheme" content="light dark">
<link rel="canonical" href="https://marzovo.top/{t('','en/')}">
<link rel="alternate" hreflang="zh-CN" href="https://marzovo.top/"><link rel="alternate" hreflang="en" href="https://marzovo.top/en/"><link rel="alternate" hreflang="x-default" href="https://marzovo.top/">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="https://marzovo.top/{t('','en/')}"><meta property="og:locale" content="{t('zh_CN','en_US')}">
<link rel="icon" type="image/svg+xml" href="{base}assets/favicon.svg">
<script src="{base}assets/theme.js"></script><link rel="stylesheet" href="{base}assets/style.css">
<script src="{base}assets/site.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">{t('跳转到正文','Skip to content')}</a>
<header class="site-header wrap"><a href="index.html" class="brand" aria-label="{t('李悦萌，首页','Yuemeng Li, home')}"><span class="brand-mark" aria-hidden="true">m.</span><span>MarzOvO<span class="brand-dot" aria-hidden="true">✦</span></span></a><nav aria-label="{t('主导航','Main navigation')}">{''.join(f'<a href="#{id}">{label}</a>' for id,label in nav)}</nav><div class="header-controls"><button type="button" class="theme-toggle" aria-label="{t('切换深浅色主题','Toggle color theme')}" aria-pressed="false" hidden><span class="sun" aria-hidden="true">☼</span><span class="moon" aria-hidden="true">☾</span></button><div class="language-switch" role="group" aria-label="{t('语言切换','Language selection')}"><a class="language-option" href="{base}index.html" lang="zh-CN" hreflang="zh-CN" {t('aria-current="page"','')} aria-label="{t('中文，当前语言','Switch to Chinese')}">中文</a><a class="language-option" href="{base}en/index.html" lang="en" hreflang="en" {t('','aria-current="page"')} aria-label="{t('Switch to English','English, current language')}">English</a></div></div></header>
<main id="main" class="wrap">
<section class="hero card" aria-labelledby="intro-title"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span>{t('工程 · 研究 · 项目实践','ENGINEERING · RESEARCH · PROJECTS')}</p><h1 id="intro-title">{t('你好，我是','Hi, I’m')}<br><span class="name-label">{name}</span><span class="hello-star" aria-hidden="true">✳</span></h1><p class="hero-title">{t('把工程思考，<br>变成实际成果。','Turning ideas<br>into working solutions.')}</p><p class="hero-description">{t('北京化工大学控制科学与工程硕士生。<br>在 MEMS、自动化与数据分析的交叉点，<br class="desktop-break">从理解问题出发，用实践推动项目。','I study Control Science and Engineering at Beijing University of Chemical Technology. I build and test systems that bring together hardware, data and AI.')}</p>{pills([t('北京 · 中国','Beijing · China'),t('2027 届硕士','Master’s · Class of 2027')])}<div class="actions"><a class="button primary" href="#projects">{t('看看我的项目','Explore projects')} <span aria-hidden="true">↗</span></a><a class="button" href="{base}assets/{t('resume-zh.pdf','resume-en.pdf')}" download="Li-Yuemeng-CV-{t('ZH','EN')}.pdf">{t('下载中文简历','Download English CV')} <span aria-hidden="true">↓</span></a></div></div>
<aside class="profile-card" aria-label="{t('个人名片','Profile card')}"><div class="id-header"><span>PERSONAL PROFILE</span><span class="id-chip">BUCT</span></div><div class="id-body"><div class="portrait-frame"><img src="{base}assets/portrait.jpg" alt="{t('李悦萌的照片','Portrait of Yuemeng Li')}" width="179" height="251"><div class="photo-caption">Y. M. LI <span>✦</span></div></div><dl><div><dt>NAME</dt><dd>{name}</dd></div><div><dt>{t('专业 / MAJOR','MAJOR')}</dt><dd>{t('控制科学与工程','Control Science<br>& Engineering')}</dd></div><div><dt>{t('当前 / CURRENT','CURRENT')}</dt><dd>{t('硕士研究生','Master’s student')}</dd></div></dl></div><div class="id-footer"><div><span class="tiny-label">CURIOUS MIND, HANDS-ON SPIRIT</span><span class="id-domain">marzovo.top</span></div><span class="seal" aria-hidden="true">M</span></div><div class="id-stripes" aria-hidden="true"></div></aside></section>
<section id="about">{heading('01','关于我','About me','A LITTLE CONTEXT')}<div class="about-grid"><article class="card about-copy"><h3>{t('在技术与实践之间，<br>把每一步做扎实。','An engineering background.<br>A hands-on approach.')}</h3><p>{t('我目前在北京化工大学攻读控制科学与工程硕士，本科毕业于同校自动化专业。我的研究聚焦于基于 MEMS 芯片的单细胞全 RNA 组学，工作覆盖芯片设计与制备、实验验证和数据处理。','I’m a master’s student at Beijing University of Chemical Technology, where I also earned my bachelor’s degree in Automation. My research uses MEMS microchips to study RNA in single cells. I design and make chips, run experiments and work with the data.')}</p><p>{t('在瑞声科技、富士康与远森光电的实习中，我接触了新品导入、产线自动化与竞品分析，也逐步积累了项目协作、风险跟踪和问题闭环的实践经验。','My internships at AAC Technologies, Foxconn and Yuansen Optoelectronics covered new product development, factory automation and market research. Outside the lab, I also build an AI tool for personal investment research.')}</p></article><aside class="card snapshot"><h3>{t('我的经历，一眼看见','At a glance')}</h3><div class="snapshot-row"><strong>03</strong><div><b>{t('段实习经历','Industry internships')}</b><span>{t('产品 · 自动化 · 项目管理','Product · Automation · Project management')}</span></div></div><div class="snapshot-row"><strong>{len(projects):02d}</strong><div><b>{t('个主导项目','Projects built and led')}</b><span>{t('MEMS · 智能视觉 · PLC · AI Agent','Microchips · Computer vision · PLC · AI')}</span></div></div><div class="snapshot-row"><strong>01</strong><div><b>{t('项发明专利申请','Invention patent application')}</b><span>{t('围绕 MEMS 芯片研究','From MEMS chip research')}</span></div></div></aside></div></section>
<section id="experience">{heading('02','学习与工作经历','Experience','LEARN. BUILD. ITERATE.')}<h3 class="subheading">{t('教育背景','Education')}<span>01—02</span></h3><div class="entries">{''.join(educations)}</div><h3 class="subheading">{t('实习经历','Internships')}<span>01—03</span></h3><div class="entries">{''.join(internships)}</div></section>
<section id="projects">{heading('03','精选项目','Selected projects','IDEAS INTO PRACTICE')}<div class="project-grid">{project_html}</div></section>
<section id="skills">{heading('04','技能与工具','Skills & tools','MY TOOLKIT')}<div class="skills-grid">{skill_html}</div></section>
<section id="honors">{heading('05','荣誉与校园实践','Honors & campus life','BEYOND THE LAB')}<div class="card awards">{award_html}</div><article class="card campus"><div class="entry-heading"><div><span class="eyebrow">{t('校园实践','CAMPUS LEADERSHIP')}</span><h3>{t('研究生会学术科技部负责人','Academic and Technology Department Lead')}</h3></div><span class="date">{t("2025.09 — 2026.08","Sep 2025 — Aug 2026")}</span></div><p>{t('负责部门管理、活动策划与资源协调，组织多场校级、院级学术交流与科技创新活动，在实践中积累大型活动组织、多方协调及团队管理经验。','Led a department in the graduate student association. Planned academic and technology events, organized resources and worked with different teams to deliver university- and school-level activities.')}</p></article></section>
<section id="contact" class="card contact"><div><p class="eyebrow">LET’S CONNECT</p><h2>{t('期待与你交流。','Let’s start a conversation.')}</h2><p>{t('关于研究、工程实践，或下一次合作。','About research, engineering, or our next opportunity to collaborate.')}</p><div class="actions"><a class="button primary" href="mailto:13683217958@163.com">{t('给我发邮件','Say hello')} <span aria-hidden="true">↗</span></a><button type="button" class="button copy-email" hidden>{t('复制邮箱','Copy email')}</button></div><p id="copy-status" class="copy-status" role="status" aria-live="polite"></p></div><div class="contact-info"><div><span class="tiny-label">EMAIL</span><a href="mailto:13683217958@163.com">13683217958@163.com <span aria-hidden="true">↗</span></a></div><div><span class="tiny-label">GITHUB</span><a href="https://github.com/MarzOvO" target="_blank" rel="noopener noreferrer">@MarzOvO <span aria-hidden="true">↗</span></a></div><a class="text-link" href="{base}assets/{t('resume-zh.pdf','resume-en.pdf')}" download="Li-Yuemeng-CV-{t('ZH','EN')}.pdf">{t('下载原始中文简历','Download English CV')} ↓</a></div></section>
</main><footer class="wrap"><p>© 2026 {name} <span> / MarzOvO</span></p><a href="#main">{t('保持好奇，认真实践。','Stay curious. Make things happen.')} ↑</a></footer>
</body></html>'''
    destination = ROOT / ('index.html' if LANG == 0 else 'en/index.html')
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(html, encoding='utf-8')
    print(f'Built {destination.relative_to(ROOT)}')

if __name__ == '__main__':
    for LANG in (0,1):
        build()
