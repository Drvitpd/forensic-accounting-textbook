"""ชุดแต่งหน้าแอปประจำเล่มที่ใช้ร่วมกันทุกบท: CSS กลาง แถบแท็บติดบนจอ และชิปข้อมูลใต้ชื่อแอป"""
import pathlib, re, html as H
CSS = '<style>' + (pathlib.Path(__file__).parent / 'theme.css').read_text(encoding='utf-8') + '</style>'
TAB_JS = ("<script>(function(){const n=document.getElementById('tabs');if(!n)return;"
          "new MutationObserver(()=>{const a=n.querySelector('[aria-selected=true]');if(a)a.scrollIntoView({block:'nearest',inline:'center'})})"
          ".observe(n,{childList:true})})();</script>")

def skin(page):
    page = re.sub(r'<style>.*?</style>', lambda m: CSS, page, count=1, flags=re.S)
    m = re.search(r'(<header>.*?)<p>(.*?)</p>\s*<nav role="tablist" id="tabs"></nav></header>', page, re.S)
    if m:
        chips = ''.join(f'<span>{c.strip()}</span>' for c in m.group(2).split(' · '))
        page = page.replace(m.group(0), m.group(1) + f'<div class="meta">{chips}</div></header>\n<div class="tabbar"><nav role="tablist" id="tabs"></nav></div>')
        page = page.replace('</body>', TAB_JS + '</body>')
    if '<link rel="icon"' not in page:
        m2 = re.search(r'<div class="brand"><img src="([^"]+)"', page)
        if m2: page = page.replace('</head>', f'<link rel="icon" href="{m2.group(1)}"></head>', 1)
    return page
