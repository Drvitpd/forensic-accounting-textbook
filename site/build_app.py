#!/usr/bin/env python3
"""สร้างหน้าแอปประจำบทที่ 1 (ฉบับผู้เรียน) จาก data/ch01.json และ data/ch01_modules.json"""
import json, hashlib, pathlib, html

ROOT = pathlib.Path(__file__).parent
d = json.load(open(ROOT / 'data/ch01.json'))
m = json.load(open(ROOT / 'data/ch01_modules.json'))
GATE_CODE = 'FA2569'  # รหัสชั่วคราว รอผู้เขียนกำหนด
GATE_HASH = hashlib.sha256(GATE_CODE.upper().encode()).hexdigest()
DATA = json.dumps({**d, **m}, ensure_ascii=False)
import base64
LOGO = 'data:image/png;base64,' + base64.b64encode(open(ROOT / 'img/logo_q.png', 'rb').read()).decode()

page = r'''<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>แอป 01 จำแนกงานนิติวิทยา · การบัญชีนิติวิทยา</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--navy:#1F3864;--bg:#F2F7FB;--b1:#E3E9F1;--g:#EAF3EC;--gL:#3C8A4E;--o:#FBF3E7;--oL:#C8932B;--r:#F6EFE9;--rL:#B5655A;--ink:#1d2430;--mut:#5b6575;--line:#d5dde8}
*{box-sizing:border-box}html,body{margin:0}
body{font-family:Sarabun,system-ui,sans-serif;font-size:17px;line-height:1.65;color:var(--ink);background:#fff}
.brand{background:#fff;border-bottom:3px solid #E8731B;padding:10px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px}.brand img{height:40px;width:auto;display:block}.brand span{font-size:13px;color:var(--mut);text-align:right}
header{background:var(--navy);color:#fff;padding:18px 20px 0}
header .k{font-size:13px;opacity:.85;letter-spacing:.02em}
header h1{margin:2px 0 4px;font-size:24px;line-height:1.3}
header p{margin:0 0 12px;font-size:15px;opacity:.9}
nav{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}
nav::-webkit-scrollbar{display:none}
nav button{flex:0 0 auto;font:inherit;font-size:15px;border:0;background:transparent;color:#cdd8ea;padding:10px 14px;border-radius:8px 8px 0 0;cursor:pointer;white-space:nowrap}
nav button[aria-selected=true]{background:#fff;color:var(--navy);font-weight:700}
main{max-width:860px;margin:0 auto;padding:20px 16px 40px}
h2{color:var(--navy);font-size:21px;margin:8px 0 6px}
h3{color:var(--navy);font-size:18px;margin:18px 0 6px}
.lead{color:var(--mut);margin:0 0 14px}
.box{border-left:4px solid var(--navy);background:var(--bg);padding:12px 14px;border-radius:6px;margin:12px 0}
.box.g{border-color:var(--gL);background:var(--g)}.box.o{border-color:var(--oL);background:var(--o)}.box.r{border-color:var(--rL);background:var(--r)}
.card{border:1px solid var(--line);border-radius:10px;padding:14px;margin:12px 0;background:#fff}
.tag{display:inline-block;font-size:13px;background:var(--b1);color:var(--navy);border-radius:999px;padding:1px 10px;margin-right:6px}
.q{font-weight:600;margin:10px 0 6px}
.row{display:flex;flex-wrap:wrap;gap:8px}
.btn{font:inherit;font-size:15px;border:1px solid var(--navy);background:#fff;color:var(--navy);padding:7px 14px;border-radius:8px;cursor:pointer}
.btn.on{background:var(--navy);color:#fff}
.btn.p{background:var(--navy);color:#fff}
.btn:disabled{opacity:.55;cursor:default}.btn.on:disabled{opacity:.9}
.opt:disabled{opacity:1;color:inherit;cursor:default}
.opt{display:block;width:100%;text-align:left;font:inherit;border:1px solid var(--line);background:#fff;border-radius:8px;padding:9px 12px;margin:6px 0;cursor:pointer}
.opt.ok{border-color:var(--gL);background:var(--g)}.opt.no{border-color:var(--rL);background:var(--r)}
.fb{margin-top:8px;padding:10px 12px;border-radius:8px;font-size:16px}
.fb.ok{background:var(--g)}.fb.no{background:var(--r)}
table{width:100%;border-collapse:collapse;font-size:15px;margin:8px 0}
th,td{border-bottom:1px solid var(--line);padding:7px 6px;text-align:left;vertical-align:top}
th{background:var(--b1);color:var(--navy)}
.tw{overflow-x:auto}
textarea,input[type=text],input[type=password],input[type=search]{font:inherit;width:100%;border:1px solid var(--line);border-radius:8px;padding:8px 10px}
textarea{min-height:76px}
label.ck{display:flex;gap:8px;align-items:flex-start;margin:6px 0}
label.ck input{margin-top:6px}
.score{font-size:20px;font-weight:700;color:var(--navy)}
.bar{height:10px;background:var(--b1);border-radius:6px;overflow:hidden}.bar i{display:block;height:100%;background:var(--gL)}
footer{max-width:860px;margin:0 auto;padding:16px;color:var(--mut);font-size:13px;border-top:1px solid var(--line)}
#gate{position:fixed;inset:0;background:rgba(31,56,100,.96);display:flex;align-items:center;justify-content:center;z-index:9;padding:16px}
#gate .in{background:#fff;border-radius:12px;max-width:420px;width:100%;padding:22px}#gate .in img{height:44px;width:auto;display:block;margin:0 0 14px}
#gate h2{margin-top:0}.err{color:var(--rL);min-height:1.4em;font-size:15px}
.hide{display:none!important}
@media print{header nav,#gate,.noprint,footer{display:none!important}header{background:#fff;color:#000}main{padding:0}}
</style></head><body>
<div id="gate"><div class="in">
<img src="__LOGO__" alt="Dr.VIT &amp; PD">
<h2>แอป 01 จำแนกงานนิติวิทยา</h2>
<p>สำหรับผู้ซื้อตำรา การบัญชีนิติวิทยา ใส่รหัสที่พิมพ์ไว้ในตำรา</p>
<div class="row" style="flex-wrap:nowrap"><input id="code" type="password" autocomplete="off" aria-label="รหัสเข้าแอป"><button class="btn" id="eye" type="button">แสดง</button></div>
<label class="ck"><input type="checkbox" id="rem"> จำรหัสในเครื่องนี้</label>
<div class="err" id="err"></div>
<button class="btn p" id="go">เปิดแอป</button>
</div></div>

<div class="brand"><img src="__LOGO__" alt="Dr.VIT &amp; PD"><span>แอปประจำเล่ม<br>การบัญชีนิติวิทยา</span></div>
<header><div class="k">ตำรา การบัญชีนิติวิทยา · บทที่ 1 · QR 1.2</div>
<h1>แอป 01 จำแนกงานนิติวิทยา</h1>
<p>ใช้ราว 30 นาที · ฝึก LO 1.3 และ LO 1.5 · อ่านหัวข้อ 1.4 และ 1.6 ก่อน</p>
<nav role="tablist" id="tabs"></nav></header>
<main id="main"></main>
<footer>เนื้อหาเป็นการถอดความของคณะผู้เขียน ไม่ใช่ถ้อยคำของมาตรฐาน · กิจการ บุคคล และตัวเลขในแอปเป็นสมมติ · ฉบับต้นแบบ v0.1 พฤศจิกายน 2569<br>ดร.วิทยา อรุณศิริเพ็ชร และ อาจารย์พงษ์ธร ดวงปัญญา · Dr.VIT &amp; PD</footer>

<script>
const D=__DATA__, GATE_HASH='__HASH__';
const $=s=>document.querySelector(s), esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store={get(k){try{return JSON.parse(localStorage.getItem('fa01.'+k))}catch(e){return null}},set(k,v){try{localStorage.setItem('fa01.'+k,JSON.stringify(v))}catch(e){}}};
/* ---------- gate ---------- */
async function sha(s){const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('')}
function okGate(){$('#gate').classList.add('hide')}
(function(){let v=null;try{v=localStorage.getItem('fa.gate')||sessionStorage.getItem('fa.gate')}catch(e){}if(v===GATE_HASH)okGate()})();
$('#eye').onclick=()=>{const i=$('#code');i.type=i.type==='password'?'text':'password';$('#eye').textContent=i.type==='password'?'แสดง':'ซ่อน'};
async function tryGate(){const c=$('#code').value.replace(/[\s-]/g,'').toUpperCase();const h=await sha(c);
 if(h===GATE_HASH){try{($('#rem').checked?localStorage:sessionStorage).setItem('fa.gate',h)}catch(e){}okGate()}else{$('#err').textContent='รหัสไม่ถูกต้อง โปรดดูรหัสที่พิมพ์ไว้ในตำรา'}}
$('#go').onclick=tryGate;$('#code').addEventListener('keydown',e=>{if(e.key==='Enter')tryGate()});
/* ---------- tabs ---------- */
const TABS=[['m1','1 จำแนกงาน'],['m2','2 เลือกทีม'],['m3','3 รุ่งเรืองวัสดุ'],['quiz','แบบทดสอบ'],['self','ประเมินตนเอง'],['gloss','อภิธานศัพท์']];
function tabs(cur){$('#tabs').innerHTML=TABS.map(([k,t])=>`<button role="tab" aria-selected="${k===cur}" data-k="${k}">${t}</button>`).join('');
 document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>show(b.dataset.k))}
function show(k){tabs(k);store.set('tab',k);({m1,m2,m3,quiz,self,gloss})[k]();window.scrollTo(0,0)}
/* ---------- module 1 ---------- */
const CLS={inv:'งานสืบสวน',lit:'งานสนับสนุนคดีความ',none:'ไม่ใช่ทั้งสองประเภท (ปิดเรื่องหรือเป็นงานป้องกัน)'};
const YN=v=>v?'ใช่':'ไม่ใช่';
function m1(){const st=store.get('m1')||{};
 let h=`<h2>โมดูล 1 จำแนกงานตามผังงานภาพที่ 1.2</h2><p class="lead">ตอบคำถามตามลำดับของผังงานกับงานสมมติ 8 งาน แล้วกดตรวจคำตอบ แอปจะบอกคำตอบและเหตุผลตาม SSFS ฉบับที่ 1</p>
 <div class="box o">คำถามที่ 1 เป็นจุดใช้ดุลยพินิจ สำหรับงานที่เริ่มจากข้อพิพาทซึ่งไม่เกี่ยวกับการทุจริต ให้ถือว่าข้อพิพาทเป็นจุดเริ่มต้นของงานแทนเหตุอันควรสงสัย (บทสรุป LO 1.2) คำถามที่ 3 เรื่องผู้ปฏิบัติอยู่ในโมดูล 2</div>`;
 D.m1.forEach((j,i)=>{const a=st[j.id]||{};const done=a.checked;
  const q=(key,txt,opts)=>`<div class="q">${txt}</div><div class="row">${opts.map(([v,l])=>`<button class="btn ${a[key]===v?'on':''}" data-j="${j.id}" data-key="${key}" data-v="${v}" ${done?'disabled':''}>${l}</button>`).join('')}</div>`;
  h+=`<div class="card"><span class="tag">งานที่ ${i+1}</span><p>${esc(j.text)}</p>
  ${q('q1','คำถามที่ 1 มีเหตุอันควรสงสัยหรือไม่',[[true,'ใช่'],[false,'ไม่ใช่']])}
  ${a.q1===false?'':q('q2','คำถามที่ 2 มีกระบวนการทางกฎหมายหรือของหน่วยงานกำกับที่เกิดแล้วหรือคาดได้ว่าจะเกิดหรือไม่',[[true,'ใช่'],[false,'ไม่ใช่']])}
  ${q('cls','ผลการจำแนก',[['inv',CLS.inv],['lit',CLS.lit],['none','ไม่ใช่ทั้งสองประเภท']])}
  ${a.cls==='none'?'':q('q4','คำถามสุดท้าย ผลงานอาจใช้ในกระบวนการทางกฎหมายหรือไม่',[[true,'ใช่'],[false,'ไม่ใช่']])}
  <div class="row noprint" style="margin-top:10px">${done?`<button class="btn" data-reset="${j.id}">ทำข้อนี้ใหม่</button>`:`<button class="btn p" data-check="${j.id}">ตรวจคำตอบ</button>`}</div>
  ${done?fb1(j,a):''}</div>`});
 h+=`<h3>ผลงาน: ตารางจำแนกงาน</h3>${table1(st)}<div class="row noprint"><button class="btn" onclick="copyT('t1')">คัดลอกตาราง</button><button class="btn" onclick="print()">พิมพ์</button></div>
 <div class="box g">ใช้ตารางนี้ตอบกรณีศึกษาที่ 2 คำถามที่ 2 และอัตนัยข้อ 2 ในเล่ม</div>`;
 $('#main').innerHTML=h;
 document.querySelectorAll('[data-key]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};const a=s[b.dataset.j]||{};let v=b.dataset.v;v=v==='true'?true:v==='false'?false:v;a[b.dataset.key]=v;
  if(b.dataset.key==='q1'&&v===false){a.cls='none';delete a.q2;delete a.q4}
  if(b.dataset.key==='cls'&&v==='none'){delete a.q4}
  s[b.dataset.j]=a;store.set('m1',s);m1()});
 document.querySelectorAll('[data-check]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};const a=s[b.dataset.check]||{};if(a.cls===undefined){alertBox(b,'เลือกผลการจำแนกก่อนตรวจคำตอบ');return}a.checked=true;s[b.dataset.check]=a;store.set('m1',s);m1()});
 document.querySelectorAll('[data-reset]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};delete s[b.dataset.reset];store.set('m1',s);m1()});
}
function alertBox(el,msg){let n=el.parentNode.querySelector('.err');if(!n){n=document.createElement('span');n.className='err';n.style.marginLeft='8px';el.parentNode.appendChild(n)}n.textContent=msg}
function fb1(j,a){const ok=a.cls===j.cls;const w=[];
 if(a.q1!==j.q1)w.push(`คำถามที่ 1 ควรตอบ ${YN(j.q1)}`);
 if(j.q1&&a.q2!==undefined&&a.q2!==j.q2)w.push(`คำถามที่ 2 ควรตอบ ${YN(j.q2)}`);
 if(j.cls!=='none'&&a.q4!==undefined&&a.q4!==j.q4)w.push(`คำถามสุดท้ายควรตอบ ${YN(j.q4)}`);
 return `<div class="fb ${ok&&!w.length?'ok':'no'}"><b>${ok?'จำแนกได้ตรงกับแนวตอบ':'ยังไม่ตรงกับแนวตอบ'}</b> คำตอบคือ ${CLS[j.cls]}${w.length?' · '+w.join(' · '):''}<br>${esc(j.why)}</div>`}
function table1(st){let r='',n=0,ok=0;D.m1.forEach((j,i)=>{const a=st[j.id]||{};if(a.checked){n++;if(a.cls===j.cls)ok++}
 r+=`<tr><td>${i+1}</td><td>${a.cls?CLS[a.cls].split(' (')[0]:'–'}</td><td>${a.checked?CLS[j.cls].split(' (')[0]:'ยังไม่ตรวจ'}</td></tr>`});
 return `<p>ตรวจแล้ว ${n} จาก ${D.m1.length} งาน · ตรงกับแนวตอบ ${ok} งาน</p><div class="tw"><table id="t1"><tr><th>งาน</th><th>คำตอบของผู้เรียน</th><th>แนวตอบ</th></tr>${r}</table></div>`}
/* ---------- module 2 ---------- */
function m2(){const st=store.get('m2')||{};const TH=Object.fromEntries(D.threats.map(t=>[t.id,t.label]));
 let h=`<h2>โมดูล 2 เลือกทีมและชี้อุปสรรค</h2><p class="lead">อ่านสถานการณ์ เลือกทีมที่เหมาะที่สุด แล้วติ๊กอุปสรรคหรือข้อจำกัดที่พบในแต่ละทีม แอปจะชี้สิ่งที่ผู้เรียนมองข้าม</p>`;
 D.m2.forEach(s=>{const a=st[s.id]||{pick:null,t:{}};const done=a.checked;
  h+=`<div class="card"><span class="tag">${s.id}</span><b>${esc(s.title)}</b><p>${esc(s.text)}</p>`;
  s.teams.forEach(tm=>{const sel=(a.t[tm.id]||[]);
   h+=`<div class="box" style="margin:8px 0"><b>ทีม ${tm.id}</b> ${esc(tm.text)}<div style="margin-top:6px">${D.threats.map(t=>`<label class="ck"><input type="checkbox" data-s="${s.id}" data-t="${tm.id}" value="${t.id}" ${sel.includes(t.id)?'checked':''} ${done?'disabled':''}> ${t.label}</label>`).join('')}</div>
   ${done?fb2(tm,sel,TH):''}</div>`});
  h+=`<div class="q">ทีมที่เหมาะที่สุด</div><div class="row">${s.teams.map(tm=>`<button class="btn ${a.pick===tm.id?'on':''}" data-pick="${s.id}" data-v="${tm.id}" ${done?'disabled':''}>ทีม ${tm.id}</button>`).join('')}</div>
  <div class="row noprint" style="margin-top:10px">${done?`<button class="btn" data-r2="${s.id}">ทำสถานการณ์นี้ใหม่</button>`:`<button class="btn p" data-c2="${s.id}">ตรวจคำตอบ</button>`}</div>
  ${done?`<div class="fb ${a.pick===s.best?'ok':'no'}"><b>${a.pick===s.best?'เลือกทีมได้ตรงกับแนวตอบ':'ยังไม่ตรงกับแนวตอบ'}</b> ทีมที่เหมาะที่สุดคือทีม ${s.best}<br>${esc(s.why)}</div>`:''}</div>`});
 h+=`<h3>ผลงาน: แบบ FA-1.2 แบบจำแนกงานและประเมินทีม</h3><p class="lead">เลือกสถานการณ์ที่ตรวจแล้ว แอปเติมช่องประเภทงาน อุปสรรค และทีมที่เลือกให้ ผู้เรียนเขียนช่องที่เหลือเอง</p>${fa12(st)}
 <div class="box g">ใช้หลักเดียวกันตอบกรณีศึกษาที่ 3 คำถามที่ 1 ถึง 4 ในเล่ม</div>`;
 $('#main').innerHTML=h;
 document.querySelectorAll('[data-s]').forEach(c=>c.onchange=()=>{const s=store.get('m2')||{};const a=s[c.dataset.s]||{pick:null,t:{}};const l=new Set(a.t[c.dataset.t]||[]);c.checked?l.add(c.value):l.delete(c.value);a.t[c.dataset.t]=[...l];s[c.dataset.s]=a;store.set('m2',s)});
 document.querySelectorAll('[data-pick]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};const a=s[b.dataset.pick]||{pick:null,t:{}};a.pick=b.dataset.v;s[b.dataset.pick]=a;store.set('m2',s);m2()});
 document.querySelectorAll('[data-c2]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};const a=s[b.dataset.c2];if(!a||!a.pick){alertBox(b,'เลือกทีมที่เหมาะที่สุดก่อนตรวจคำตอบ');return}a.checked=true;store.set('m2',s);m2()});
 document.querySelectorAll('[data-r2]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};delete s[b.dataset.r2];store.set('m2',s);m2()});
 const sel=$('#fa12s');if(sel)sel.onchange=()=>{store.set('fa12s',sel.value);m2()};
 document.querySelectorAll('[data-fa]').forEach(t=>t.oninput=()=>{const f=store.get('fa12')||{};f[t.dataset.fa]=t.value;store.set('fa12',f)});
}
function fb2(tm,sel,TH){const miss=tm.threats.filter(x=>!sel.includes(x)),extra=sel.filter(x=>!tm.threats.includes(x));
 if(!miss.length&&!extra.length)return `<div class="fb ok">ตรงกับแนวตอบ${tm.threats.length?'':' ทีมนี้ไม่มีอุปสรรคที่ระบุได้จากข้อมูล'}</div>`;
 return `<div class="fb no">${miss.length?'มองข้าม: '+miss.map(x=>TH[x]).join(' · '):''}${miss.length&&extra.length?'<br>':''}${extra.length?'ข้อมูลยังไม่พอสรุปว่ามี: '+extra.map(x=>TH[x]).join(' · '):''}</div>`}
function fa12(st){const done=D.m2.filter(s=>st[s.id]&&st[s.id].checked);if(!done.length)return '<p>ยังไม่มีสถานการณ์ที่ตรวจแล้ว</p>';
 const cur=store.get('fa12s')||done[0].id;const s=done.find(x=>x.id===cur)||done[0];const a=st[s.id];const f=store.get('fa12')||{};const TH=Object.fromEntries(D.threats.map(t=>[t.id,t.label]));
 const picked=s.teams.find(t=>t.id===a.pick);const k=x=>s.id+'.'+x;
 const lit=/ยื่นฟ้องแล้ว/.test(s.text);
 return `<p><select id="fa12s" class="btn">${done.map(x=>`<option value="${x.id}" ${x.id===s.id?'selected':''}>${x.id} ${esc(x.title)}</option>`).join('')}</select></p>
 <div class="tw"><table id="t2"><tr><th style="width:34%">ช่อง</th><th>ข้อมูล</th></tr>
 <tr><td>ประเภทงานตาม SSFS</td><td>${lit?'งานสนับสนุนคดีความ':'งานสืบสวน'}</td></tr>
 <tr><td>ผู้ว่าจ้าง</td><td><textarea data-fa="${k('emp')}" placeholder="เช่น ทนายความ หรือที่ปรึกษากฎหมายของกิจการ">${esc(f[k('emp')]||'')}</textarea></td></tr>
 <tr><td>สมรรถนะที่งานต้องการ</td><td><textarea data-fa="${k('need')}">${esc(f[k('need')]||'')}</textarea></td></tr>
 <tr><td>สมรรถนะของทีมที่เลือก</td><td>ทีม ${a.pick}: ${esc(picked.text)}</td></tr>
 <tr><td>อุปสรรคที่ผู้เรียนระบุ</td><td>${s.teams.map(t=>`ทีม ${t.id}: ${(a.t[t.id]||[]).map(x=>TH[x]).join(' · ')||'ไม่ระบุ'}`).join('<br>')}</td></tr>
 <tr><td>มาตรการป้องกัน</td><td><textarea data-fa="${k('safe')}" placeholder="เช่น ยืนยันความเป็นอิสระเป็นลายลักษณ์อักษร ค่าตอบแทนไม่ผูกกับผลคดี">${esc(f[k('safe')]||'')}</textarea></td></tr>
 <tr><td>ข้อสรุป</td><td><textarea data-fa="${k('con')}">${esc(f[k('con')]||'')}</textarea></td></tr></table></div>
 <div class="row noprint"><button class="btn" onclick="print()">พิมพ์แบบ FA-1.2</button></div>
 <p style="font-size:13px;color:var(--mut)">เลขที่แบบ FA-1.2 · เวอร์ชัน 0.1 · พฤศจิกายน 2569 · แบบเป็นแนวทางขั้นต่ำ ผู้ปฏิบัติควรใช้ความระมัดระวังเยี่ยงผู้ประกอบวิชาชีพและปรับตามลักษณะงาน</p>`}
/* ---------- module 3 ---------- */
function m3(){const f=store.get('m3')||{};const ck=f.ck||[];
 let h=`<h2>โมดูล 3 รุ่งเรืองวัสดุ: ประเมินเหตุอันควรสงสัย</h2><p class="lead">สมมติว่าผู้เรียนเป็นหน่วยงานตรวจสอบภายในตามมติข้อแรกของที่ประชุมในเรื่องเปิดบท กรอกแบบ FA-1.1 จากข้อมูลที่บริษัทมีอยู่ แล้วทบทวนด้วยรายการตรวจท้ายหน้า ผู้สอนมีแนวตอบสำหรับเทียบในชั้นเรียน</p>
 <div class="box"><b>ข้อมูลที่มีอยู่ (จากเรื่องเปิดบท)</b><ul>${D.m3_facts.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>
 <h3>แบบ FA-1.1 แบบบันทึกเหตุอันควรสงสัย</h3><div class="tw"><table id="t3"><tr><th style="width:34%">ช่อง</th><th>บันทึก</th></tr>`;
 const F=[['src','แหล่งที่มาของเบาะแส'],['al','ข้อกล่าวอ้างแต่ละข้อ'],['sup','ข้อมูลที่มีอยู่ซึ่งอาจสนับสนุน'],['ref','ข้อมูลที่มีอยู่ซึ่งอาจหักล้าง หรือข้อมูลที่ยังขาด'],['con','ข้อสรุปว่ามีเหตุอันควรสงสัยหรือไม่ พร้อมเหตุผล'],['who','ผู้ประเมินและวันที่']];
 F.forEach(([k,l])=>h+=`<tr><td>${l}</td><td><textarea data-m3="${k}">${esc(f[k]||'')}</textarea></td></tr>`);
 h+=`</table></div><h3>ทบทวนก่อนส่ง</h3>${D.m3_checks.map((c,i)=>`<label class="ck"><input type="checkbox" data-ck="${i}" ${ck.includes(i)?'checked':''}> ${esc(c)}</label>`).join('')}
 <p id="m3s"></p><div class="row noprint"><button class="btn" onclick="print()">พิมพ์แบบ FA-1.1</button></div>
 <div class="box r">ข้อควรระวัง: แบบนี้บันทึกว่ามีเหตุพอจะสืบสวนต่อหรือไม่ ไม่ใช่ข้อสรุปว่าบุคคลใดกระทำผิด (SSFS ฉบับที่ 1 ย่อหน้า 10 และตารางที่ 1.9)</div>
 <div class="box g">ใช้แบบนี้ประกอบกรณีศึกษาที่ 3 และรายการตรวจ 1.1 ข้อ 1</div>
 <p style="font-size:13px;color:var(--mut)">เลขที่แบบ FA-1.1 · เวอร์ชัน 0.1 · พฤศจิกายน 2569 · แบบเป็นแนวทางขั้นต่ำ ผู้ปฏิบัติควรใช้ความระมัดระวังเยี่ยงผู้ประกอบวิชาชีพและปรับตามลักษณะงาน</p>`;
 $('#main').innerHTML=h;
 const upd=()=>{const f=store.get('m3')||{};const filled=F.filter(([k])=>(f[k]||'').trim()).length;$('#m3s').innerHTML=`กรอกแล้ว ${filled} จาก ${F.length} ช่อง · ทบทวนแล้ว ${(f.ck||[]).length} จาก ${D.m3_checks.length} ข้อ`};
 document.querySelectorAll('[data-m3]').forEach(t=>t.oninput=()=>{const f=store.get('m3')||{};f[t.dataset.m3]=t.value;store.set('m3',f);upd()});
 document.querySelectorAll('[data-ck]').forEach(c=>c.onchange=()=>{const f=store.get('m3')||{};const s=new Set(f.ck||[]);c.checked?s.add(+c.dataset.ck):s.delete(+c.dataset.ck);f.ck=[...s];store.set('m3',f);upd()});upd();
}
/* ---------- quiz ---------- */
const L='กขคง';
function quiz(){const st=store.get('quiz')||{};
 let h=`<h2>แบบทดสอบท้ายบท: เฉลยและเหตุผล</h2><p class="lead">ทำแบบทดสอบในเล่มให้ครบก่อน แล้วกดตัวเลือกที่ตอบไว้เพื่อดูเฉลยและเหตุผลรายตัวเลือก</p><div id="qs"></div>`;
 D.quiz.forEach(q=>{const a=st[q.no];h+=`<div class="card"><span class="tag">ข้อ ${q.no}</span><span class="tag">${q.part} · LO ${q.lo} · ${q.level}</span><div class="q">${esc(q.q)}</div>
  ${q.opts.map((o,i)=>`<button class="opt ${a!==undefined?(i===q.ans?'ok':(i===a?'no':'')):''}" data-q="${q.no}" data-i="${i}" ${a!==undefined?'disabled':''}>${L[i]}. ${esc(o)}</button>`).join('')}
  ${a!==undefined?`<div class="fb ${a===q.ans?'ok':'no'}"><b>${a===q.ans?'ตอบตรงกับเฉลย':'ยังไม่ตรงกับเฉลย'}</b> เฉลยคือ ${L[q.ans]}<br>${a!==q.ans?`ตัวเลือก ${L[a]}: ${esc(q.why[a])}<br>`:''}ตัวเลือก ${L[q.ans]}: ${esc(q.why[q.ans])}</div>`:''}</div>`});
 h+=`<div class="row noprint"><button class="btn" id="qr">ล้างคำตอบทั้งหมด</button></div>`;
 $('#main').innerHTML=h;
 const n=Object.keys(st).length,ok=D.quiz.filter(q=>st[q.no]===q.ans).length;
 $('#qs').innerHTML=`<div class="box"><span class="score">${ok} จาก ${n}</span> ข้อที่ตอบแล้ว (ทั้งหมด ${D.quiz.length} ข้อ)<div class="bar" style="margin-top:6px"><i style="width:${n?ok/n*100:0}%"></i></div>${byLO(st)}</div>`;
 document.querySelectorAll('[data-q]').forEach(b=>b.onclick=()=>{const s=store.get('quiz')||{};s[b.dataset.q]=+b.dataset.i;store.set('quiz',s);const y=window.scrollY;quiz();window.scrollTo(0,y)});
 $('#qr').onclick=()=>{store.set('quiz',{});quiz()};
}
function byLO(st){const g={};D.quiz.forEach(q=>{g[q.lo]=g[q.lo]||[0,0];if(st[q.no]!==undefined){g[q.lo][1]++;if(st[q.no]===q.ans)g[q.lo][0]++}});
 return `<div class="tw"><table><tr><th>LO</th><th>ตรงกับเฉลย</th></tr>${Object.entries(g).map(([k,v])=>`<tr><td>LO ${k}</td><td>${v[0]} จาก ${v[1]} ข้อที่ตอบ</td></tr>`).join('')}</table></div>`}
/* ---------- self check ---------- */
function self(){const st=store.get('self')||{};const n=D.selfcheck.filter(r=>st[r.lo]).length;
 let h=`<h2>ประเมินตนเองตาม LO</h2><p class="lead">ติ๊กเมื่อมีหลักฐานว่าบรรลุแล้ว หากยังไม่บรรลุ ให้กลับไปอ่านหัวข้อที่ระบุ</p>
 <div class="box"><span class="score">${Math.round(n/D.selfcheck.length*100)}%</span> บรรลุแล้ว ${n} จาก ${D.selfcheck.length} LO<div class="bar" style="margin-top:6px"><i style="width:${n/D.selfcheck.length*100}%"></i></div></div>`;
 D.selfcheck.forEach(r=>h+=`<div class="card"><label class="ck"><input type="checkbox" data-lo="${r.lo}" ${st[r.lo]?'checked':''}><span><b>${r.lo}</b> <span class="tag">${r.level}</span><br>${esc(D.lo[r.lo]||'')}<br><span style="color:var(--mut)">หลักฐาน: ${esc(r.evidence)}</span><br><span style="color:var(--mut)">หากยังไม่บรรลุ อ่านหัวข้อ ${esc(r.goto)}</span></span></label></div>`);
 $('#main').innerHTML=h;
 document.querySelectorAll('[data-lo]').forEach(c=>c.onchange=()=>{const s=store.get('self')||{};s[c.dataset.lo]=c.checked;store.set('self',s);self()});
}
/* ---------- glossary ---------- */
function gloss(){let h=`<h2>อภิธานศัพท์บทที่ 1</h2><input type="search" id="gs" placeholder="ค้นคำไทยหรืออังกฤษ"><div id="gl"></div>`;$('#main').innerHTML=h;
 const r=()=>{const s=$('#gs').value.trim().toLowerCase();$('#gl').innerHTML=D.glossary.filter(g=>!s||(g.th+g.en+g.def_).toLowerCase().includes(s)).map(g=>`<div class="card"><b>${esc(g.th)}</b> <span style="color:var(--mut)">(${esc(g.en)})</span><br>${esc(g.def_)}</div>`).join('')||'<p>ไม่พบคำที่ค้น</p>'};
 $('#gs').oninput=r;r()}
function copyT(id){const t=document.getElementById(id);const txt=[...t.rows].map(r=>[...r.cells].map(c=>c.innerText).join('\t')).join('\n');try{navigator.clipboard.writeText(txt)}catch(e){}}
show(store.get('tab')||'m1');
</script></body></html>'''

