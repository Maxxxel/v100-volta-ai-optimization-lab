(function(root){
  'use strict';
  const finite=v=>typeof v==='number'&&Number.isFinite(v);
  const mean=(scores,selected)=>selected.length&&selected.every(k=>finite(scores[k]))?selected.reduce((sum,k)=>sum+scores[k],0)/selected.length:null;
  const compare=(a,b,descending=false)=>{
    const absent=v=>v===null||v===undefined||v==='';
    if(absent(a)||absent(b))return absent(a)===absent(b)?0:(absent(a)?1:-1);
    const c=finite(a)&&finite(b)?a-b:String(a).localeCompare(String(b),undefined,{numeric:true,sensitivity:'base'});
    return descending?-c:c;
  };
  const numeric=text=>{
    if(/^\s*(?:NOT MEASURED|NOT RECORDED|—)\s*$/i.test(text))return null;
    const pct=text.match(/(-?[\d.]+)\s*%/);if(pct)return Number(pct[1]);
    return /^\s*-?[\d,.]+\s*$/.test(text)?Number(text.trim().replace(/,/g,'')):text;
  };
  if(typeof module!=='undefined'&&module.exports){module.exports={mean,compare,numeric};return;}
  const el=(name,text)=>{const e=document.createElement(name);if(text!==undefined)e.textContent=text;return e;};
  function sortable(table,grouped){
    if(table.dataset.sortable)return;table.dataset.sortable='true';table.classList.add('benchmark-sortable');
    const controls=el('div');controls.className='benchmark-controls';const search=el('input');search.type='search';search.placeholder='Filter model, tuning or engine';search.setAttribute('aria-label','Filter benchmark rows');controls.append(search);
    table.parentElement.insertBefore(controls,table);let group=null;
    if(grouped){group=el('select');group.setAttribute('aria-label','Filter benchmark cohort');group.append(el('option','All cohorts (sorted separately)'));group.firstChild.value='';[...new Set([...table.tBodies[0].rows].map(r=>r.cells[0].textContent))].forEach(k=>{let o=el('option',k);o.value=k;group.append(o);});controls.append(group);}
    const filter=()=>{const term=search.value.toLowerCase();[...table.tBodies[0].rows].forEach(r=>{r.hidden=!r.textContent.toLowerCase().includes(term)||(group&&group.value&&r.cells[0].textContent!==group.value);});};search.addEventListener('input',filter);if(group)group.addEventListener('change',filter);
    [...table.tHead.rows[0].cells].forEach((th,index)=>{const label=th.textContent;th.textContent='';const button=el('button',label+' ↕');button.type='button';button.className='benchmark-sort';th.append(button);let descending=null;button.addEventListener('click',()=>{descending=descending===null?!/rank|model|cohort/i.test(label):!descending;const rows=[...table.tBodies[0].rows];rows.sort((a,b)=>(grouped&&index!==0?compare(a.cells[0].textContent,b.cells[0].textContent):0)||compare(numeric(a.cells[index].textContent),numeric(b.cells[index].textContent),descending));rows.forEach(r=>table.tBodies[0].append(r));[...table.tHead.rows[0].cells].forEach(h=>h.removeAttribute('aria-sort'));th.setAttribute('aria-sort',descending?'descending':'ascending');button.textContent=label+(descending?' ↓':' ↑');});});
  }
  function modelTable(table,data){
    if(table.dataset.interactive)return;table.dataset.interactive='true';table.classList.add('benchmark-sortable');const target=document.getElementById('benchmark-selection');if(!target)return;
    const keys=['coding','tools','mbpp'],labels={coding:'HumanEval+164',tools:'BFCL v4 static100 subset',mbpp:'MBPP+223 admitted subset'};let selected=[...data.selected],sortColumn=4,descending=true;const chosen=new Map();
    const note=el('p','Mean = sum of selected percentages / number of selected benchmarks. All selected results are required. Profiles can differ between benchmarks; this is not one deployment configuration.');target.append(note);
    const controls=el('div');controls.className='benchmark-controls';target.append(controls);const inputs=[];
    keys.forEach(k=>{const label=el('label');const checkbox=el('input');checkbox.type='checkbox';checkbox.checked=selected.includes(k);label.append(checkbox,document.createTextNode(' '+labels[k]));controls.append(label);inputs.push([k,checkbox]);checkbox.addEventListener('change',()=>{selected=inputs.filter(x=>x[1].checked).map(x=>x[0]);render();});});
    const search=el('input');search.type='search';search.placeholder='Filter models';search.setAttribute('aria-label','Filter model overview');controls.append(search);search.addEventListener('input',render);
    const headers=[...table.tHead.rows[0].cells];headers.forEach((th,index)=>{const label=th.textContent;th.textContent='';const button=el('button',label+' ↕');button.type='button';button.className='benchmark-sort';th.append(button);button.addEventListener('click',()=>{descending=index===sortColumn?!descending:![0,6].includes(index);sortColumn=index;headers.forEach(h=>h.removeAttribute('aria-sort'));th.setAttribute('aria-sort',descending?'descending':'ascending');render();});});
    function render(){
      const rows=data.models.map(model=>{let scores={},runs={};keys.forEach(k=>{const available=data.records.filter(r=>r.model===model.id&&r.discipline===k).sort((a,b)=>Number(a.experiment.slice(1))-Number(b.experiment.slice(1)));const id=chosen.get(model.id+':'+k);runs[k]={available,record:available.find(r=>r.id===id)||available[available.length-1]};const r=runs[k].record;scores[k]=r?100*r.solved/r.tasks:null;});return {model,scores,runs,total:mean(scores,selected),coverage:selected.filter(k=>finite(scores[k])).length};});
      const ranked=rows.filter(r=>finite(r.total)).sort((a,b)=>b.total-a.total);let previous=null,rank=0;ranked.forEach((r,i)=>{if(r.total!==previous){rank=i+1;previous=r.total;}r.rank=rank;});
      const value=(r,index)=>index===0?r.model.name:index<=3?r.scores[keys[index-1]]:index===4?r.total:index===5?r.coverage:(r.rank||null);
      rows.sort((a,b)=>compare(value(a,sortColumn),value(b,sortColumn),descending));const body=table.tBodies[0];body.textContent='';
      rows.forEach(row=>{if(!row.model.name.toLowerCase().includes(search.value.toLowerCase()))return;const tr=el('tr');tr.append(el('td',row.model.name+' / '+row.model.quantization));keys.forEach(k=>{const td=el('td');const {available,record}=row.runs[k];if(!record){td.textContent='NOT MEASURED';}else{
        const a=el('a',record.solved+'/'+record.tasks+' ('+row.scores[k].toFixed(2)+'%) · '+record.experiment);a.href='../experiments/'+record.experiment+'/';td.append(a);
        if(record.warning){td.classList.add('benchmark-warning');td.title=record.warning;}
        if(available.length>1){const select=el('select');select.setAttribute('aria-label',row.model.name+' '+labels[k]+' measured configuration');available.forEach(r=>{const option=el('option',r.experiment+' · '+r.profile);option.value=r.id;option.selected=r.id===record.id;select.append(option);});select.addEventListener('change',()=>{chosen.set(row.model.id+':'+k,select.value);render();});td.append(select);}
        td.append(el('small',record.profile));}tr.append(td);});tr.append(el('td',finite(row.total)?row.total.toFixed(2)+'%':'NOT MEASURED'),el('td',row.coverage+'/'+selected.length),el('td',row.rank?String(row.rank):'—'));body.append(tr);});
    }
    render();
  }
  function init(){document.querySelectorAll('table').forEach(table=>{if(!table.tHead||!table.tBodies.length)return;const text=table.tHead.textContent;if(text.includes('Overall mean (%)')&&root.V100Comparison)modelTable(table,root.V100Comparison);else if(text.includes('Rank within cohort'))sortable(table,true);});}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})(typeof window==='undefined'?{}:window);
