const http=require('http'), fs=require('fs'), path=require('path');
const root=path.resolve(__dirname,'..'), port=8781;
const MT={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'};
http.createServer((req,res)=>{
  let p=decodeURIComponent(req.url.split('?')[0]);
  if(p==='/') p='/index.html';
  const f=path.join(root,p);
  if(!f.startsWith(root)||!fs.existsSync(f)||fs.statSync(f).isDirectory()){res.writeHead(404);return res.end('not found');}
  res.writeHead(200,{'Content-Type':MT[path.extname(f)]||'application/octet-stream','Cache-Control':'no-store, max-age=0'});
  fs.createReadStream(f).pipe(res);
}).listen(port,()=>console.log('serving '+root+' on http://localhost:'+port));