out = page.replace('__DATA__', DATA).replace('__HASH__', GATE_HASH).replace('__LOGO__', LOGO)
(ROOT.parent / 'docs').mkdir(exist_ok=True)
(ROOT.parent / 'docs/ch01.html').write_text(out, encoding='utf-8')
(ROOT.parent / 'docs/.nojekyll').write_text('')
print('ok', len(out))

# ---------- index + QR ----------
BASE = 'https://drvitpd.github.io/forensic-accounting-textbook/'
css = page[page.find('<style>'):page.find('</style>')+8]
gate = page[page.find('<div id="gate">'):page.find('<header>')]
idx = f'''<!DOCTYPE html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>แอปประจำเล่ม การบัญชีนิติวิทยา</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&display=swap" rel="stylesheet">{css}</head><body>
{gate.replace('แอป 01 จำแนกงานนิติวิทยา','แอปประจำเล่ม การบัญชีนิติวิทยา')}
<div class="brand"><img src="__LOGO__" alt="Dr.VIT &amp; PD"><span>แอปประจำเล่ม<br>การบัญชีนิติวิทยา</span></div>
<header><div class="k">ตำราเล่มนี้</div><h1>แอปประจำเล่ม การบัญชีนิติวิทยา</h1>
<p>Forensic Accounting · ดร.วิทยา อรุณศิริเพ็ชร และ อาจารย์พงษ์ธร ดวงปัญญา</p><div style="height:12px"></div></header>
<main><h2>วิธีใช้คู่กับตำรา</h2>
<p>แต่ละบทมีแอปฝึกที่ใช้ข้อมูลชุดเดียวกับตำรา พร้อมเฉลยและเหตุผลของแบบทดสอบปรนัย แบบประเมินตนเองตาม LO และอภิธานศัพท์ ผู้อ่านควรทำแบบทดสอบในเล่มให้ครบก่อนเปิดเฉลยในแอป</p>
<h2>รายการแอป</h2>
<div class="card"><span class="tag">บทที่ 1</span><b><a href="ch01.html">แอป 01 จำแนกงานนิติวิทยา</a></b><br>การบัญชีนิติวิทยาและวิชาชีพ · จำแนกงานตาม SSFS · เลือกทีม · ประเมินเหตุอันควรสงสัย</div>
<div class="card"><span class="tag">บทที่ 2</span><b><a href="ch02.html">แอป 02 จากปัจจัยสู่สมมติฐาน</a></b><br>ทฤษฎีการทุจริตและอาชญาวิทยา · จำแนกข้อเท็จจริงตามปัจจัย · สัญญาณเตือนที่ตรวจได้ · เขียนสมมติฐานการทุจริต</div>
<p class="lead">แอปของบทที่ 3 ถึง 16 จะเพิ่มตามลำดับเมื่อแต่ละบทผ่านการตรวจ</p></main>
<footer>เนื้อหาเป็นการถอดความของคณะผู้เขียน ไม่ใช่ถ้อยคำของมาตรฐาน · กิจการ บุคคล และตัวเลขในแอปเป็นสมมติ<br>ดร.วิทยา อรุณศิริเพ็ชร และ อาจารย์พงษ์ธร ดวงปัญญา · Dr.VIT &amp; PD</footer>
<script>const GATE_HASH='{GATE_HASH}';const $=s=>document.querySelector(s);
async function sha(s){{const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('')}}
function okGate(){{$('#gate').classList.add('hide')}}
(function(){{let v=null;try{{v=localStorage.getItem('fa.gate')||sessionStorage.getItem('fa.gate')}}catch(e){{}}if(v===GATE_HASH)okGate()}})();
$('#eye').onclick=()=>{{const i=$('#code');i.type=i.type==='password'?'text':'password';$('#eye').textContent=i.type==='password'?'แสดง':'ซ่อน'}};
async function tryGate(){{const c=$('#code').value.replace(/[\\s-]/g,'').toUpperCase();const h=await sha(c);
 if(h===GATE_HASH){{try{{($('#rem').checked?localStorage:sessionStorage).setItem('fa.gate',h)}}catch(e){{}}okGate()}}else{{$('#err').textContent='รหัสไม่ถูกต้อง โปรดดูรหัสที่พิมพ์ไว้ในตำรา'}}}}
$('#go').onclick=tryGate;$('#code').addEventListener('keydown',e=>{{if(e.key==='Enter')tryGate()}});</script></body></html>'''
(ROOT.parent / 'docs/index.html').write_text(idx.replace('__LOGO__', LOGO), encoding='utf-8')
import qrcode
(ROOT.parent / 'docs/qr').mkdir(exist_ok=True)
for name, url in [('ch01', BASE + 'ch01.html'), ('ch02', BASE + 'ch02.html'), ('index', BASE)]:
    qrcode.make(url, border=1, box_size=12).save(ROOT.parent / f'docs/qr/{name}.png')
print('index + qr ok')
