/* Local development-screening view; never changes benchmark scores. */
(function () {
 function init() {
  const table=document.getElementById('screening-table'),input=document.getElementById('screening-search');
  if (!table || table.dataset.bound) return;
  table.dataset.bound='true';
  input.addEventListener('input',()=>{const q=input.value.toLowerCase();for(const row of table.tBodies[0].rows)row.hidden=!row.cells[0].textContent.toLowerCase().includes(q)&&!row.cells[1].textContent.toLowerCase().includes(q);});
  Array.from(table.tHead.rows[0].cells).forEach((th,index)=>{
   if(index>7)return;
   const button=document.createElement('button');button.type='button';button.textContent=th.textContent+' ↕';th.replaceChildren(button);
   button.addEventListener('click',()=>{
    const dir=button.dataset.dir==='desc'?'asc':'desc';button.dataset.dir=dir;
    const value=row=>{let s=row.cells[index].textContent.replaceAll(',','');if(s==='NOT MEASURED')return null;if(index>=2)return Number.parseFloat(s);return s.toLowerCase();};
    const rows=Array.from(table.tBodies[0].rows);rows.sort((a,b)=>{const av=value(a),bv=value(b);if(av===null)return bv===null?0:1;if(bv===null)return -1;return (typeof av==='number'?av-bv:av.localeCompare(bv))*(dir==='asc'?1:-1);});table.tBodies[0].append(...rows);
   });
  });
 }
 if(typeof document$!=='undefined')document$.subscribe(init);else if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
