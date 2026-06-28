# -*- coding: utf-8 -*-
# 小憩 時租 — 可點擊模擬網站（靜態原型，假資料能操作）工業風×木質綠
import os
OUT = "/Users/chenkuanyu/jy_studio_rental_mockups/proto"
os.makedirs(OUT, exist_ok=True)

GOLD="#B89150"; IRON="#22241F"; GREEN="#374829"; GREEN1="#46583B"
CSS=f"""
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased}}
:root{{--gold:{GOLD};--iron:{IRON};--green:{GREEN};--green1:{GREEN1}}}
body{{max-width:480px;margin:0 auto;background:#E7E3DC;font-family:-apple-system,"PingFang TC","Noto Sans TC",sans-serif;color:#1C1E1A;min-height:100vh;padding-bottom:80px}}
a{{text-decoration:none;color:inherit}}
.topbar{{background:var(--iron);padding:14px 18px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:20}}
.brand{{display:flex;align-items:center;gap:8px}}
.brand .lf{{width:20px;height:20px}}
.brand .bz{{font-size:21px;font-weight:900;letter-spacing:4px;color:#F4F1EA}}
.brand .en{{font-size:8.5px;font-weight:700;color:var(--gold);letter-spacing:3px;margin-top:2px}}
.back{{color:#E7E3DC;font-size:14px;font-weight:700;display:flex;align-items:center;gap:5px}}
.loc{{font-size:12px;font-weight:700;color:#E7E3DC;border:1px solid #4A4C44;padding:6px 10px;border-radius:4px}}
.hero{{background:linear-gradient(120deg,#2B2E27,#3C4A2C);padding:22px 20px 24px;position:relative}}
.hero:after{{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:var(--gold)}}
.hero h1{{font-size:22px;font-weight:900;line-height:1.4;color:#F4F1EA;letter-spacing:1px}}
.hero p{{font-size:12.5px;color:#D7D2C5;margin-top:8px;line-height:1.6}}
.sec{{margin:20px 16px 0}}
.sect{{font-size:15.5px;font-weight:900;margin:0 2px 12px;display:flex;align-items:center;letter-spacing:1px}}
.sect:before{{content:"";display:inline-block;width:16px;height:3px;background:var(--gold);margin-right:8px}}
.card{{background:#FBFAF7;border:1.5px solid var(--iron);border-radius:8px;overflow:hidden;margin-bottom:15px;box-shadow:4px 4px 0 rgba(34,36,31,.12);display:block}}
.photo{{height:175px;position:relative;display:flex;align-items:center;justify-content:center}}
.phl{{font-size:13px;font-weight:700;color:rgba(255,255,255,.92);letter-spacing:1px}}
.cap{{position:absolute;left:12px;top:12px;background:var(--iron);color:#F4F1EA;font-size:11px;font-weight:800;padding:4px 10px;border-radius:4px}}
.cbody{{padding:14px 15px}}
.crow{{display:flex;align-items:flex-end;justify-content:space-between}}
.cnm{{font-size:16.5px;font-weight:900;letter-spacing:.5px}}
.cprice{{font-size:19px;font-weight:900;color:var(--green)}}.cprice span{{font-size:11px;font-weight:700;color:#736E63}}
.cloc{{font-size:12px;color:#736E63;margin-top:5px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px}}
.chip{{font-size:11px;font-weight:700;color:var(--green1);background:#ECEDE5;border:1px solid #D7DAC9;padding:4px 9px;border-radius:4px}}
.btn{{display:block;text-align:center;background:var(--iron);color:#F4F1EA;font-size:15px;font-weight:800;padding:14px;border-radius:6px;letter-spacing:2px;border:0;width:100%;cursor:pointer}}
.btn.gold{{background:var(--gold);color:#241E12}}
.btn.green{{background:var(--green)}}
.fixbar{{position:fixed;bottom:0;left:50%;transform:translateX(-50%);max-width:480px;width:100%;background:#FBFAF7;border-top:1.5px solid var(--iron);padding:12px 16px calc(12px + env(safe-area-inset-bottom))}}
.gallery{{display:flex;gap:0;height:230px}}
.gcell{{flex:1;display:flex;align-items:flex-end;padding:8px;color:#fff;font-size:11px;font-weight:700}}
.kv{{display:flex;justify-content:space-between;font-size:14px;padding:11px 0;border-bottom:1px solid #E0DCD2}}
.kv b{{font-weight:800}} .kv .g{{color:var(--green);font-weight:900;font-size:17px}}
.desc{{font-size:13.5px;line-height:1.8;color:#3A3A33;margin-top:6px}}
.dates{{display:flex;gap:8px;overflow-x:auto;padding:2px 0 6px}}
.date{{flex:none;width:60px;text-align:center;border:1.5px solid #CFC9BC;border-radius:8px;padding:9px 0;background:#FBFAF7;cursor:pointer}}
.date.on{{border-color:var(--iron);background:var(--iron);color:#F4F1EA}}
.date .d1{{font-size:11px;font-weight:700}} .date .d2{{font-size:17px;font-weight:900;margin-top:2px}}
.slots{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}}
.slot{{text-align:center;border:1.5px solid #CFC9BC;border-radius:7px;padding:11px 0;font-size:14px;font-weight:800;background:#FBFAF7;cursor:pointer}}
.slot.on{{border-color:var(--green);background:var(--green);color:#fff}}
.slot.taken{{background:#E7E3DC;color:#B3AEA2;border-color:#DAD5C9;text-decoration:line-through;cursor:not-allowed}}
.field{{margin-top:14px}}
.field label{{font-size:13px;font-weight:800;display:block;margin-bottom:6px}}
.field input,.field textarea{{width:100%;border:1.5px solid #CFC9BC;border-radius:7px;padding:12px;font-size:15px;background:#FBFAF7;font-family:inherit}}
.pay{{border:1.5px solid #CFC9BC;border-radius:8px;padding:15px;margin-top:12px;cursor:pointer;display:flex;align-items:center;gap:12px;background:#FBFAF7}}
.pay.on{{border-color:var(--iron);box-shadow:0 0 0 2px var(--iron)}}
.pay .ic{{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:900;color:#fff}}
.pay .t{{flex:1}} .pay .t b{{font-size:15px;font-weight:900}} .pay .t small{{font-size:12px;color:#736E63;display:block;margin-top:2px}}
.bankbox{{background:#F2EFE7;border:1px dashed #B7B0A0;border-radius:8px;padding:14px;margin-top:12px;font-size:13.5px;line-height:1.9}}
.bankbox b{{font-weight:900}}
.note{{font-size:12px;color:#736E63;text-align:center;margin:16px;line-height:1.7}}
.donewrap{{text-align:center;padding:40px 24px 10px}}
.check{{width:74px;height:74px;border-radius:50%;background:var(--green);color:#fff;font-size:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 18px}}
.pwd{{font-size:34px;font-weight:900;letter-spacing:10px;color:var(--iron);background:#FBFAF7;border:2px solid var(--iron);border-radius:10px;padding:16px;margin:16px 0;text-align:center}}
.summary{{background:#FBFAF7;border:1.5px solid var(--iron);border-radius:8px;padding:14px 16px;margin:0 16px}}
.line{{display:flex;align-items:center;justify-content:center;gap:8px;background:#06C755;color:#fff;font-size:15px;font-weight:900;padding:14px;border-radius:8px}}
.linefab{{position:fixed;right:16px;bottom:92px;width:54px;height:54px;background:#06C755;border-radius:10px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(6,199,85,.4);color:#fff;font-size:12px;font-weight:900;z-index:30}}
.proto{{background:var(--gold);color:#241E12;text-align:center;font-size:11px;font-weight:800;padding:5px}}
"""
LINE_URL="https://lin.ee/VJ9huTD"
LEAF=f'<svg class="lf" viewBox="0 0 24 24" fill="{GOLD}"><path d="M12 2C8 6 5 9 5 14a7 7 0 0 0 14 0c0-5-3-8-7-12zm0 4.5c2.4 2.6 4 4.8 4 7.5a4 4 0 0 1-8 0c0-2.7 1.6-4.9 4-7.5z"/></svg>'

