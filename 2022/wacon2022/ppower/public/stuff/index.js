#!/usr/bin/env node
const express = require('express')
const childProcess = require('child_process')

const app = express()
const saved = Object.create(null)
const config = {}

const merge = function(t, src) {
    for(var v of Object.getOwnPropertyNames(src)) {
        if(typeof(src[v]) === 'object') {
        	if(!t[v]) t[v] = {}
            merge(t[v], src[v]);
        } else {
            t[v] = src[v];
        }
    }
    return t;
};

const sendFlag = (res)=>{
	try{
		// TODO: Fix the typo
		let flagggggggggggg = childProcess.execSync('/realreadflag',{
			env:Object.create(null),
			cwd:'/',
			timeout:1000
		})
		return res.send(flaggggggggggg) 
	} catch(e){console.log(e)}
	res.send("lol")
}

const recover = _=>{
	for(let v of Object.getOwnPropertyNames(Object.prototype)){
	    if(v in saved){
	    	Object.prototype[v] = saved[v]
	    } else {
	    	delete Object.prototype[v]
	    }
	}
}

app.get('/',(req,res)=>res.sendFile(`${process.cwd()}/index.html`))

app.get('/answer',(req,res)=>{
	//const payload = '{"answer":"Its-none-of-your-business","__proto__": {"flagForEveryone":true}}';
	let r = merge({},req.query);
	res.type('text/plain')

	if(r.answer == "Its-none-of-your-business"){
		if(!config.flagForEveryone){
			res.send(req.query);
			//res.send(':(').end()
		} else {
			sendFlag(res)
		}
	} else {
		res.send('oh ok').end()
	}

	recover()
})

;(function(){
	for(let v of Object.getOwnPropertyNames(Object.prototype)){
	    saved[v] = Object.prototype[v]
	}
	Object.freeze(saved)

	if(process.env.flagForEveryone){
		config.flagForEveryone = true
	}
})()

app.listen(8000)