async function simule(){
    // const selectorProductos = document.getElementById("selectorProductos")
    const costoProducto = document.getElementById("costoProducto")
    const valorRecupero = document.getElementById("valorRecupero")
    const cantidadDias = document.getElementById("cantidadDias")
    const tamañoLote = document.getElementById("tamañoLote")
    const stockInicial = document.getElementById("stockInicial")
    const divRta = document.getElementById("divRta")
    
    // nProducto = selectorProductos.value



    const res = await fetch(`http://localhost:8081/${costoProducto.value}/${valorRecupero.value}/${cantidadDias.value}/${tamañoLote.value}/${stockInicial.value}`)
    const datos = await res.json()
    console.log(datos)
    divRta.innerHTML = datos
    
}