def head(title):
    return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">\n<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
<title>{title}・小憩 TAKE A BREATH</title><style>{CSS}</style></head><body>
<div class="proto">模擬版・假資料示意，可實際操作流程</div>'''

def topbar(back=None):
    left = f'<a class="back" href="{back}">‹ 返回</a>' if back else f'<div class="brand">{LEAF}<div><div class="bz">小憩</div><div class="en">TAKE A BREATH</div></div></div>'
    return f'<div class="topbar">{left}<div class="loc">台北・中山區</div></div>'

SPACES={
 "vip1":dict(nm="VIP 1・沙發床房",cap="2-4 人",price=300,c1="#9A8C76",c2="#6E6253",
   amen=["折疊沙發床","獨立門・隱私","WiFi","冷氣","儲物櫃","吧台共用"],
   desc="本店最大、唯一有獨立門的私密空間。放置灰橘色折疊沙發床（200×100），可坐可躺，適合諮詢、教學、雙人作業或想要更隱密的療程。"),
 "a":dict(nm="美容房 A",cap="1-2 人",price=200,c1="#A99272",c2="#7C654A",
   amen=["電動升降美容床","可升降・加熱","立燈","美容車","WiFi","冷熱水"],
   desc="黑鐵框＋白紗簾的工業風隔間，配置電動升降美容床（S 型升降・有加熱），立燈＋美容車齊全，做臉、霧眉、美睫、采妝都合適。"),
 "b":dict(nm="美容房 B",cap="1-2 人",price=200,c1="#5E6E48",c2="#3C4A2C",
   amen=["電動升降美容床","可升降・加熱","立燈","美容車","WiFi","冷氣"],
   desc="與美容房 A 同款配置的工業風獨立隔間，電動升降美容床（S 型升降・有加熱），安靜不互相干擾，適合單人接客。"),
}
TIERS=[("2 小時","NT$300"),("3 小時","NT$450"),("半日 5H","NT$700"),("全日 8H","NT$1000")]

# ---------- index ----------
cards=""
for sid,s in SPACES.items():
    chips="".join(f'<span class="chip">{a}</span>' for a in s["amen"][:4])
    cards+=f'''<a class="card" href="space.html?id={sid}">
      <div class="photo" style="background:linear-gradient(135deg,{s['c1']},{s['c2']})"><span class="cap">{s['cap']}</span><span class="phl">點我看詳情・照片</span></div>
      <div class="cbody"><div class="crow"><div class="cnm">{s['nm']}</div><div class="cprice">NT${s['price']}<span>/小時</span></div></div>
      <div class="cloc">台北・中山區　·　即時可訂</div><div class="chips">{chips}</div></div></a>'''
tiers="".join(f'<div class="card" style="margin:0;box-shadow:none;text-align:center;padding:14px 4px"><div style="font-size:12px;font-weight:700;color:#736E63">{n}</div><div style="font-size:15px;font-weight:900;color:{GREEN};margin-top:4px">{p}</div></div>' for n,p in TIERS)
index=head("時租美容空間")+topbar()+f'''
<div class="hero"><h1>美業人的<br>時租美容空間</h1><p>木質 × 森林綠 × 工業風的療癒場域<br>24H 線上預約・電子鎖自助進場</p></div>
<div class="sec"><div class="sect">可租空間</div>{cards}</div>
<div class="sec"><div class="sect">時數方案</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">{tiers}</div></div>
<div class="note">付款：LINE Pay・匯款（不收信用卡）<br>預約後 email／LINE 寄電子鎖密碼，開門自助進場</div>
<a class="linefab" href="{LINE_URL}">LINE</a></body></html>'''
open(f"{OUT}/index.html","w",encoding="utf-8").write(index)

# ---------- space detail ----------
space=head("空間詳情")+topbar(back="index.html")+f'''
<div id="app"></div>
<script>
const SP={{{",".join(f'"{k}":{{"nm":"{v["nm"]}","cap":"{v["cap"]}","price":{v["price"]},"c1":"{v["c1"]}","c2":"{v["c2"]}","amen":{v["amen"]},"desc":"{v["desc"]}"}}'.replace("'",'"') for k,v in SPACES.items())}}};
const id=new URLSearchParams(location.search).get("id")||"vip1";const s=SP[id];
const amen=s.amen.map(a=>`<span class="chip">${{a}}</span>`).join("");
document.getElementById("app").innerHTML=`
<div class="gallery" style="background:linear-gradient(135deg,${{s.c1}},${{s.c2}})">
  <div class="gcell">實景照 1</div><div class="gcell" style="background:rgba(0,0,0,.12)">實景照 2</div><div class="gcell">實景照 3</div></div>
<div class="sec" style="margin-top:16px"><div class="crow"><div class="cnm" style="font-size:21px">${{s.nm}}</div><div class="cprice" style="font-size:23px">NT$${{s.price}}<span>/小時</span></div></div>
<div class="cloc" style="margin-top:6px">台北・中山區　·　可容 ${{s.cap}}　·　即時可訂</div>
<div class="chips" style="margin-top:14px">${{amen}}</div>
<div class="desc" style="margin-top:16px">${{s.desc}}</div>
<div style="height:90px"></div></div>
<div class="fixbar"><a class="btn green" href="booking.html?id=${{id}}">選擇此空間・看時段</a></div>`;
</script>
<a class="linefab" href="{LINE_URL}">LINE</a></body></html>'''
open(f"{OUT}/space.html","w",encoding="utf-8").write(space)

# ---------- booking (date + slots) ----------
booking=head("選時段")+topbar(back="space.html")+f'''
<div class="sec"><div class="sect">選擇日期</div><div class="dates" id="dates"></div></div>
<div class="sec"><div class="sect">選擇時段（每格 1 小時）</div><div class="slots" id="slots"></div>
<div class="note" style="text-align:left;margin:12px 2px">灰色刪除線＝已被預約。連續點選多格＝租多小時。</div></div>
<div style="height:90px"></div>
<div class="fixbar"><a class="btn" id="next" style="opacity:.45;pointer-events:none">請先選時段</a></div>
<script>
const id=new URLSearchParams(location.search).get("id")||"vip1";
const dd=document.getElementById("dates");const wk=["日","一","二","三","四","五","六"];
const today=new Date();let selDate=0;
for(let i=0;i<7;i++){{const d=new Date(today.getTime()+i*864e5);
 const el=document.createElement("div");el.className="date"+(i==0?" on":"");
 el.innerHTML=`<div class="d1">${{i==0?"今天":"週"+wk[d.getDay()]}}</div><div class="d2">${{d.getDate()}}</div>`;
 el.onclick=()=>{{document.querySelectorAll(".date").forEach(x=>x.classList.remove("on"));el.classList.add("on");selDate=i;render();}};dd.appendChild(el);}}
