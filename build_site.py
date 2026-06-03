#!/usr/bin/env python3
"""
Generate a fully static HTML site from all ERP evaluation markdown files.
Every page is a standalone .html file with the same sidebar, CSS, and responsive layout.
Zero JavaScript rendering — all content is pre-built.
"""
import os, re, json, html as html_mod

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'docs')

# ── MARKDOWN → HTML CONVERTER ──

def md(text):
    if not text: return ''
    lines = text.split('\n')
    out = []; in_table=False; in_ul=False; in_ol=False; in_code=False; code_buf=[]
    def inline(s):
        # Replace code spans with placeholders to protect from bold/italic
        codes = []
        def save_code(m):
            codes.append(f'<code>{m.group(1)}</code>')
            return f'__CODE{len(codes)-1}__'
        s = re.sub(r'`([^`]+)`', save_code, s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        # Restore code spans
        for i, c in enumerate(codes):
            s = s.replace(f'__CODE{i}__', c)
        return s
    def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    i=0
    while i < len(lines):
        line=lines[i]; raw=line.strip()
        if raw.startswith('```'):
            if in_code:
                c='\n'.join(code_buf)
                out.append(f'<pre><code>{esc(c)}</code></pre>'); code_buf=[]; in_code=False
            else: in_code=True; code_buf=[]
            i+=1; continue
        if in_code: code_buf.append(line); i+=1; continue
        if in_ul and not raw.startswith(('- ','* ','  ')): out.append('</ul>'); in_ul=False
        if in_ol and not (raw.startswith(tuple(f'{n} ' for n in range(1,20))) or raw.startswith('  ')): out.append('</ol>'); in_ol=False
        if '|' in raw and raw.startswith('|'):
            cells=[c.strip() for c in raw.strip('|').split('|')]
            if all(re.match(r'^[-:]+$',c) for c in cells): i+=1; continue
            if not in_table: out.append('<div class="table-wrap"><table><thead><tr>')
            else: out.append('<tr>')
            for c in cells: out.append(f'<{"th" if not in_table else "td"}>{inline(c)}</{"th" if not in_table else "td"}>')
            if not in_table: out.append('</tr></thead><tbody>'); in_table=True
            else: out.append('</tr>')
            i+=1; continue
        elif in_table: out.append('</tbody></table></div>'); in_table=False
        hm=re.match(r'^(#{1,6})\s+(.+)',raw)
        if hm: lvl=len(hm.group(1)); out.append(f'<h{lvl}>{inline(hm.group(2))}</h{lvl}>'); i+=1; continue
        if raw.startswith('>'): out.append(f'<blockquote>{inline(raw[1:].strip())}</blockquote>'); i+=1; continue
        if raw.startswith(('- ','* ')):
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append(f'<li>{inline(raw[2:])}</li>'); i+=1; continue
        olm=re.match(r'^(\d+)\.\s+(.+)',raw)
        if olm:
            if not in_ol: out.append('<ol>'); in_ol=True
            out.append(f'<li>{inline(olm.group(2))}</li>'); i+=1; continue
        if raw in ('---','***','___'): out.append('<hr>'); i+=1; continue
        if not raw: out.append(''); i+=1; continue
        out.append(f'<p>{inline(raw)}</p>'); i+=1
    if in_table: out.append('</tbody></table></div>')
    if in_ul: out.append('</ul>')
    if in_ol: out.append('</ol>')
    return '\n'.join(out)

def read_md(rel):
    p=os.path.join(BASE,rel)
    return open(p,'r',encoding='utf-8').read() if os.path.exists(p) else None

# ── SITE STRUCTURE ──
# Each item: (filename, title, icon, section, children_or_content)
# sections with children define nav groups

SECTIONS = [
    ('Comparison', [
        ('index.html', 'Executive Dashboard', '📊'),
        ('vendors.html', 'Vendor Profiles', '🏢'),
        ('products.html', 'Products in Scope', '📦'),
        ('pricing.html', 'License Pricing', '💲'),
        ('annual.html', 'Annual Cost Model', '📅'),
        ('implementation.html', 'Implementation Costs', '⚙️'),
        ('training.html', 'Training Costs', '🎓'),
        ('tco.html', '5-Year TCO', '📈'),
        ('capabilities.html', 'Capability Comparison', '⭐'),
        ('reqfit.html', 'Requirements Fit', '✅'),
        ('risks.html', 'Risk Assessment', '⚠️'),
        ('recommendation.html', 'Final Recommendation', '🏆'),
    ]),
    ('Detailed Evaluation', [
        ('eval-matrix.html', 'ERP Evaluation Matrix', '📋'),
        ('vendor-stack.html', 'Vendor Stack (Full)', '🔧'),
        ('cost-capability.html', 'Cost & Capability Detail', '💰'),
        ('full-comparison.html', 'Complete Comparison Table', '📄'),
        ('vendor-sap.html', 'SAP S/4HANA Evaluation', '🏢'),
        ('vendor-oracle.html', 'Oracle Fusion Evaluation', '🏢'),
        ('vendor-msft.html', 'Microsoft D365 Evaluation', '🏢'),
        ('vendor-odoo.html', 'Odoo Evaluation', '🏢'),
    ]),
    ('Model Company', [
        ('company.html', 'Company Profile', '🏗️'),
        ('executive.html', 'Executive Summary', '📋'),
        ('requirements.html', 'ERP Requirements (178 Must)', '✅'),
        ('data-volumes.html', 'Data Volumes & Integrations', '📊'),
        ('internal-controls.html', 'Internal Controls Matrix', '🔒'),
        ('req-workflow-matrix.html', 'Req ↔ Workflow Matrix', '🔗'),
        ('assumptions.html', 'Assumptions & Decisions', '📝'),
        ('mobile-strategy.html', 'Mobile App Strategy', '📱'),
        ('data-migration.html', 'Data Migration Mapping', '🗂️'),
        ('wilcon.html', 'Wilcon Depot Benchmark', '🏪'),
    ]),
    ('Workflows (276)', [
        ('workflows.html', 'Workflow Index', '🔄'),
        ('WF-finance.html', 'Finance', '💰'),
        ('WF-store-operations.html', 'Store Operations', '🏪'),
        ('WF-procurement.html', 'Procurement', '🛒'),
        ('WF-merchandising.html', 'Merchandising', '🏷️'),
        ('WF-inventory.html', 'Inventory', '📦'),
        ('WF-warehouse.html', 'Warehouse', '🏭'),
        ('WF-ecommerce.html', 'Ecommerce', '🌐'),
        ('WF-hr.html', 'HR & Payroll', '👥'),
        ('WF-customer.html', 'Customer', '🤝'),
        ('WF-compliance.html', 'Compliance', '📜'),
        ('WF-supply-chain.html', 'Supply Chain', '🚛'),
        ('WF-marketing.html', 'Marketing', '📣'),
        ('WF-it-operations.html', 'IT Operations', '💻'),
        ('WF-services.html', 'Services', '🔧'),
        ('WF-governance.html', 'Governance', '🏛️'),
        ('WF-project-sales.html', 'Project Sales', '📐'),
        ('WF-audit.html', 'Audit', '🔍'),
        ('WF-health-safety.html', 'Health & Safety', '⛑️'),
        ('WF-property.html', 'Property', '🏠'),
        ('WF-engineering-construction.html', 'Eng. & Construction', '🏗️'),
        ('WF-logistics-fleet.html', 'Logistics & Fleet', '🚚'),
        ('WF-treasury.html', 'Treasury', '🏦'),
        ('WF-innovation.html', 'Innovation', '💡'),
        ('WF-esg.html', 'ESG', '🌱'),
        ('WF-hazmat.html', 'Hazmat', '☣️'),
        ('WF-master-data.html', 'Master Data', '📋'),
        ('WF-wholesale.html', 'Wholesale', '📦'),
        ('WF-non-store-maintenance.html', 'Non-Store Maint.', '🧹'),
        ('WF-document-management.html', 'Document Mgmt', '📄'),
        ('touchpoint-map.html', 'System Touchpoint Map', '🗺️'),
    ]),
    ('Methodology', [
        ('methodology.html', 'Scoring Methodology', '📐'),
        ('roadmap.html', 'Implementation Roadmap', '🗺️'),
        ('tech-guidelines.html', 'Technical Guidelines', '💡'),
    ]),
]

# Build flat lookup: filename -> (title, icon)
PAGE_META = {}
for sec, pages in SECTIONS:
    for fname, title, icon in pages:
        PAGE_META[fname] = (title, icon, sec)

# ── CSS (shared across all pages) ──
CSS = """\
:root{--oracle:#c74634;--oracle-l:#fdeae8;--msft:#0078d4;--msft-l:#e6f4ff;--sap:#0faaff;--sap-l:#e6f5ff;\
--bg:#f5f6f8;--card:#fff;--text:#1a1a2e;--text2:#666;--border:#e2e5ea;--accent:#4f46e5;--accent-l:#eef2ff;\
--green:#16a34a;--amber:#d97706;--red:#dc2626;--r:10px;--nav-w:260px}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;background:var(--bg);\
color:var(--text);line-height:1.65;overflow-x:hidden}
/* SIDEBAR */
.sb{position:fixed;top:0;left:0;width:var(--nav-w);height:100vh;background:#1a1a2e;color:#c5c8d8;\
overflow-y:auto;overflow-x:hidden;z-index:1000;transition:transform .3s}
.sb .logo{padding:16px 14px 6px;display:block;text-decoration:none;color:#fff}
.sb .logo b{font-size:16px;display:block}
.sb .logo small{font-size:10px;color:#8b8fa3;display:block;margin-top:2px}
.ns{padding:10px 14px 3px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;\
color:#6b7094;border-top:1px solid #2a2a42;margin-top:2px}
.ns:first-child{border-top:none;margin-top:6px}
.sb nav a{display:flex;align-items:center;gap:7px;padding:6px 14px;color:#a0a4b8;text-decoration:none;\
font-size:12.5px;font-weight:500;border-left:3px solid transparent;transition:.15s;white-space:nowrap;\
overflow:hidden;text-overflow:ellipsis}
.sb nav a:hover,.sb nav a.act{background:rgba(255,255,255,.06);color:#fff;border-left-color:var(--accent)}
.sb nav a .ic{width:16px;text-align:center;flex-shrink:0;font-size:13px}
.sb nav a.sub{font-size:11.5px;padding-left:28px}
/* HAMBURGER */
.ham{display:none;position:fixed;top:10px;left:10px;z-index:1100;width:40px;height:40px;border-radius:var(--r);\
border:none;background:#1a1a2e;color:#fff;font-size:20px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.15)}
.ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:999}
.ov.show{display:block}
/* MAIN */
.mn{margin-left:var(--nav-w);padding:24px;min-height:100vh}
/* CARDS */
.cd{background:var(--card);border-radius:var(--r);box-shadow:0 1px 3px rgba(0,0,0,.08);\
padding:22px;margin-bottom:18px;border:1px solid var(--border)}
.cd h2{font-size:18px;margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--border)}
/* KPI */
.kr{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:18px}
.kp{background:var(--card);border-radius:var(--r);padding:14px;box-shadow:0 1px 3px rgba(0,0,0,.08);\
border:1px solid var(--border);text-align:center}
.kp .lb{font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.4px;color:var(--text2);margin-bottom:3px}
.kp .vl{font-size:22px;font-weight:800}
.kp .sb2{font-size:10px;color:var(--text2);margin-top:2px}
/* TABLES */
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:0 -4px;padding:0 4px}
table{width:100%;border-collapse:collapse;font-size:12px;background:var(--card);border-radius:var(--r);\
overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08)}
th{background:#1a1a2e;color:#fff;font-weight:600;text-align:left;padding:9px 11px;font-size:10.5px;\
text-transform:uppercase;letter-spacing:.3px;position:sticky;top:0;z-index:1}
td{padding:7px 11px;border-bottom:1px solid var(--border);vertical-align:top;font-size:12.5px}
tr:hover td{background:#f7f8fc}
th.o,td.o{border-left:3px solid var(--oracle)}
th.m,td.m{border-left:3px solid var(--msft)}
th.s,td.s{border-left:3px solid var(--sap)}
tr.ct td{background:var(--accent-l);font-weight:700;font-size:11px;text-transform:uppercase;letter-spacing:.3px}
/* STARS & RISK */
.st{color:#f59e0b;letter-spacing:1px}
.rl{display:inline-block;background:#dcfce7;color:var(--green);padding:2px 8px;border-radius:6px;font-size:10px;font-weight:700}
.rm{display:inline-block;background:#fef3c7;color:var(--amber);padding:2px 8px;border-radius:6px;font-size:10px;font-weight:700}
.rh{display:inline-block;background:#fee2e2;color:var(--red);padding:2px 8px;border-radius:6px;font-size:10px;font-weight:700}
/* VENDOR CARDS */
.vc{border-radius:var(--r);padding:18px;box-shadow:0 1px 3px rgba(0,0,0,.08);border:2px solid transparent;margin-bottom:14px}
.vc.oracle{background:var(--oracle-l);border-color:var(--oracle)}
.vc.msft{background:var(--msft-l);border-color:var(--msft)}
.vc.sap{background:var(--sap-l);border-color:var(--sap)}
.vc h3{margin:0 0 4px;font-size:15px}
.vc .tg{display:inline-block;padding:2px 10px;border-radius:6px;font-size:10px;font-weight:700;color:#fff;margin-bottom:6px}
.vc.oracle .tg{background:var(--oracle)}.vc.msft .tg{background:var(--msft)}.vc.sap .tg{background:var(--sap)}
.vc ul{list-style:none;font-size:12.5px}.vc li{padding:2px 0}.vc li::before{content:'→ ';font-weight:700}
/* BAR */
.br{display:flex;align-items:center;margin-bottom:5px;gap:8px}
.bl{width:70px;font-size:10.5px;font-weight:600;text-align:right;flex-shrink:0}
.bt{flex:1;height:20px;background:#e5e7eb;border-radius:5px;overflow:hidden}
.bf{height:100%;border-radius:5px;display:flex;align-items:center;padding-left:8px;color:#fff;font-size:9.5px;font-weight:700}
.bf.o{background:var(--oracle)}.bf.m{background:var(--msft)}.bf.s{background:var(--sap)}
/* MD CONTENT */
.mc h1{font-size:22px;margin:18px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--border)}
.mc h2{font-size:18px;margin:16px 0 8px;padding-bottom:4px;border-bottom:1px solid var(--border)}
.mc h3{font-size:15px;margin:12px 0 6px;color:var(--text2)}
.mc h4{font-size:14px;margin:10px 0 4px;color:var(--text2)}
.mc p{margin:6px 0}
.mc ul,.mc ol{margin:6px 0 6px 18px}
.mc li{margin:2px 0}
.mc blockquote{border-left:4px solid var(--accent);background:var(--accent-l);padding:10px 14px;margin:10px 0;\
border-radius:0 var(--r) var(--r) 0;font-size:13px}
.mc pre{background:#1a1a2e;color:#e0e0e0;padding:14px;border-radius:var(--r);overflow-x:auto;margin:10px 0;font-size:12px}
.mc code{background:#f0f1f3;padding:1px 5px;border-radius:4px;font-size:11.5px}
.mc pre code{background:none;padding:0}
.mc hr{border:none;border-top:1px solid var(--border);margin:16px 0}
.mc table{margin:10px 0}
.mc strong{color:var(--text)}
/* SECTION TITLE */
.stl{display:flex;align-items:center;gap:10px;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid var(--border)}
.stl .ic{font-size:20px}.stl h2{font-size:18px;margin:0;border:none;padding:0}
/* GRID */
.gr{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-bottom:16px}
/* FOOTER */
.ft{text-align:center;padding:20px 14px;color:var(--text2);font-size:10px;margin-top:24px;border-top:1px solid var(--border)}
/* RESPONSIVE */
@media(max-width:900px){
  .sb{transform:translateX(-100%)}
  .sb.open{transform:translateX(0)}
  .ham{display:flex;align-items:center;justify-content:center}
  .mn{margin-left:0;padding:52px 10px 14px}
  .kr{grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px}
  .kp .vl{font-size:17px}table{font-size:10.5px}th,td{padding:5px 6px}
  .bl{width:55px;font-size:9.5px}.vc ul{font-size:11.5px}
}
@media(max-width:480px){.mn{padding:48px 6px 10px}.cd{padding:12px}.kr{grid-template-columns:1fr 1fr}}
@media print{.sb,.ham,.ov{display:none!important}.mn{margin:0;padding:8px}}
"""

# ── HTML TEMPLATE ──
def page_html(filename, title, icon, body_html):
    """Generate a full standalone HTML page."""
    # Build nav
    nav_parts = []
    for sec_name, pages in SECTIONS:
        nav_parts.append(f'<div class="ns">{sec_name}</div>')
        for fname, ptitle, picon in pages:
            active = ' act' if fname == filename else ''
            cls = ' sub' if sec_name not in ('Comparison',) else ''
            nav_parts.append(f'<a href="{fname}" class="{cls.strip()}{active}"><span class="ic">{picon}</span>{ptitle}</a>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — BuildRight Depot ERP Comparison</title>
<style>{CSS}</style>
</head>
<body>
<button class="ham" onclick="document.getElementById('sb').classList.toggle('open');document.getElementById('ov').classList.toggle('show')" aria-label="Menu">☰</button>
<div class="ov" id="ov" onclick="this.classList.remove('show');document.getElementById('sb').classList.remove('open')"></div>
<aside class="sb" id="sb">
<a href="index.html" class="logo"><b>🏗️ BuildRight Depot</b><small>ERP Vendor Comparison</small></a>
<nav>{''.join(nav_parts)}</nav>
</aside>
<div class="mn">
{body_html}
<div class="ft"><strong>BuildRight Depot Corp.</strong> — ERP Vendor Comparison · June 2026<br>
Oracle pricing from official Global Price List (April 2026) · Microsoft &amp; SAP from public sources<br>
<em>All costs are estimates. Actual pricing subject to vendor negotiation.</em></div>
</div>
</body></html>"""


# ── CONTENT GENERATORS ──
# Comparison table helper
def T(*cols):
    row = '<tr>'
    for i, c in enumerate(cols):
        if i == 0: row += f'<td><strong>{c}</strong></td>'
        elif i <= 3: row += f'<td class="{["o","m","s"][i-1]}">{c}</td>'
        else: row += f'<td style="color:var(--green);font-weight:700">{c}</td>'
    return row + '</tr>'

def gen_dashboard():
    return page_html('index.html', 'Executive Dashboard', '📊', f"""
<div style="text-align:center;padding:16px 0 12px">
  <h1 style="font-size:24px;font-weight:800">🏗️ BuildRight Depot Corp.</h1>
  <p style="color:var(--text2);max-width:560px;margin:6px auto;font-size:13px">ERP vendor comparison — 200 stores, 6,510 employees, Philippines.<br>Comparing <strong>Oracle Fusion Cloud</strong>, <strong>Microsoft Dynamics 365</strong>, and <strong>SAP S/4HANA Cloud</strong>.</p>
</div>
<div class="kr">
  <div class="kp"><div class="lb">Microsoft 5-Year TCO</div><div class="vl" style="color:var(--msft)">$32.9–37.1M</div><div class="sb2">✓ Lowest</div></div>
  <div class="kp"><div class="lb">Oracle 5-Year TCO</div><div class="vl" style="color:var(--oracle)">$48.2–56.7M</div><div class="sb2">3rd — Highest Risk</div></div>
  <div class="kp"><div class="lb">SAP 5-Year TCO</div><div class="vl" style="color:var(--sap)">$55.6–63.2M</div><div class="sb2">2nd — Strongest ERP</div></div>
  <div class="kp"><div class="lb">Total Users</div><div class="vl">6,510</div><div class="sb2">200 stores + 4 DCs</div></div>
  <div class="kp"><div class="lb">Must Have Reqs</div><div class="vl">~178</div><div class="sb2">14 categories</div></div>
</div>
<div class="cd"><h2>5-Year TCO Comparison</h2>
  <div class="br"><div class="bl">Microsoft</div><div class="bt"><div class="bf m" style="width:56%">$32.9–37.1M</div></div></div>
  <div class="br"><div class="bl">Oracle</div><div class="bt"><div class="bf o" style="width:84%">$48.2–56.7M</div></div></div>
  <div class="br"><div class="bl">SAP</div><div class="bt"><div class="bf s" style="width:100%">$55.6–63.2M</div></div></div>
</div>
<div class="gr">
  <div class="vc oracle"><h3>Oracle Fusion Cloud</h3><span class="tg">CONDITIONAL</span><ul>
    <li><b>TCO:</b> $48.2–56.7M</li><li><b>Score:</b> 3.73/5</li><li><b>Reqs:</b> ~141/178</li>
    <li><b>POS:</b> ❌ No native POS</li><li><b>Risk:</b> 10+ integration flows</li></ul></div>
  <div class="vc msft"><h3>Microsoft Dynamics 365</h3><span class="tg">✅ RECOMMENDED</span><ul>
    <li><b>TCO:</b> $32.9–37.1M ✓ Best</li><li><b>Score:</b> 4.62/5 ✓ Best</li><li><b>Reqs:</b> ~148/178</li>
    <li><b>POS:</b> ✅ Native retail POS</li><li><b>Risk:</b> ISV payroll dependency</li></ul></div>
  <div class="vc sap"><h3>SAP S/4HANA Cloud</h3><span class="tg">CONDITIONAL</span><ul>
    <li><b>TCO:</b> $55.6–63.2M</li><li><b>Score:</b> 4.25/5</li><li><b>Reqs:</b> ~149/178 ✓ Most</li>
    <li><b>POS:</b> ⚠️ CCO immature</li><li><b>Risk:</b> Highest cost + POS gap</li></ul></div>
</div>
<div class="cd"><h2>Capability Scorecard</h2><div class="tw"><table>
<thead><tr><th>Dimension</th><th>Wt</th><th class="o">Oracle</th><th class="m">Microsoft</th><th class="s">SAP</th><th>Winner</th></tr></thead>
<tbody>
{T('Financial Management','15%','★★★★★','★★★★★','★★★★★','SAP (slight)')}
{T('Inventory & Warehouse','10%','★★★★☆','★★★★☆','★★★★★','SAP')}
{T('POS & Retail','15%','★★☆☆☆','★★★★★','★★★☆☆','Microsoft')}
{T('Ecommerce','8%','★★★★☆','★★★★★','★★★★☆','Microsoft')}
{T('Supply Chain Planning','5%','★★★★☆','★★★★☆','★★★★★','SAP')}
{T('HR & Payroll','8%','★★★★★','★★★☆☆','★★★★★','Oracle / SAP')}
{T('CRM & Loyalty','5%','★★★★☆','★★★★★','★★★★☆','Microsoft')}
{T('Analytics & BI','5%','★★★★☆','★★★★★','★★★★★','Microsoft')}
{T('AI & Innovation','4%','★★★★☆','★★★★★','★★★★☆','Microsoft')}
{T('Low-Code / Extension','4%','★★★☆☆','★★★★★','★★★☆☆','Microsoft')}
{T('PH Localization','5%','★★☆☆☆','★★★☆☆','★★★★☆','SAP')}
{T('Impl. Risk','7%','★★☆☆☆','★★★★★','★★★☆☆','Microsoft')}
<tr style="font-weight:800;background:var(--accent-l)"><td><b>TOTAL</b></td><td>100%</td><td class="o">3.73</td><td class="m" style="color:var(--green)">4.62</td><td class="s">4.25</td><td style="color:var(--green);font-weight:700">Microsoft</td></tr>
</tbody></table></div></div>""")

def gen_vendors():
    rows=[['Headquarters','Austin, Texas, USA','Redmond, Washington, USA','Walldorf, Germany'],
          ['Cloud Platform','Oracle Cloud Infra (OCI)','Microsoft Azure','SAP BTP (AWS/Azure/GCP)'],
          ['Core ERP','Fusion Cloud ERP','D365 Finance + SCM','S/4HANA Cloud'],
          ['Licensing','Per-user/month (Named/Employee)','Per-user/month (tiered by app)','Per-user/month (Prof/Limited/Employee)'],
          ['Contract Term','3-year minimum','1–3 years (EA typically 3)','3–5 years (RISE with SAP)'],
          ['Release Cycle','Quarterly','Semi-annual waves','Quarterly'],
          ['Implementation','18–30 months','12–18 months','18–36 months'],
          ['Target Market','Large enterprises (1K+ emp)','Mid-to-large (200–50K+)','Large enterprises (1K+)'],
          ['Gartner MQ','Leader','Leader','Leader'],
          ['PH Presence','Limited — smaller ecosystem','Growing — MS PH + ISV','Established — Accenture/Deloitte/IBM']]
    body=f'<div class="stl"><span class="ic">🏢</span><h2>Vendor Profiles</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Dimension</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    for r in rows: body+=f'<tr><td><strong>{r[0]}</strong></td><td class="o">{r[1]}</td><td class="m">{r[2]}</td><td class="s">{r[3]}</td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('vendors.html','Vendor Profiles','🏢',body)

def gen_products():
    body=f'<div class="stl"><span class="ic">📦</span><h2>Products in Scope (Full Stack)</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Functional Area</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    prods=[('Core Business Operations',[
        ('Core Financials','Fusion Cloud ERP','D365 Finance','S/4HANA Cloud (FI, CO)'),
        ('Procurement','Fusion Procurement','D365 SCM — Procurement','S/4HANA MM + Ariba'),
        ('Inventory','Fusion SCM — Inventory','D365 SCM — Inventory','S/4HANA MM + EWM'),
        ('Warehouse','⚠️ WMS Cloud (separate)','✅ D365 SCM — WMS (native)','✅ SAP EWM (embedded)'),
        ('Supply Chain Planning','Fusion Supply + Demand','D365 Planning Optimization','SAP IBP'),
        ('Order Management','Fusion Order Mgmt','D365 SCM — Sales','S/4HANA SD + OMS'),
    ]),('Retail & Commerce',[('POS / Retail','⚠️ Oracle Retail Xstore (separate)','✅ D365 Commerce POS (native)','SAP Customer Checkout'),
        ('Ecommerce','Oracle Commerce Cloud','D365 Commerce — e-commerce','SAP Commerce Cloud'),
        ('Retail Merchandising','Oracle Retail (RMS, RPM)','D365 Commerce (native)','SAP Retail + CAR'),
    ]),('Human Capital Management',[('Core HR','Fusion HCM — Global HR','D365 Human Resources','SuccessFactors EC'),
        ('Payroll','Fusion HCM Payroll','⚠️ ISV Partner required','SuccessFactors Payroll'),
        ('Talent / Recruiting','Fusion Talent + Recruiting','D365 HR + LinkedIn','SuccessFactors Talent'),
        ('Time & Labor','Fusion Time & Labor','D365 HR + 3rd party','SuccessFactors Time'),
        ('Learning','Fusion Learning Cloud','LinkedIn Learning','SuccessFactors Learning'),
    ]),('Customer Experience',[('CRM / Sales','Fusion CX — Sales','D365 Sales','SAP Sales Cloud'),
        ('Customer Service','Fusion CX — Service','D365 Customer Service','SAP Service Cloud'),
        ('Loyalty','CrowdTwist','✅ D365 Commerce (native)','SAP Loyalty Management'),
        ('Marketing','Fusion CX — Marketing','CI – Journeys','SAP Emarsys'),
        ('CDP','CX Unity','Customer Insights','SAP Customer Data Platform'),
    ]),('Analytics & Platform',[('Analytics / BI','Oracle Analytics + OTBI','✅ Power BI','SAP Analytics Cloud'),
        ('Data Warehouse','Autonomous DW','Azure Synapse','SAP Datasphere'),
        ('Integration','Oracle Integration Cloud','Azure APIM + Logic Apps','SAP BTP Integration Suite'),
        ('Low-Code','Visual Builder (VBCS)','✅ Power Apps + Automate','SAP BTP (CF/ABAP)'),
        ('Document Mgmt','WebCenter','✅ SharePoint (native)','ArchiveLink + ILM'),
        ('Master Data Gov.','Product Hub + CDM','Dataverse (basic)','✅ SAP MDG (gold std)'),
    ]),('AI & Innovation',[('AI / ML','OCI AI + Custom AI Agents','✅ Azure AI + Copilot','SAP Business AI'),
        ('IoT','Oracle IoT Cloud','Azure IoT Hub','SAP IoT (BTP)'),
    ])]
    for cat,items in prods:
        body+=f'<tr class="ct"><td colspan="4">{cat}</td></tr>'
        for label,o,m,s in items:
            body+=f'<tr><td>{label}</td><td class="o">{o}</td><td class="m">{m}</td><td class="s">{s}</td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('products.html','Products in Scope','📦',body)

def gen_pricing():
    rows=[('Full ERP User (Finance+SCM+Proc)','$2,125/mo ($625+$625+$875)','$275/mo ($175+$100 att.)','$210/mo (Professional)'),
          ('Commerce / POS','~$200/mo (Xstore est.)','$175/mo (D365 Commerce)','$75/terminal/mo (CCO)'),
          ('Warehouse User','~$100/mo (WMS Cloud est.)','$175/mo (D365 SCM)','$300/mo (S/4HANA + EWM)'),
          ('HR Admin','$450/mo (HCM Pillar)','$120/mo (D365 HR)','$64/mo (SF EC+Pay+Talent+Time)'),
          ('Sales / CRM','$350/mo ($150+$200)','$190/mo ($95+$95)','$280/mo ($140+$140)'),
          ('Executive / Analytics','$680/mo ($180+$500 EPM)','$185/mo ($175+$10 PBI)','$246/mo ($210+$36 SAC)'),
          ('Employee Self-Service','$20/mo ($15+$5)','$8/mo (Team Member)','$47/mo ($35+$12)'),
          ('Light / Read-Only','$20/mo','$8/mo','$70–100/mo'),
          ('Integration Platform','$1,200/mo per 1M msgs','$150–2,800/mo (APIM)','$3,000–10,000/mo (BTP)'),
          ('AI Agents','$2.50–50/user/mo','$30/user/mo (Copilot)','Consumption-based'),
          ('Typical Discount','<strong>30–40%</strong> off list','<strong>15–25%</strong> off (EA)','<strong>20–30%</strong> off list')]
    body=f'<div class="stl"><span class="ic">💲</span><h2>Per-User Monthly License Pricing</h2></div>'
    body+='<div class="cd"><p style="margin-bottom:8px;font-size:12px;color:var(--text2)">Oracle from official Global Price List (April 2026). Microsoft &amp; SAP from public sources.</p><div class="tw"><table>'
    body+='<thead><tr><th>User Role</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    for label,o,m,s in rows: body+=T(label,o,m,s)
    body+='</tbody></table></div></div>'
    return page_html('pricing.html','License Pricing','💲',body)

def gen_annual():
    body=f'<div class="stl"><span class="ic">📅</span><h2>Annual License Cost Model (6,510 Users)</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>User Segment</th><th>Users</th><th class="o">Oracle (Net/yr)</th><th class="m">Microsoft (Net/yr)</th><th class="s">SAP (Net/yr)</th></tr></thead><tbody>'
    for label,n,o,m,s in [('Full ERP',250,'$1,218,750','$660,000','$472,500'),('Commerce / POS',600,'$936,000','$1,008,000','$405,000'),('Warehouse',150,'$117,000','$252,000','$405,000'),('HR / Payroll',30,'$105,300','$34,560','$17,280'),('Sales / CRM',50,'$136,500','$91,200','$126,000'),('Executive',20,'$106,080','$35,520','$44,280'),('Employee Self-Service',5500,'$858,000','$422,400','$2,326,500'),('Integration / Platform','—','$175,000','$144,000','$156,000'),('Add-on Products','—','$1,850,000','$738,000','$2,400,000')]:
        body+=f'<tr><td>{label}</td><td>{n}</td><td class="o">{o}</td><td class="m">{m}</td><td class="s">{s}</td></tr>'
    body+=f'<tr style="font-weight:700;background:#f0f4ff"><td><b>Subtotal Net License</b></td><td>6,510</td><td class="o"><b>$5,502,630</b></td><td class="m"><b>$3,385,680</b></td><td class="s"><b>$6,352,560</b></td></tr>'
    body+=T('Support &amp; Maintenance','—','$550,263 (10%)','$609,422 (18%)','$1,397,563 (22%)')
    body+=f'<tr style="font-weight:800;background:#e8edff"><td><b>Total Annual + Support</b></td><td>6,510</td><td class="o"><b>$6,052,893</b></td><td class="m" style="color:var(--green)"><b>$3,995,102</b></td><td class="s"><b>$7,750,123</b></td></tr>'
    body+='</tbody></table></div></div>'
    body+='<div class="kr"><div class="kp"><div class="lb">Oracle / User / Month</div><div class="vl" style="color:var(--oracle)">$77.48</div></div><div class="kp"><div class="lb">Microsoft / User / Month</div><div class="vl" style="color:var(--msft)">$51.14 ✓</div></div><div class="kp"><div class="lb">SAP / User / Month</div><div class="vl" style="color:var(--sap)">$99.21</div></div></div>'
    return page_html('annual.html','Annual Cost Model','📅',body)

def gen_implementation():
    body=f'<div class="stl"><span class="ic">⚙️</span><h2>Implementation Cost Breakdown</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Phase</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    impl=[('Planning & Design',[('Project Planning','$200K–350K','$150K–250K','$250K–400K'),('Architecture & Design','$300K–500K','$200K–350K','$400K–600K')]),
          ('System Configuration',[('Core Financials','$200K–300K','$150K–200K','$250K–350K'),('Supply Chain & Inventory','$150K–250K','$100K–200K','$200K–300K'),('Procurement','$100K–150K','$80K–120K','$100K–150K'),('Warehouse Mgmt','$150K–200K','$80K–120K','$150K–250K'),('POS / Retail','$200K–300K (Xstore)','$90K–160K (native)','$200K–450K (CCO)'),('HR / HCM / Payroll','$100K–150K','$60K–100K (ISV)','$80K–120K'),('Ecommerce','$100K–150K','$50K–80K','$100K–150K'),('Analytics / BI / EPM','$100K–150K','$50K–80K','$80K–120K')]),
          ('Data Migration',[('Master data (55K SKUs, 800 vendors, 600K customers)','$200K–350K','$120K–200K','$200K–350K'),('Transaction history','$150K–250K','$80K–150K','$150K–250K'),('Opening balances','$150K–200K','$100K–150K','$150K–200K')]),
          ('Integration Development',[('POS ↔ ERP','$300K–500K (OIC)','$50K–100K (native)','$200K–300K (CPI)'),('Ecommerce ↔ ERP','$200K–300K','$50K–100K (native)','$150K–250K'),('WMS ↔ ERP','$200K–300K (OIC)','— (native)','— (embedded)'),('PH-specific (BIR, eFPS, GCash)','$300K–500K','$200K–350K','$250K–400K'),('Other integrations','$400K–700K','$230K–360K','$360K–550K')]),
          ('Custom Development',[('PH regulatory extensions','$200K–350K (VBCS)','$150K–250K (Power Apps)','$200K–350K (BTP)'),('Catch-weight at POS','$150K–250K','$100K–150K','$150K–250K'),('Other custom','$330K–630K','$180K–370K','$330K–580K')]),
          ('Testing, Localization & Go-Live',[('Testing & QA','$500K–1,000K','$300K–500K','$500K–800K'),('PH Localization','$500K–1,000K','$300K–700K','$400K–800K'),('Go-Live & Hypercare','$500K–850K','$350K–600K','$500K–850K')])]
    for cat,items in impl:
        body+=f'<tr class="ct"><td colspan="4">{cat}</td></tr>'
        for label,o,m,s in items: body+=T(label,o,m,s)
    body+=f'<tr style="font-weight:800;background:#e8edff"><td><b>TOTAL IMPLEMENTATION</b></td><td class="o"><b>$5.0M–8.5M</b></td><td class="m" style="color:var(--green)"><b>$2.8M–4.5M</b></td><td class="s"><b>$5.5M–9.0M</b></td></tr>'
    body+=f'<tr style="font-weight:700"><td><b>Duration</b></td><td class="o">18–30 months</td><td class="m">12–18 months</td><td class="s">18–36 months</td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('implementation.html','Implementation Costs','⚙️',body)

def gen_training():
    body=f'<div class="stl"><span class="ic">🎓</span><h2>Training Cost Breakdown</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Training Category</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    tr=[('End-User Training',[('Finance (250 users)','$65K–90K','$42K–52K','$65K–90K'),('POS / Retail (600 users)','$117K–165K','$75K–105K','$117K–165K'),('Warehouse (150 users)','$24K','$15K','$24K'),('HR + ESS rollout','$27K–37K','$16K–21K','$27K–37K'),('Sales / CRM (50 users)','$9K','$5K','$9K')]),
        ('Technical Team Training',[('Admin + Integration + BI + Extension','$60K–105K','$43K–72K','$60K–105K')]),
        ('Executive & Leadership',[('Dashboard + Change Management','$15K–30K','$13K–23K','$15K–30K')]),
        ('Materials & Ongoing',[('Custom e-learning, videos, docs + translation','$60K–100K','$46K–77K','$60K–100K'),('Ongoing training (per year, Yrs 2–5)','$115K–195K/yr','$75K–130K/yr','$115K–195K/yr')])]
    for cat,items in tr:
        body+=f'<tr class="ct"><td colspan="4">{cat}</td></tr>'
        for label,o,m,s in items: body+=T(label,o,m,s)
    body+=f'<tr style="font-weight:700;background:#f0f4ff"><td><b>Year 1 Total</b></td><td class="o"><b>$480K–750K</b></td><td class="m"><b>$310K–500K</b></td><td class="s"><b>$490K–770K</b></td></tr>'
    body+=f'<tr style="font-weight:800;background:#e8edff"><td><b>5-Year Training Total</b></td><td class="o"><b>$940K–1,530K</b></td><td class="m" style="color:var(--green)"><b>$610K–1,020K</b></td><td class="s"><b>$950K–1,550K</b></td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('training.html','Training Costs','🎓',body)

def gen_tco():
    body=f'<div class="stl"><span class="ic">📈</span><h2>5-Year Total Cost of Ownership (TCO)</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Cost Category</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    body+=f'<tr class="ct"><td colspan="4">One-Time Costs</td></tr>'
    for label,o,m,s in [('Implementation','$5,000K–8,500K','$2,800K–4,500K','$5,500K–9,000K'),('Training — Year 1','$480K–750K','$310K–500K','$490K–770K'),('Internal Project Team','$1,000K–1,800K','$800K–1,200K','$1,000K–1,800K'),('Third-Party POS Setup','$300K–500K (Xstore)','— (native)','$100K–200K (CCO)')]:
        body+=T(label,o,m,s)
    body+=f'<tr style="background:#f0f4ff"><td><b>Subtotal One-Time</b></td><td class="o"><b>$6,780K–11,550K</b></td><td class="m"><b>$3,910K–6,200K</b></td><td class="s"><b>$7,090K–11,770K</b></td></tr>'
    body+=f'<tr class="ct"><td colspan="4">Recurring Annual Costs</td></tr>'
    for label,o,m,s in [('Software Licensing','$6,127K/yr','$4,058K/yr','$6,623K/yr'),('Support &amp; Maintenance','$613K/yr','$730K/yr','$1,457K/yr'),('Cloud Infrastructure','$120K/yr','$120K/yr','$156K/yr'),('Ongoing Training','$115K–195K/yr','$75K–130K/yr','$115K–195K/yr'),('Custom Enhancements','$200K–400K/yr','$100K–200K/yr','$200K–300K/yr'),('ISV / Partner / Environments / Support','$235K–650K/yr','$110K–300K/yr','$235K–650K/yr')]:
        body+=T(label,o,m,s)
    body+=f'<tr class="ct"><td colspan="4">5-Year Total</td></tr>'
    body+=T('One-Time Costs','$6,780K–11,550K','$3,910K–6,200K','$7,090K–11,770K')
    body+=T('Recurring × 5 Years','$37,000K–40,025K','$25,965K–27,540K','$43,430K–45,655K')
    body+=T('Contingency (10%)','$4,378K–5,158K','$2,988K–3,374K','$5,052K–5,743K')
    body+=f'<tr style="font-weight:800;font-size:13px;background:#e8edff"><td><b>TOTAL 5-YEAR TCO</b></td><td class="o"><b>$48.2M–56.7M</b></td><td class="m" style="color:var(--green)"><b>$32.9M–37.1M</b></td><td class="s"><b>$55.6M–63.2M</b></td></tr>'
    body+='</tbody></table></div></div>'
    body+='<div class="kr"><div class="kp"><div class="lb">Oracle / User / Mo</div><div class="vl" style="color:var(--oracle)">$114–134</div></div><div class="kp"><div class="lb">Microsoft / User / Mo</div><div class="vl" style="color:var(--msft)">$78–88 ✓</div></div><div class="kp"><div class="lb">SAP / User / Mo</div><div class="vl" style="color:var(--sap)">$131–149</div></div></div>'
    return page_html('tco.html','5-Year TCO','📈',body)

def gen_capabilities():
    mods=[(1,'Financial Management','★★★★★','★★★★★','★★★★★','SAP (slight)'),(2,'Inventory Management','★★★★☆','★★★★☆','★★★★★','SAP'),(3,'Procurement','★★★★☆','★★★★☆','★★★★★','SAP'),(4,'Warehouse Management','★★★★☆','★★★★☆','★★★★★','SAP'),(5,'POS & Retail','★★☆☆☆','★★★★★','★★★☆☆','Microsoft'),(6,'Ecommerce','★★★★☆','★★★★★','★★★★☆','Microsoft'),(7,'Supply Chain Planning','★★★★☆','★★★★☆','★★★★★','SAP'),(8,'HR & Payroll','★★★★★','★★★☆☆','★★★★★','Oracle / SAP'),(9,'CRM & Loyalty','★★★★☆','★★★★★','★★★★☆','Microsoft'),(10,'Analytics & BI','★★★★☆','★★★★★','★★★★★','Microsoft'),(11,'Intercompany','★★★★★','★★★★★','★★★★★','SAP (slight)'),(12,'Document Management','★★★★☆','★★★★★','★★★★☆','Microsoft'),(13,'Master Data Governance','★★★★☆','★★★★☆','★★★★★','SAP'),(14,'AI / Machine Learning','★★★★☆','★★★★★','★★★★☆','Microsoft'),(15,'Low-Code / Extension','★★★☆☆','★★★★★','★★★☆☆','Microsoft'),(16,'Non-Functional','★★★★☆','★★★★★','★★★★☆','Microsoft'),(17,'Quality Management','★★★★☆','★★★☆☆','★★★★★','SAP'),(18,'Field Service','★★★★☆','★★★★★','★★★★☆','Microsoft'),(19,'Expense Management','★★★★☆','★★★★☆','★★★★★','SAP'),(20,'PH Localization','★★☆☆☆','★★★☆☆','★★★★☆','SAP')]
    body=f'<div class="stl"><span class="ic">⭐</span><h2>Capability Comparison (20 Modules)</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>#</th><th>Module</th><th class="o">Oracle</th><th class="m">Microsoft</th><th class="s">SAP</th><th>Winner</th></tr></thead><tbody>'
    for n,mod,o,m,s,w in mods:
        wc=f'style="color:var(--green);font-weight:700"' if w in ('SAP','Microsoft') else ''
        body+=f'<tr><td>{n}</td><td>{mod}</td><td class="o"><span class="st">{o}</span></td><td class="m"><span class="st">{m}</span></td><td class="s"><span class="st">{s}</span></td><td {wc}>{w}</td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('capabilities.html','Capability Comparison','⭐',body)

def gen_reqfit():
    cats=[('R1. Financial Mgmt',22,20,20,21,'2 🔧','2 🔧','1 🔧'),('R2. Inventory',12,10,10,12,'2 ⚙️','2 ⚙️','0'),('R3. Procurement',12,10,10,11,'2 ⚙️','2 ⚙️','1 ⚙️'),('R4. Warehouse',5,4,4,5,'1 ⚙️','1 ⚙️','0'),('R5. POS & Retail',17,9,13,8,'6⚙ 2🔧','4 ⚙️','6⚙ 3🔧'),('R6. Ecommerce',9,7,8,7,'2 ⚙️','1 ⚙️','2 ⚙️'),('R7. Supply Chain',7,6,6,7,'1 ⚙️','1 ⚙️','0'),('R8. HR & Payroll',17,14,10,14,'2⚙ 1🔧','4⚙ 3🔧','2⚙ 1🔧'),('R9. CRM & Loyalty',16,12,14,12,'3⚙ 1🔧','2 ⚙️','3⚙ 1🔧'),('R10. Analytics',12,10,12,11,'2 🔧','0','1 🔧'),('R11. Intercompany',5,5,5,5,'0','0','0'),('R12. Document Mgmt',8,6,6,6,'2 ⚙️','2 ⚙️','2 ⚙️'),('R13. Master Data',8,6,6,8,'2 ⚙️','2 ⚙️','0'),('R14. Non-Functional',28,22,24,22,'4⚙ 2🔧','3⚙ 1🔧','4⚙ 2🔧')]
    body=f'<div class="stl"><span class="ic">✅</span><h2>Must-Have Requirements Fit Summary</h2></div>'
    body+='<div class="cd"><p style="margin-bottom:10px;color:var(--text2);font-size:13px">~178 Must Have requirements across 14 categories.</p><div class="tw"><table>'
    body+='<thead><tr><th>Category</th><th>Must</th><th class="o">Oracle Met</th><th class="m">MS Met</th><th class="s">SAP Met</th><th class="o">Oracle Gaps</th><th class="m">MS Gaps</th><th class="s">SAP Gaps</th></tr></thead><tbody>'
    for cat,must,om,mm,sm,og,mg,sg in cats:
        body+=f'<tr><td>{cat}</td><td>{must}</td><td class="o">{om}</td><td class="m">{mm}</td><td class="s">{sm}</td><td class="o">{og}</td><td class="m">{mg}</td><td class="s">{sg}</td></tr>'
    body+=f'<tr style="font-weight:800;background:#e8edff"><td><b>TOTAL</b></td><td><b>~178</b></td><td class="o"><b>~141</b></td><td class="m" style="color:var(--green)"><b>~148</b></td><td class="s"><b>~149</b></td><td class="o"><b>~10</b></td><td class="m"><b>~7</b></td><td class="s"><b>~8</b></td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('reqfit.html','Requirements Fit','✅',body)

def gen_risks():
    risks=[('POS — 600 Terminals','<span class="rh">⚠️ HIGH</span> Xstore via OIC','<span class="rl">✅ LOW</span> Proven at 1K+','<span class="rm">⚠️ MED</span> CCO maturing'),
           ('POS — Offline 8+ hours','<span class="rm">⚠️ MED</span> Sync testing needed','<span class="rl">✅ LOW</span> CSU proven','<span class="rm">⚠️ MED-HIGH</span> CCO limited'),
           ('PH Payroll (SSS, PhilHealth, BIR)','<span class="rm">⚠️ MED</span> Oracle HCM growing','<span class="rh">❌ HIGH</span> Full ISV dependency','<span class="rm">⚠️ MED</span> SF Payroll growing'),
           ('BIR Tax Compliance','<span class="rh">⚠️ HIGH</span> Partner needed','<span class="rh">⚠️ HIGH</span> ISV needed','<span class="rh">⚠️ HIGH</span> Partner needed'),
           ('Integration Complexity','<span class="rh">❌ HIGHEST</span> 10+ flows','<span class="rl">✅ LOWEST</span> 4 flows, native','<span class="rm">⚠️ HIGH</span> 8 flows'),
           ('Catch-Weight','<span class="rm">⚠️ MED</span>','<span class="rm">⚠️ MED</span>','<span class="rl">✅ LOW-MED</span> EWM best'),
           ('2.8M POS Txns/Month','<span class="rm">⚠️ MED</span> OIC latency','<span class="rl">✅ LOW</span> Azure handles','<span class="rl">✅ LOW</span> HANA handles'),
           ('5-Entity Consolidation','<span class="rl">✅ LOW</span>','<span class="rl">✅ LOW</span>','<span class="rl">✅ LOW</span>'),
           ('Impl. Timeline Risk','<span class="rh">⚠️ HIGH</span> 18–30 mo','<span class="rl">✅ LOW</span> 12–18 mo','<span class="rm">⚠️ HIGH</span> 18–36 mo'),
           ('PH Partner Ecosystem','<span class="rh">⚠️ LIMITED</span>','<span class="rm">⚠️ GROWING</span>','<span class="rl">✅ STRONGEST</span>')]
    body=f'<div class="stl"><span class="ic">⚠️</span><h2>Risk Assessment</h2></div><div class="cd"><div class="tw"><table>'
    body+='<thead><tr><th>Risk Factor</th><th class="o">Oracle Fusion</th><th class="m">Microsoft D365</th><th class="s">SAP S/4HANA</th></tr></thead><tbody>'
    for label,o,m,s in risks: body+=T(label,o,m,s)
    body+=f'<tr style="font-weight:800;background:#e8edff"><td><b>OVERALL RISK</b></td><td class="o"><span class="rh">HIGH</span></td><td class="m"><span class="rl">LOW</span></td><td class="s"><span class="rm">MEDIUM-HIGH</span></td></tr>'
    body+='</tbody></table></div></div>'
    return page_html('risks.html','Risk Assessment','⚠️',body)

def gen_recommendation():
    body=f"""<div class="stl"><span class="ic">🏆</span><h2>Final Recommendation</h2></div>
<div class="cd" style="border-left:4px solid var(--msft);background:#f0f9ff">
  <h2 style="color:var(--msft);border:none">✅ Microsoft Dynamics 365 — RECOMMENDED</h2>
  <p>Best overall fit: lowest TCO, strongest retail POS, fastest implementation.</p>
  <div class="kr">
    <div class="kp"><div class="lb">5-Year TCO</div><div class="vl" style="color:var(--msft)">$32.9–37.1M</div></div>
    <div class="kp"><div class="lb">Capability</div><div class="vl" style="color:var(--msft)">4.62/5</div></div>
    <div class="kp"><div class="lb">Impl. Time</div><div class="vl" style="color:var(--msft)">12–18 mo</div></div>
    <div class="kp"><div class="lb">Cost/User/Mo</div><div class="vl" style="color:var(--msft)">$78–88</div></div>
  </div>
  <h3>Key Strengths</h3><ul style="margin-left:18px"><li><b>Native retail POS</b> with offline CSU — proven at 600+ terminals</li><li><b>Lowest 5-year TCO</b> — $16–19M less than Oracle, $23–26M less than SAP</li><li><b>Tightest integration</b> — only 4 major flows vs. 8–10+</li><li><b>Power Platform</b> — strongest low-code ecosystem</li><li><b>Fastest implementation</b> — 12–18 months</li></ul>
  <h3>Key Risks</h3><ul style="margin-left:18px"><li>⚠️ <b>PH Payroll</b> — requires ISV partner</li><li>⚠️ Supply chain planning less mature than SAP IBP</li><li>⚠️ Catch-weight requires product variant config</li></ul>
</div>
<div class="cd" style="border-left:4px solid var(--sap);margin-top:14px">
  <h2 style="color:var(--sap);border:none">⚠️ SAP S/4HANA Cloud — CONDITIONAL</h2>
  <p>Strongest ERP breadth but highest cost and POS weakness.</p>
  <h3>Strengths:</h3><ul style="margin-left:18px;margin-bottom:8px"><li>Most Must Have met (~149/178)</li><li>SAP IBP gold standard for supply chain</li><li>SAP EWM most comprehensive WMS</li><li>Strongest PH partner network</li></ul>
  <h3>Risks:</h3><ul style="margin-left:18px"><li>❌ Highest cost ($23–26M more than Microsoft)</li><li>⚠️ CCO immature for 1K-terminal retail</li><li>⚠️ 22% support fee</li></ul>
</div>
<div class="cd" style="border-left:4px solid var(--oracle);margin-top:14px">
  <h2 style="color:var(--oracle);border:none">⚠️ Oracle Fusion Cloud — CONDITIONAL</h2>
  <p>Strong enterprise ERP but no native POS and highest integration complexity.</p>
  <h3>Strengths:</h3><ul style="margin-left:18px;margin-bottom:8px"><li>EPM best-in-class consolidation</li><li>Comprehensive HCM suite</li><li>New AI Agents ($2.50–50/user)</li></ul>
  <h3>Risks:</h3><ul style="margin-left:18px"><li>❌ No native POS — Xstore is separate</li><li>❌ 10+ integration flows between modules</li><li>⚠️ Smallest PH partner ecosystem</li></ul>
</div>
<div class="cd" style="background:#fefce8;border-color:#eab308"><h2>📋 Next Steps</h2><ol style="margin-left:18px;line-height:2">
  <li>Request vendor demos with BuildRight scenarios</li><li>Issue RFP to all three vendors</li><li>Engage PH implementation partners</li><li>Conduct POS proof-of-concept (50 terminals)</li><li>Validate ISV payroll capability</li><li>Finalize scoring with partner input</li></ol></div>"""
    return page_html('recommendation.html','Final Recommendation','🏆',body)

# ── MD SOURCE MAPPING ──
MD_MAP = {
    'eval-matrix': '08-erp-comparison/ERP-Evaluation-Matrix.md',
    'vendor-stack': '08-erp-comparison/Vendor-Stack-Evaluation.md',
    'cost-capability': '08-erp-comparison/ERP-Cost-Capability-Comparison.md',
    'full-comparison': '08-erp-comparison/Complete-Vendor-Comparison-Table.md',
    'vendor-sap': '03-sap/README.md',
    'vendor-oracle': '04-oracle-fusion/README.md',
    'vendor-msft': '05-microsoft-d365/README.md',
    'vendor-odoo': '06-odoo/README.md',
    'company': '01-model-company/model-company-profile.md',
    'executive': '01-model-company/executive-summary.md',
    'requirements': '01-model-company/erp-requirements.md',
    'data-volumes': '01-model-company/data-volumes-and-integrations.md',
    'internal-controls': '01-model-company/internal-controls-matrix.md',
    'req-workflow-matrix': '01-model-company/requirement-workflow-matrix.md',
    'assumptions': '01-model-company/assumptions-and-design-decisions.md',
    'mobile-strategy': '01-model-company/mobile-app-strategy.md',
    'data-migration': '01-model-company/data-migration-mapping.md',
    'wilcon': '02-wilcon-benchmark/wilcon-depot-research.md',
    'workflows': '01-model-company/workflows/README.md',
    'WF-finance': '01-model-company/workflows/WF-finance.md',
    'WF-store-operations': '01-model-company/workflows/WF-store-operations.md',
    'WF-procurement': '01-model-company/workflows/WF-procurement.md',
    'WF-merchandising': '01-model-company/workflows/WF-merchandising.md',
    'WF-inventory': '01-model-company/workflows/WF-inventory.md',
    'WF-warehouse': '01-model-company/workflows/WF-warehouse.md',
    'WF-ecommerce': '01-model-company/workflows/WF-ecommerce.md',
    'WF-hr': '01-model-company/workflows/WF-hr.md',
    'WF-customer': '01-model-company/workflows/WF-customer.md',
    'WF-compliance': '01-model-company/workflows/WF-compliance.md',
    'WF-supply-chain': '01-model-company/workflows/WF-supply-chain.md',
    'WF-marketing': '01-model-company/workflows/WF-marketing.md',
    'WF-it-operations': '01-model-company/workflows/WF-it-operations.md',
    'WF-services': '01-model-company/workflows/WF-services.md',
    'WF-governance': '01-model-company/workflows/WF-governance.md',
    'WF-project-sales': '01-model-company/workflows/WF-project-sales.md',
    'WF-audit': '01-model-company/workflows/WF-audit.md',
    'WF-health-safety': '01-model-company/workflows/WF-health-safety.md',
    'WF-property': '01-model-company/workflows/WF-property.md',
    'WF-engineering-construction': '01-model-company/workflows/WF-engineering-construction.md',
    'WF-logistics-fleet': '01-model-company/workflows/WF-logistics-fleet.md',
    'WF-treasury': '01-model-company/workflows/WF-treasury.md',
    'WF-innovation': '01-model-company/workflows/WF-innovation.md',
    'WF-esg': '01-model-company/workflows/WF-esg.md',
    'WF-hazmat': '01-model-company/workflows/WF-hazmat.md',
    'WF-master-data': '01-model-company/workflows/WF-master-data.md',
    'WF-wholesale': '01-model-company/workflows/WF-wholesale.md',
    'WF-non-store-maintenance': '01-model-company/workflows/WF-non-store-maintenance.md',
    'WF-document-management': '01-model-company/workflows/WF-document-management.md',
    'touchpoint-map': '01-model-company/workflows/workflow-system-touchpoint-map.md',
    'methodology': '07-methodology/scoring-methodology.md',
    'roadmap': '07-methodology/implementation-roadmap.md',
    'tech-guidelines': '07-methodology/technical-guidelines.md',
}

# ── GENERATE ALL PAGES ──
os.makedirs(OUT, exist_ok=True)

# Write .nojekyll
open(os.path.join(OUT, '.nojekyll'), 'w').close()

# Built-in comparison pages
generators = {
    'index.html': gen_dashboard,
    'vendors.html': gen_vendors,
    'products.html': gen_products,
    'pricing.html': gen_pricing,
    'annual.html': gen_annual,
    'implementation.html': gen_implementation,
    'training.html': gen_training,
    'tco.html': gen_tco,
    'capabilities.html': gen_capabilities,
    'reqfit.html': gen_reqfit,
    'risks.html': gen_risks,
    'recommendation.html': gen_recommendation,
}

count = 0
for fname, genfn in generators.items():
    html = genfn()
    path = os.path.join(OUT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    size = os.path.getsize(path)
    print(f'  ✅ {fname:40s} {size:>8,} bytes')
    count += 1

# MD-derived pages
for page_id, md_path in MD_MAP.items():
    fname = page_id + '.html'
    title, icon, sec = PAGE_META.get(fname, (page_id, '📄', ''))
    raw = read_md(md_path)
    if not raw:
        print(f'  ⚠️ {fname:40s} — source not found: {md_path}')
        continue
    body_html = f'<div class="stl"><span class="ic">{icon}</span><h2>{title}</h2></div><div class="cd mc">{md(raw)}</div>'
    full_html = page_html(fname, title, icon, body_html)
    path = os.path.join(OUT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    size = os.path.getsize(path)
    print(f'  ✅ {fname:40s} {size:>8,} bytes')
    count += 1

print(f'\n🎉 Generated {count} HTML pages in {OUT}/')
total = sum(os.path.getsize(os.path.join(OUT,f)) for f in os.listdir(OUT) if f.endswith('.html'))
print(f'   Total size: {total/1024:.0f} KB')
