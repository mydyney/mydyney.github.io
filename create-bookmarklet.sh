#!/bin/bash
# 한 줄로 압축된 북마클릿 생성

echo "javascript:(function(){const s=['.se-main-container','#postViewArea','.se-component-content','#viewTypeSelector'];let c=null;for(let sel of s){c=document.querySelector(sel);if(c)break;}if(!c){alert('블로그 본문을 찾을 수 없습니다.');return;}const h=c.outerHTML;const b=new Blob([h],{type:'text/html;charset=utf-8'});const u=URL.createObjectURL(b);const a=document.createElement('a');a.href=u;a.download='naver.md';document.body.appendChild(a);a.click();document.body.removeChild(a);URL.revokeObjectURL(u);alert('✅ naver.md 다운로드 완료!');})();"
