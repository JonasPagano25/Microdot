// Pido los datos cada segundo
setInterval(() => {
    // Pido los datos a la ruta /data/update
    fetch("/data/update")
    .then(response => response.json())
    .then(data => {
        // Guardo el valor de temperatura
        const lightper = data.lightper;
        // Maximo valor de temperatura
        const max_lightper = 100;
        // Lo escalo a un valor entre -30 y 240 grados
        const deg = lightper * 300 / max_lightper - 30;
        // Lo cambio en la aguja
        document.querySelector(".gauge .pointer .hand").style.transform = `rotate(${deg}deg)`;
        console.log(lightper);
    })
    
}, 200);
