#!/usr/bin/env python3
"""สร้างหน้าแอปประจำบทที่ 2 (ฉบับผู้เรียน) จาก data/ch02.json และ data/ch02_modules.json
สไตล์และหน้ากั้นรหัสใช้ชุดเดียวกับแอป 01 (ดึงจาก build_app.py)"""
import json, hashlib, pathlib, base64, re
from theme import skin, CSS as THEME_CSS
ROOT = pathlib.Path(__file__).parent
src = (ROOT / 'build_app.py').read_text(encoding='utf-8')
CSS = THEME_CSS
GATE = src[src.index('<div id="gate">'):src.index('<div class="brand">')].replace('แอป 01 จำแนกงานนิติวิทยา', 'แอป 02 จากปัจจัยสู่สมมติฐาน')
GATE_JS = src[src.index('/* ---------- gate ---------- */'):src.index('/* ---------- tabs ---------- */')]
d = json.load(open(ROOT / 'data/ch02.json')); m = json.load(open(ROOT / 'data/ch02_modules.json'))
GATE_CODE = 'FA2569'  # รหัสชั่วคราว รอผู้เขียนกำหนด
GATE_HASH = hashlib.sha256(GATE_CODE.upper().encode()).hexdigest()
DATA = json.dumps({**d, **m}, ensure_ascii=False)
LOGO = 'data:image/png;base64,' + base64.b64encode(open(ROOT / 'img/logo_q.png', 'rb').read()).decode()
EXTRA_CSS = ''

