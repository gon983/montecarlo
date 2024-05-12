async function simule(){
    const selectorProductos = document.getElementById("selectorProductos")
    const divRta = document.getElementById("divRta")
    if(selectorProductos){
        nProducto = selectorProductos.value
    }

    const res = await fetch(`http://localhost:8081/${nProducto}`)
    const datos = await res.json()
    console.log(datos)
    divRta.innerHTML = datos
    
}