const taken={{0:["11:00","14:00","15:00","19:00"],1:["10:00","13:00"],2:["16:00","17:00","18:00"]}};
let sel=[];
function render(){{sel=[];upd();const g=document.getElementById("slots");g.innerHTML="";
 for(let h=9;h<=21;h++){{const t=(h<10?"0":"")+h+":00";const tk=(taken[selDate]||[]).includes(t);
  const el=document.createElement("div");el.className="slot"+(tk?" taken":"");el.textContent=t;
  if(!tk)el.onclick=()=>{{el.classList.toggle("on");const i=sel.indexOf(t);i>=0?sel.splice(i,1):sel.push(t);upd();}};g.appendChild(el);}}}}
function upd(){{const n=document.getElementById("next");if(sel.length){{sel.sort();n.style.opacity=1;n.style.pointerEvents="auto";
  n.textContent=`已選 ${{sel.length}} 小時・下一步`;n.href=`info.html?id=${{id}}&n=${{sel.length}}&t=${{sel[0]}}`;}}else{{n.style.opacity=.45;n.style.pointerEvents="none";n.textContent="請先選時段";}}}}
render();
</script>
<a class="linefab" href="{LINE_URL}">LINE</a></body></html>'''
open(f"{OUT}/booking.html","w",encoding="utf-8").write(booking)

# ---------- info form ----------
info=head("填寫資料")+topbar(back="booking.html")+f'''
<div class="sec"><div class="sect">預約資料</div>
<div class="field"><label>姓名 / 暱稱</label><input id="nm" placeholder="例：Amy 美睫"></div>
<div class="field"><label>手機</label><input id="ph" placeholder="09xx-xxx-xxx" inputmode="tel"></div>
<div class="field"><label>服務項目（選填）</label><input id="sv" placeholder="例：美睫 / 霧眉 / 做臉"></div>
<div class="field"><label>備註（選填）</label><textarea id="rm" rows="2" placeholder="想先說的事…"></textarea></div>
<div style="height:90px"></div></div>
<div class="fixbar"><a class="btn green" id="go">下一步・付款</a></div>
<script>const q=location.search;document.getElementById("go").href="pay.html"+q;</script>
<a class="linefab" href="{LINE_URL}">LINE</a></body></html>'''
open(f"{OUT}/info.html","w",encoding="utf-8").write(info)

# ---------- payment ----------
pay=head("付款")+topbar(back="info.html")+f'''
<div class="summary" style="margin-top:16px"><div class="kv"><span>空間</span><b id="sp">美容房 A</b></div>
<div class="kv"><span>時段</span><b id="tm">今天 14:00 起</b></div>
<div class="kv"><span>時數</span><b id="hr">2 小時</b></div>
<div class="kv" style="border:0"><span>應付總額</span><span class="g" id="amt">NT$400</span></div></div>
<div class="sec"><div class="sect">選擇付款方式</div>
<div class="pay on" id="p1" onclick="pick('p1')"><div class="ic" style="background:#06C755">LINE</div><div class="t"><b>LINE Pay</b><small>線上即時付款</small></div><div id="r1">●</div></div>
<div class="pay" id="p2" onclick="pick('p2')"><div class="ic" style="background:var(--iron)">匯款</div><div class="t"><b>銀行匯款 / ATM 轉帳</b><small>轉帳後回填末五碼</small></div><div id="r2"></div></div>
<div class="bankbox" id="bank" style="display:none"><b>（範例）國泰世華 013</b><br>帳號：<b>1234-5678-9012</b><br>戶名：<b>小憩工作室</b><br>轉好回填末五碼或上傳收據，老闆確認後放行電子鎖密碼。</div>
<div style="height:90px"></div></div>
<div class="fixbar"><a class="btn gold" href="done.html">確認・送出預約</a></div>
<script>
const p=new URLSearchParams(location.search);const id=p.get("id")||"a";const n=+(p.get("n")||2);const t=p.get("t")||"14:00";
const NM={{vip1:"VIP 1・沙發床房",a:"美容房 A",b:"美容房 B"}};const PR={{vip1:300,a:200,b:200}};
sp.textContent=NM[id];tm.textContent="今天 "+t+" 起";hr.textContent=n+" 小時";amt.textContent="NT$"+(PR[id]*n);
function pick(x){{p1.classList.toggle("on",x=="p1");p2.classList.toggle("on",x=="p2");r1.textContent=x=="p1"?"●":"";r2.textContent=x=="p2"?"●":"";bank.style.display=x=="p2"?"block":"none";}}
</script>
<a class="linefab" href="{LINE_URL}">LINE</a></body></html>'''
open(f"{OUT}/pay.html","w",encoding="utf-8").write(pay)

# ---------- done ----------
done=head("預約完成")+topbar()+f'''
<div class="donewrap"><div class="check">✓</div><div style="font-size:22px;font-weight:900">預約成功！</div>
<div style="font-size:13.5px;color:#736E63;margin-top:8px;line-height:1.7">電子鎖密碼已產生<br>（正式版會在報到前 20 分鐘 email／LINE 寄給你）</div>
<div class="pwd">8&nbsp;3&nbsp;4&nbsp;7</div>
<div style="font-size:12px;color:#736E63">到場輸入此密碼開門，自助進場</div></div>
<div class="summary" style="margin-top:6px"><div class="kv"><span>空間</span><b>美容房 A</b></div>
<div class="kv"><span>時段</span><b>今天 14:00–16:00</b></div>
<div class="kv" style="border:0"><span>金額</span><span class="g">NT$400・LINE Pay 已付</span></div></div>
<div class="sec"><a class="line" href="{LINE_URL}">有問題？加 LINE 直接問我們</a>
<a class="btn" href="index.html" style="margin-top:12px;background:#fff;color:var(--iron);border:1.5px solid var(--iron)">回首頁</a></div>
<div class="note">這是模擬完成頁。正式版：匯款者付款待你後台確認後才放行密碼。</div>
</body></html>'''
open(f"{OUT}/done.html","w",encoding="utf-8").write(done)

print("built:", os.listdir(OUT))