page = r'''<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#1F3864">
<title>แอป 02 จากปัจจัยสู่สมมติฐาน · การบัญชีนิติวิทยา</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&display=swap" rel="stylesheet">
__CSS____EXTRA__</head><body>
__GATE__<div class="brand"><img src="__LOGO__" alt="Dr.VIT &amp; PD"><span>แอปประจำเล่ม<br>การบัญชีนิติวิทยา</span></div>
<header><div class="k">ตำรา การบัญชีนิติวิทยา · บทที่ 2 · QR 2.2</div>
<h1>แอป 02 จากปัจจัยสู่สมมติฐาน</h1>
<p>ใช้ราว 30 นาที · ฝึก LO 2.3 2.4 และ 2.6 · อ่านหัวข้อ 2.5 2.6 และ 2.8 ก่อน</p>
<nav role="tablist" id="tabs"></nav></header>
<main id="main"></main>
<footer>เนื้อหาเป็นการถอดความของคณะผู้เขียน ไม่ใช่ถ้อยคำของมาตรฐาน · กิจการ บุคคล และตัวเลขในแอปเป็นสมมติ · ฉบับต้นแบบ v0.2 พฤศจิกายน 2569<br>ดร.วิทยา อรุณศิริเพ็ชร และ อาจารย์พงษ์ธร ดวงปัญญา · Dr.VIT &amp; PD</footer>
<script>
const D=__DATA__, GATE_HASH='__HASH__';
const $=s=>document.querySelector(s), esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store={get(k){try{return JSON.parse(localStorage.getItem('fa02.'+k))}catch(e){return null}},set(k,v){try{localStorage.setItem('fa02.'+k,JSON.stringify(v))}catch(e){}if(k!=='tab'){const a=document.querySelector('#tabs [aria-selected=true]');if(a)tabs(a.dataset.k)}}};
__GATEJS__
/* ---------- tabs ---------- */
const TABS=[['m1','1','จำแนกข้อเท็จจริง'],['m2','2','สัญญาณเตือน'],['m3','3','เขียนสมมติฐาน'],['quiz','?','แบบทดสอบ'],['self','%','ประเมินตนเอง'],['gloss','ก','อภิธานศัพท์']];
function doneOf(k){const st=store.get(k)||{};
 if(k==='m1')return D.m1.every(j=>st[j.id]&&st[j.id].checked);
 if(k==='m2')return D.m2.every(j=>st[j.id]&&st[j.id].checked);
 if(k==='m3')return (st.h||[]).some(x=>fb3ok(x));
 if(k==='quiz')return Object.keys(st).length===D.quiz.length;
 if(k==='self')return D.selfcheck.every(r=>st[r.lo]);return false}
function tabs(cur){$('#tabs').innerHTML=TABS.map(([k,n,t])=>`<button role="tab" aria-selected="${k===cur}" data-k="${k}"><span class="n ${doneOf(k)?'done':''}">${doneOf(k)?'✓':n}</span>${t}</button>`).join('');
 document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>show(b.dataset.k))}
function show(k){if(!TABS.some(t=>t[0]===k))k='m1';tabs(k);store.set('tab',k);({m1,m2,m3,quiz,self,gloss})[k]();window.scrollTo(0,0)}
function hd(eb,title,lead,chips){return `<div class="eyebrow">${eb}</div><h2>${title}</h2><p class="lead">${lead}</p>${chips?`<div class="chips">${chips.map(c=>`<span>${c}</span>`).join('')}</div>`:''}`}
function alertBox(el,msg){let n=el.parentNode.querySelector('.err');if(!n){n=document.createElement('span');n.className='err';n.style.marginLeft='8px';el.parentNode.appendChild(n)}n.textContent=msg}
function copyT(id){const t=document.getElementById(id);const txt=[...t.rows].map(r=>[...r.cells].map(c=>c.innerText).join('\t')).join('\n');try{navigator.clipboard.writeText(txt)}catch(e){}}
const FN=Object.assign({obs:'ข้อสังเกต (ไม่ใช้ตั้งสมมติฐาน)'},D.factors), LV={ind:'บุคคล',org:'องค์กร'};
/* ---------- module 1 ---------- */
function m1(){const st=store.get('m1')||{};
 let h=hd('โมดูล 1 จาก 3','จำแนกข้อเท็จจริงตามผังงานภาพที่ 2.2','ตอบคำถามตามลำดับของผังงานกับข้อเท็จจริง 12 ข้อ ข้อ 1 ถึง 9 มาจากเรื่องเปิดบท ข้อ 10 ถึง 12 เป็นสถานการณ์สมมติ แล้วกดตรวจคำตอบ แอปบอกปัจจัยตามแนวตอบและเหตุผล',['LO 2.3','หัวข้อ 2.5 และ 2.8.1','ผลงาน: แบบ FA-2.1'])+`
 <div class="box o">คำถามที่ 2 เป็นจุดใช้ดุลยพินิจ ข้อเท็จจริงหนึ่งข้ออาจจัดได้มากกว่าหนึ่งปัจจัย (หัวข้อ 2.8.1) ข้อที่แนวตอบรับได้สองปัจจัย แอปจะบอกไว้ในเหตุผล</div>`;
 D.m1.forEach((j,i)=>{const a=st[j.id]||{};const done=a.checked;
  const q=(key,txt,opts)=>`<div class="q">${txt}</div><div class="seg">${opts.map(([v,l])=>`<button class="btn ${a[key]===v?'on':''}" data-j="${j.id}" data-key="${key}" data-v="${v}" ${done?'disabled':''}>${l}</button>`).join('')}</div>`;
  h+=`<div class="card"><span class="tag">ข้อเท็จจริงที่ ${i+1}</span><span class="mini">${esc(j.src)}</span><p>${esc(j.text)}</p>
  ${q('q1','คำถามที่ 1 ข้อเท็จจริงนี้ตรวจสอบได้จากข้อมูลที่ทีมมีฐานทางกฎหมายในการเข้าถึงหรือไม่',[[true,'ใช่'],[false,'ไม่ใช่']])}
  ${a.q1===false?'<p class="mini">ตามผังงาน ทีมบันทึกเป็นข้อสังเกตและไม่ใช้ตั้งสมมติฐาน</p>':a.q1===undefined?'':q('f','คำถามที่ 2 ข้อเท็จจริงนี้จัดอยู่ในปัจจัยใด',Object.entries(D.factors))+q('lvl','ระดับของปัจจัย',[['ind','บุคคล'],['org','องค์กร']])}
  <div class="row noprint" style="margin-top:10px">${done?`<button class="btn" data-reset="${j.id}">ทำข้อนี้ใหม่</button>`:`<button class="btn p" data-check="${j.id}">ตรวจคำตอบ</button>`}</div>
  ${done?fb1(j,a):''}</div>`});
 h+=`<h3 class="section">ผลงาน: แบบ FA-2.1 แบบจำแนกข้อเท็จจริงตามปัจจัยการทุจริต</h3>${table1(st)}<div class="row noprint"><button class="btn" onclick="copyT('t1')">คัดลอกตาราง</button><button class="btn" onclick="print()">พิมพ์</button></div>
 <p class="mini">เลขที่แบบ FA-2.1 · เวอร์ชัน 0.2 · พฤศจิกายน 2569 · แบบเป็นแนวทางขั้นต่ำ ผู้ปฏิบัติควรใช้ความระมัดระวังเยี่ยงผู้ประกอบวิชาชีพและปรับตามลักษณะงาน</p>
 <div class="box g">ใช้ตารางนี้ต่อในโมดูล 3 และประกอบอัตนัยข้อ 2 ในเล่ม</div>`;
 $('#main').innerHTML=h;
 document.querySelectorAll('[data-key]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};const a=s[b.dataset.j]||{};let v=b.dataset.v;v=v==='true'?true:v==='false'?false:v;a[b.dataset.key]=v;
  if(b.dataset.key==='q1'){if(v===false){a.f='obs';delete a.lvl}else if(a.f==='obs')delete a.f}
  s[b.dataset.j]=a;store.set('m1',s);const y=window.scrollY;m1();window.scrollTo(0,y)});
 document.querySelectorAll('[data-check]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};const a=s[b.dataset.check]||{};if(a.q1===undefined||a.f===undefined){alertBox(b,'ตอบคำถามที่ 1 และ 2 ก่อนตรวจคำตอบ');return}a.checked=true;s[b.dataset.check]=a;store.set('m1',s);const y=window.scrollY;m1();window.scrollTo(0,y)});
 document.querySelectorAll('[data-reset]').forEach(b=>b.onclick=()=>{const s=store.get('m1')||{};delete s[b.dataset.reset];store.set('m1',s);const y=window.scrollY;m1();window.scrollTo(0,y)});
}
const ok1=(j,a)=>a.f===j.f||j.alt.includes(a.f);
function fb1(j,a){const ok=ok1(j,a);const w=[];
 if(a.q1!==j.q1)w.push(`คำถามที่ 1 ควรตอบ ${j.q1?'ใช่':'ไม่ใช่'}`);
 if(j.f!=='obs'&&a.lvl&&a.lvl!==j.lvl)w.push(`ระดับตามแนวตอบคือ${LV[j.lvl]}`);
 return `<div class="fb ${ok&&!w.length?'ok':'no'}"><b>${ok?'จำแนกได้ตรงกับแนวตอบ':'ยังไม่ตรงกับแนวตอบ'}</b> แนวตอบคือ ${FN[j.f]}${j.alt.length?' (รับ '+j.alt.map(x=>FN[x].split(' (')[0]).join(' ')+' ด้วย)':''}${w.length?' · '+w.join(' · '):''}<br>${esc(j.why)}</div>`}
function table1(st){let r='',n=0,ok=0;D.m1.forEach((j,i)=>{const a=st[j.id]||{};if(a.checked){n++;if(ok1(j,a))ok++}
 r+=`<tr><td>${i+1}</td><td>${esc(j.text)}</td><td>${esc(j.src.split(' · ')[1]||j.src)}</td><td>${a.q1===undefined?'–':a.q1?'ข้อเท็จจริง':'ข้อสังเกต'}</td><td>${a.f?FN[a.f].split(' (')[0]:'–'}</td><td>${a.lvl?LV[a.lvl]:'–'}</td><td>${a.checked?(ok1(j,a)?'ตรงกับแนวตอบ':'แนวตอบ: '+FN[j.f].split(' (')[0]):'ยังไม่ตรวจ'}</td></tr>`});
 return `<p>ตรวจแล้ว ${n} จาก ${D.m1.length} ข้อ · ตรงกับแนวตอบ ${ok} ข้อ</p><div class="tw"><table id="t1" class="wide"><tr><th>ข้อ</th><th>ข้อเท็จจริง</th><th>แหล่งข้อมูล</th><th>ข้อเท็จจริงหรือข้อสังเกต</th><th>ปัจจัย</th><th>ระดับ</th><th>หมายเหตุ</th></tr>${r}</table></div>`}
/* ---------- module 2 ---------- */
function m2(){const st=store.get('m2')||{};const C=D.m2_cat;
 let h=hd('โมดูล 2 จาก 3','สัญญาณเตือน: อะไรตรวจได้ทันที','จัดสัญญาณเตือนแปดอย่างในตารางที่ 2.6 และสัญญาณสองข้อจากเรื่องเปิดบท ว่าตรวจได้จากข้อมูลขององค์กรทันที ต้องมีฐานทางกฎหมายก่อน หรือเป็นข้อสังเกตที่ใช้ประกอบเท่านั้น',['LO 2.4','หัวข้อ 2.6','ผลงาน: รายการสัญญาณที่ตรวจได้'])+`
 <div class="box r">ข้อควรระวัง: สัญญาณเตือนชี้ว่าควรตรวจที่ใด แต่ไม่ใช่หลักฐาน และให้ผลบวกลวงสูง (หัวข้อ 2.6.2) การเก็บข้อมูลส่วนบุคคลต้องมีฐานตามมาตรา 24 และข้อมูลอ่อนไหวอยู่ภายใต้มาตรา 26 ของพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล (หัวข้อ 2.6.3)</div>`;
 D.m2.forEach((s,i)=>{const a=st[s.id];const done=a&&a.checked;
  h+=`<div class="card"><span class="tag">สัญญาณที่ ${i+1}</span><span class="mini">${esc(s.src)}</span><p><b>${esc(s.text)}</b></p><div class="seg">${Object.entries(C).map(([k,l])=>`<button class="btn ${a&&a.v===k?'on':''}" data-s="${s.id}" data-v="${k}" ${done?'disabled':''}>${l}</button>`).join('')}</div>
  <div class="row noprint" style="margin-top:10px">${done?`<button class="btn" data-r2="${s.id}">ทำข้อนี้ใหม่</button>`:`<button class="btn p" data-c2="${s.id}">ตรวจคำตอบ</button>`}</div>
  ${done?`<div class="fb ${a.v===s.a?'ok':'no'}"><b>${a.v===s.a?'ตรงกับแนวตอบ':'ยังไม่ตรงกับแนวตอบ'}</b> แนวตอบคือ ${C[s.a]}<br>${esc(s.why)}</div>`:''}</div>`});
 const org=D.m2.filter(s=>st[s.id]&&st[s.id].checked&&st[s.id].v==='org');
 h+=`<h3 class="section">ผลงาน: รายการสัญญาณที่ตรวจได้</h3>${org.length?`<div class="tw"><table id="t2"><tr><th>สัญญาณที่จัดว่าตรวจได้ทันที</th><th>ตรงกับแนวตอบ</th></tr>${org.map(s=>`<tr><td>${esc(s.text)}</td><td>${s.a==='org'?'ใช่':'ไม่ใช่ แนวตอบ: '+C[s.a]}</td></tr>`).join('')}</table></div><div class="row noprint"><button class="btn" onclick="copyT('t2')">คัดลอกตาราง</button></div>`:'<p>ยังไม่มีสัญญาณที่ตรวจแล้วและจัดว่าตรวจได้ทันที</p>'}
 <div class="box g">ใช้หลักเดียวกันตอบกรณีศึกษาที่ 2 และอัตนัยข้อ 3 ในเล่ม</div>`;
 $('#main').innerHTML=h;
 const keep=f=>{const y=window.scrollY;f();window.scrollTo(0,y)};
 document.querySelectorAll('[data-s]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};s[b.dataset.s]={v:b.dataset.v};store.set('m2',s);keep(m2)});
 document.querySelectorAll('[data-c2]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};const a=s[b.dataset.c2];if(!a){alertBox(b,'เลือกคำตอบก่อนตรวจ');return}a.checked=true;store.set('m2',s);keep(m2)});
 document.querySelectorAll('[data-r2]').forEach(b=>b.onclick=()=>{const s=store.get('m2')||{};delete s[b.dataset.r2];store.set('m2',s);keep(m2)});
}
/* ---------- module 3 ---------- */
const HF=[['form','รูปแบบการทุจริต','รูปแบบที่สงสัย เช่น การแยกใบสั่งซื้อเพื่อหลบการอนุมัติระดับสูง'],['mech','กลไกที่ผู้กระทำอาจใช้','ทำอย่างไร ผ่านขั้นตอนหรือระบบใด'],['yes','หลักฐานที่ควรพบหากสมมติฐานจริง','ข้อมูลหรือเอกสารใดจะปรากฏ'],['no','หลักฐานที่ควรพบหากสมมติฐานไม่จริง','ลักษณะที่สำคัญที่สุด ช่วยป้องกันอคติยืนยัน']];
const ACCUSE=/กระทำผิดแล้ว|เป็นผู้ทุจริต|ทุจริตจริง|ทุจริตแน่|มีความผิด|ยักยอกเงิน|โกง/;
const filled=(x,k)=>(x[k]||'').trim().length>=8;
function m3(){const s=store.get('m3')||{h:[{}],ck:[]};if(!s.h.length)s.h=[{}];const st1=store.get('m1')||{};
 const done1=D.m1.filter(j=>st1[j.id]&&st1[j.id].checked);
 const usable=D.m1.filter(j=>j.f!=='obs');
 let h=hd('โมดูล 3 จาก 3','เขียนสมมติฐานการทุจริต','เขียนสมมติฐานจากข้อเท็จจริงที่จำแนกแล้วให้ครบสี่ลักษณะตามหัวข้อ 2.8.1 แอปตรวจความครบและเรียงลำดับตามเกณฑ์ในหัวข้อ 2.8.2 แต่ไม่ได้ประเมินคุณภาพของเหตุผลแทนผู้สอน',['LO 2.6','หัวข้อ 2.8','ผลงาน: แบบ FA-2.2']);
 if(!done1.length)h+=`<div class="box o empty"><span>แนะนำให้ทำโมดูล 1 ก่อน เพื่อให้รายการข้อเท็จจริงแสดงปัจจัยที่ผู้เรียนจำแนกไว้</span><button class="btn" id="go1">ไปโมดูล 1</button></div>`;
 s.h.forEach((x,i)=>{const n=HF.filter(([k])=>filled(x,k)).length;
  h+=`<div class="card"><div class="card-h"><span class="tag">สมมติฐาน H${i+1}</span><span class="meter" id="mt${i}">${meter(n)}</span></div>
  <div class="fld"><label for="f${i}">ข้อเท็จจริงที่ใช้</label><select id="f${i}" data-h="${i}" data-k="fact"><option value="">เลือกข้อเท็จจริง</option>${usable.map(j=>{const a=st1[j.id];const tag=a&&a.checked?FN[a.f].split(' (')[0]:'ยังไม่จำแนก';return `<option value="${j.id}" ${x.fact===j.id?'selected':''}>ข้อ ${D.m1.indexOf(j)+1} · ${tag} · ${esc(j.text.slice(0,40))}…</option>`}).join('')}</select></div>
  ${HF.map(([k,l,p],n)=>`<div class="fld ${filled(x,k)?'ok':''}" id="w${i}${k}"><label for="t${i}${k}"><span class="num">${n+1}</span>${l}</label><textarea id="t${i}${k}" data-h="${i}" data-k="${k}" placeholder="${p}">${esc(x[k]||'')}</textarea></div>`).join('')}
  <div class="sub"><div class="q">ประเมินเพื่อจัดลำดับ (หัวข้อ 2.8.2)</div><div class="grid3">
   ${seg(i,x,'loss','ความเสี่ยงที่หลักฐานจะสูญหาย',[['h','สูง'],['l','ต่ำ']])}
   ${seg(i,x,'dmg','ความเสียหายที่อาจเกิด',[[3,'สูง'],[2,'กลาง'],[1,'ต่ำ']])}
   ${seg(i,x,'ease','ความง่ายในการได้หลักฐาน',[[3,'ง่าย'],[2,'ปานกลาง'],[1,'ยาก']])}</div></div>
  <div class="fb ${fb3ok(x)?'ok':'no'}" id="fb${i}">${fb3(x)}</div>
  <div class="row noprint" style="justify-content:flex-end;margin-top:6px"><button class="btn ghost" data-del="${i}">ลบสมมติฐานนี้</button></div></div>`});
 h+=`${s.h.length<6?'<button class="btn add noprint" id="add">+ เพิ่มสมมติฐาน</button>':''}
 <h3 class="section">ผลงาน: แบบ FA-2.2 แบบสมมติฐานการทุจริต</h3><div id="fa22"></div>
 <div class="row noprint"><button class="btn" onclick="copyT('t3')">คัดลอกตาราง</button><button class="btn" onclick="print()">พิมพ์แบบ FA-2.2</button><button class="btn" id="ref">${s.ref?'ซ่อน':'เทียบกับ'}ตารางที่ 2.8</button></div>
 ${s.ref?`<div class="tw"><table class="wide"><tr><th>ปัจจัยตามทฤษฎี</th><th>ข้อเท็จจริงที่มี</th><th>สมมติฐาน</th><th>หลักฐานที่ควรพบหากจริง</th><th>หลักฐานที่ควรพบหากไม่จริง</th></tr>${D.ref28.map(r=>`<tr>${r.map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</table></div><p class="mini">ที่มา: ตารางที่ 2.8 ในตำรา หัวข้อ 2.8.2 ระบุว่าสมมติฐานเรื่องสิทธิ์ในระบบควรทดสอบก่อน เพราะบันทึกการแก้ไขในระบบอาจสูญหายหรือหมดอายุการเก็บ</p>`:''}
 <h3 class="section">รายการตรวจ 2.1 ก่อนส่งสมมติฐาน</h3><div class="card">${D.checks.map((c,i)=>`<label class="ck"><input type="checkbox" data-ck="${i}" ${s.ck.includes(i)?'checked':''}> ${esc(c)}</label>`).join('')}<p id="m3s" class="mini" style="margin:8px 0 0"></p></div>
 <div class="box r">ข้อควรระวัง: สมมติฐานเป็นคำถามที่หลักฐานต้องตอบ ไม่ใช่ข้อสรุปว่าบุคคลใดกระทำผิด</div>
 <div class="box g">ใช้แบบนี้ประกอบอัตนัยข้อ 5 และกรณีศึกษาที่ 3 ในเล่ม</div>
 <p class="mini">เลขที่แบบ FA-2.2 · เวอร์ชัน 0.2 · พฤศจิกายน 2569 · แบบเป็นแนวทางขั้นต่ำ ผู้ปฏิบัติควรใช้ความระมัดระวังเยี่ยงผู้ประกอบวิชาชีพและปรับตามลักษณะงาน</p>`;
 $('#main').innerHTML=h;
 const save=x=>store.set('m3',x),keep=()=>{const y=window.scrollY;m3();window.scrollTo(0,y)};
 const upd=()=>{const x=store.get('m3')||s;$('#fa22').innerHTML=fa22(x);$('#m3s').textContent=`ทบทวนแล้ว ${x.ck.length} จาก ${D.checks.length} ข้อ`;
  x.h.forEach((y,i)=>{const e=$('#fb'+i);if(!e)return;e.innerHTML=fb3(y);e.className='fb '+(fb3ok(y)?'ok':'no');$('#mt'+i).innerHTML=meter(HF.filter(([k])=>filled(y,k)).length);HF.forEach(([k])=>$('#w'+i+k).classList.toggle('ok',filled(y,k)))})};
 document.querySelectorAll('textarea[data-h],select[data-h]').forEach(t=>t[t.tagName==='SELECT'?'onchange':'oninput']=()=>{const x=store.get('m3')||s;x.h[+t.dataset.h][t.dataset.k]=t.value;save(x);upd()});
 document.querySelectorAll('button[data-h]').forEach(b=>b.onclick=()=>{const x=store.get('m3')||s;let v=b.dataset.v;v=/^\d$/.test(v)?+v:v;x.h[+b.dataset.h][b.dataset.k]=v;save(x);keep()});
 document.querySelectorAll('[data-del]').forEach(b=>b.onclick=()=>{const x=store.get('m3')||s;x.h.splice(+b.dataset.del,1);save(x);keep()});
 const add=$('#add');if(add)add.onclick=()=>{const x=store.get('m3')||s;x.h.push({});save(x);keep()};
 const g1=$('#go1');if(g1)g1.onclick=()=>show('m1');
 $('#ref').onclick=()=>{const x=store.get('m3')||s;x.ref=!x.ref;save(x);keep()};
 document.querySelectorAll('[data-ck]').forEach(c=>c.onchange=()=>{const x=store.get('m3')||s;const z=new Set(x.ck);c.checked?z.add(+c.dataset.ck):z.delete(+c.dataset.ck);x.ck=[...z];save(x);upd()});
 save(s);upd();
}
function meter(n){return `ครบ ${n} จาก 4 ลักษณะ <span class="bar"><i style="width:${n*25}%"></i></span>`}
function seg(i,x,k,l,opts){return `<div><div class="mini" style="margin-bottom:6px">${l}</div><div class="seg">${opts.map(([v,t])=>`<button class="btn ${x[k]===v?'on':''}" data-h="${i}" data-k="${k}" data-v="${v}">${t}</button>`).join('')}</div></div>`}
function fb3ok(x){return HF.every(([k])=>filled(x,k))&&!HF.some(([k])=>ACCUSE.test(x[k]||''))&&!!x.loss}
function fb3(x){const miss=HF.filter(([k])=>!filled(x,k)).map(f=>f[1]);const out=[];
 out.push(fb3ok(x)?'<b>พร้อมใช้ในแบบ FA-2.2</b> ครบสี่ลักษณะตามหัวข้อ 2.8.1 และประเมินความเสี่ยงที่หลักฐานจะสูญหายแล้ว':miss.length?`<b>ยังไม่ครบ</b> ยังขาด: ${miss.join(' · ')}`:'<b>ครบสี่ลักษณะแล้ว</b> เหลือเรื่องที่ต้องแก้ก่อนใช้');
 if(!x.loss)out.push('ยังไม่ได้ประเมินความเสี่ยงที่หลักฐานจะสูญหาย');
 if(HF.some(([k])=>ACCUSE.test(x[k]||'')))out.push('<span class="warn">พบถ้อยคำที่อาจอ่านเป็นข้อสรุปว่าบุคคลกระทำผิด ควรเขียนเป็นสมมติฐานที่ต้องทดสอบ (รายการตรวจ 2.1 ข้อ 6)</span>');
 return out.join('<br>')}
function order(hs){return hs.map((x,i)=>({x,i})).sort((a,b)=>((b.x.loss==='h')-(a.x.loss==='h'))||((b.x.dmg||0)-(a.x.dmg||0))||((b.x.ease||0)-(a.x.ease||0))||a.i-b.i)}
function fa22(s){const o=order(s.h);const rk={};o.forEach((e,n)=>rk[e.i]=n+1);
 return `<div class="tw"><table id="t3" class="wide"><tr><th>รหัส</th><th>รูปแบบการทุจริต</th><th>กลไก</th><th>หลักฐานหากจริง</th><th>หลักฐานหากไม่จริง</th><th>ความเสี่ยงหลักฐานสูญหาย</th><th>ลำดับ</th><th>ผู้รับผิดชอบ</th></tr>${s.h.map((x,i)=>`<tr><td>H${i+1}</td><td>${esc(x.form||'')}</td><td>${esc(x.mech||'')}</td><td>${esc(x.yes||'')}</td><td>${esc(x.no||'')}</td><td>${x.loss==='h'?'สูง':x.loss==='l'?'ต่ำ':'–'}</td><td>${rk[i]}</td><td></td></tr>`).join('')}</table></div>
 <p class="mini">แอปเรียงลำดับโดยให้สมมติฐานที่หลักฐานเสี่ยงสูญหายมาก่อน แล้วเรียงตามความเสียหายและความง่ายในการได้หลักฐาน ตามผังงานภาพที่ 2.2 และหัวข้อ 2.8.2 ช่องผู้รับผิดชอบให้ทีมกรอกเอง</p>`}
/* ---------- quiz ---------- */
const L='กขคง';
function quiz(){const st=store.get('quiz')||{};
 let h=hd('แบบทดสอบท้ายบท','เฉลยและเหตุผลรายตัวเลือก','ทำแบบทดสอบในเล่มให้ครบก่อน แล้วกดตัวเลือกที่ตอบไว้เพื่อดูเฉลยและเหตุผลจากเล่มเฉลย',['ปรนัย 20 ข้อ','LO 2.1 ถึง 2.5'])+`<div id="qs"></div>`;
 D.quiz.forEach(q=>{const a=st[q.no];h+=`<div class="card"><span class="tag">ข้อ ${q.no}</span><span class="tag">${q.part} · LO ${q.lo} · ${q.level}</span><div class="q">${esc(q.q)}</div>
  ${q.opts.map((o,i)=>`<button class="opt ${a!==undefined?(i===q.ans?'ok':(i===a?'no':'')):''}" data-q="${q.no}" data-i="${i}" ${a!==undefined?'disabled':''}>${L[i]}. ${esc(o)}</button>`).join('')}
  ${a!==undefined?`<div class="fb ${a===q.ans?'ok':'no'}"><b>${a===q.ans?'ตอบตรงกับเฉลย':'ยังไม่ตรงกับเฉลย'}</b> ผู้เรียนตอบ ${L[a]}<br>${esc(q.why)}</div>`:''}</div>`});
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
 let h=hd('ตารางที่ 2.13','ประเมินตนเองตาม LO','ติ๊กเมื่อมีหลักฐานว่าบรรลุแล้ว หากยังไม่บรรลุ ให้กลับไปอ่านหัวข้อที่ระบุ')+`
 <div class="box"><span class="score">${Math.round(n/D.selfcheck.length*100)}%</span> บรรลุแล้ว ${n} จาก ${D.selfcheck.length} LO<div class="bar" style="margin-top:6px"><i style="width:${n/D.selfcheck.length*100}%"></i></div></div>`;
 D.selfcheck.forEach(r=>h+=`<div class="card"><label class="ck"><input type="checkbox" data-lo="${r.lo}" ${st[r.lo]?'checked':''}><span><b>${r.lo}</b> <span class="tag">${r.level}</span><br>${esc(D.lo[r.lo]||'')}<br><span style="color:var(--mut)">หลักฐาน: ${esc(r.evidence)}</span><br><span style="color:var(--mut)">หากยังไม่บรรลุ อ่านหัวข้อ ${esc(r.goto)}</span></span></label></div>`);
 $('#main').innerHTML=h;
 document.querySelectorAll('[data-lo]').forEach(c=>c.onchange=()=>{const s=store.get('self')||{};s[c.dataset.lo]=c.checked;store.set('self',s);self()});
}
/* ---------- glossary ---------- */
function gloss(){let h=hd('บทที่ 2','อภิธานศัพท์',`ศัพท์ ${D.glossary.length} คำ เรียงตามอักษรไทย ค้นได้ทั้งคำไทยและอังกฤษ`)+`<input type="search" id="gs" placeholder="ค้นคำไทยหรืออังกฤษ"><div id="gl"></div>`;$('#main').innerHTML=h;
 const r=()=>{const s=$('#gs').value.trim().toLowerCase();$('#gl').innerHTML=D.glossary.filter(g=>!s||(g.th+g.en+g.def_).toLowerCase().includes(s)).map(g=>`<div class="card"><b>${esc(g.th)}</b> <span style="color:var(--mut)">(${esc(g.en)})</span><br>${esc(g.def_)}</div>`).join('')||'<p>ไม่พบคำที่ค้น</p>'};
 $('#gs').oninput=r;r()}
show(store.get('tab')||'m1');
</script></body></html>'''
out = skin(page.replace('__CSS__', CSS).replace('__EXTRA__', EXTRA_CSS).replace('__GATE__', GATE).replace('__GATEJS__', GATE_JS)
       .replace('__DATA__', DATA).replace('__HASH__', GATE_HASH).replace('__LOGO__', LOGO))
(ROOT.parent / 'docs/ch02.html').write_text(out, encoding='utf-8')
import qrcode
qrcode.make('https://drvitpd.github.io/forensic-accounting-textbook/ch02.html', border=1, box_size=12).save(ROOT.parent / 'docs/qr/ch02.png')
print('ok', len(out))
