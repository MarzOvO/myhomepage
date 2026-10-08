"""Build the English PDF resume: python scripts/build_resume.py (requires reportlab)."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, PageBreak, HRFlowable,
)

ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor('#202b24')
GREEN = colors.HexColor('#375643')
MUTED = colors.HexColor('#535b55')
WIDTH = A4[0] - 88
STYLES = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10, leading=14, textColor=INK, spaceAfter=5),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.7, leading=13.2, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=3.5),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=GREEN, spaceBefore=10, spaceAfter=6, keepWithNext=True),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=10.6, leading=14.5, textColor=INK, keepWithNext=True),
    'date': ParagraphStyle('date', fontName='Helvetica', fontSize=9, leading=14.5, textColor=MUTED, alignment=TA_RIGHT),
    'role': ParagraphStyle('role', fontName='Helvetica', fontSize=9.3, leading=13, textColor=MUTED, spaceAfter=5, keepWithNext=True),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9.2, leading=14, textColor=MUTED),
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=27, leading=33, textColor=INK, spaceAfter=5),
}

def para(text, style='body'):
    return Paragraph(text, STYLES[style])

def section(title):
    return para(title.upper(), 'section')

def item(title, role, date, bullets):
    table = Table([[para(title, 'title'), para(date, 'date')]], colWidths=[WIDTH - 134, 134])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return KeepTogether([table, para(role, 'role')] + [para('- ' + b, 'bullet') for b in bullets] + [Spacer(1, 4)])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#cbd3cc'))
    canvas.setLineWidth(.5)
    canvas.line(44, 34, A4[0] - 44, 34)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(44, 22, 'Yuemeng Li  |  marzovo.top')
    canvas.drawRightString(A4[0] - 44, 22, str(doc.page))
    canvas.restoreState()

def build():
    output = ROOT / 'assets/resume-en.pdf'
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=44, leftMargin=44,
                            topMargin=37, bottomMargin=47, title='Yuemeng Li - English Resume',
                            author='Yuemeng Li', subject='Education, internships and engineering projects')
    story = [
        para('YUEMENG LI', 'name'),
        para('CONTROL ENGINEERING  /  AUTOMATION  /  AI TOOLS', 'role'),
        para('Beijing, China  |  +86 136 8321 7958  |  <link href="mailto:13683217958@163.com">13683217958@163.com</link>', 'contact'),
        para('<link href="https://marzovo.top/en/">marzovo.top/en</link>  |  <link href="https://github.com/MarzOvO">github.com/MarzOvO</link>', 'contact'),
        Spacer(1, 10), HRFlowable(width='100%', thickness=1.3, color=GREEN), Spacer(1, 11),
        para('Master’s student at Beijing University of Chemical Technology with a background in automation. Hands-on experience in microchip research, production-line controls and project support. Built projects in computer vision, traffic-light control and AI-assisted investment research.'),
        section('Education'),
        item('Beijing University of Chemical Technology', 'Master’s in Control Science and Engineering | Admitted by recommendation', 'Sep 2024 - Jul 2027<br/>(expected)', [
            'GPA: 3.53/4.00; top 5%. Courses include sensing technology, microelectromechanical systems (MEMS), and system modeling.'
        ]),
        item('Beijing University of Chemical Technology', 'Bachelor’s in Automation', 'Sep 2020 - Jun 2024', [
            'GPA: 3.52/4.33; top 5%. Courses include automatic control, modern control theory, process control, and analog and digital electronics.'
        ]),
        section('Internships'),
        item('AAC Technologies', 'Project Management Intern', 'Jun 2026 - Jul 2026', [
            'Supported a new microphone module project. Updated schedules and tracked design, materials, manufacturing, equipment and production-line readiness.',
            'Organized trial-production and quality-test data, and followed up on risks and open issues. Supported the project as the sample scale grew from about 11,800 to 20,000.'
        ]),
        item('Foxconn Technology Group', 'Anodizing Line Control Intern', 'Jul 2022 - Aug 2023', [
            'Used chemical concentration data to develop automatic dosing logic, reducing concentration fluctuations by about 16% and lowering the need for manual dosing.',
            'Helped test the automated crane that moves products between chemical baths, checking its routes and stop times.'
        ]),
        item('Shenzhen Yuansen Optoelectronics Technology Co., Ltd.', 'Product Intern', 'Jul 2021 - Aug 2021', [
            'Compared features, performance and prices for over 30 LED and optical products in Europe. Studied how price changes could affect demand.',
            'Suggested product improvements and helped develop pricing and promotion plans for the European market.'
        ]),
        section('Skills'),
        para('<b>Programming and AI:</b> Python, MATLAB, C, Linux, pi-ai, AI agent workflows.<br/><b>Engineering:</b> PLC programming, PID tuning, MEMS fabrication, L-Edit, AutoCAD.<br/><b>Data and tools:</b> Cutadapt, STAR, featureCounts, MA/MACD/RSI, Office, WPS.<br/><b>Languages and certificates:</b> English (CET-4 and CET-6); National Computer Rank Examination, Level 2.'),
        PageBreak(),
        para('PROJECTS &amp; ACHIEVEMENTS', 'title'),
        section('Selected projects'),
        item('AI Investment Research and Decision-Support Assistant', 'Independent Developer | Python, pi-ai, language models', '2025 - Present', [
            'Designed a personal research system with Research, Decision and Report agents to automate market research, decision support and report writing.',
            'Combined stock and ETF prices, financial news and policy updates. Used MA, MACD and RSI with a language model to assess market trends over different time frames and suggest portfolio changes.',
            'Built tools that account for current holdings, available funds and risk limits. Added position-size suggestions, tests on historical data, decision records and an interactive web interface.'
        ]),
        item('Microchips for Single-Cell RNA Research', 'Project Lead | MEMS, PDMS, Python, Linux', 'Sep 2024 - Present', [
            'Designed chip layouts, made molds, cast PDMS chips and tested their performance to collect RNA from individual cells. Improved the design and experiments based on results.',
            'Wrote Python scripts and used Cutadapt, STAR and featureCounts to clean sequencing reads, match sequences and measure gene activity.',
            'Filed a Chinese invention patent application, no. 2025115308827.'
        ]),
        item('Adaptive Traffic Lights with PLC Control', 'Project Lead | PLC, digital I/O, timers and counters', 'Sep 2023 - Oct 2023', [
            'Programmed traffic-light sequences for both road directions. Configured digital inputs and outputs for vehicle sensors, pedestrian buttons and signal lights.',
            'Used timers, counters and interlocks to handle each pedestrian request in a single crossing cycle, switch signals safely and count pedestrian requests.',
            'Adjusted green lights based on vehicle detection. Added fixed-timing and sensor-based modes to respond to current traffic conditions.'
        ]),
        item('Smart Camera Tracking for Basketball Broadcasts', 'Project Lead | Python, YOLOv7, camera-mount control', 'Nov 2022 - Dec 2023', [
            'Built a labeled basketball dataset, trained a model to detect players and the ball, and deployed it on a mobile device.',
            'Designed a camera-target selection method and sent target coordinates wirelessly to a camera-mount controller. Achieved over 96% detection accuracy with average detection latency below 50 ms.',
            'Recognized as a national-level undergraduate innovation project; won third prize in the Beijing division of the China International College Students’ Innovation Competition.'
        ]),
        section('Awards & campus leadership'),
        para('<b>2024-2025:</b> Special-grade and First-grade Graduate Academic Scholarships, BUCT.<br/><b>2025:</b> BUCT-Wanji Technology Scholarship.<br/><b>2024:</b> China International College Students’ Innovation Competition, Beijing Third Prize.', 'bullet'),
        para('<b>Sep 2025 - Aug 2026:</b> Led the Academic and Technology Department of the graduate student association. Planned academic and technology events, coordinated resources and worked with different teams.', 'bullet'),
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Built {output}')

if __name__ == '__main__':
    build()
