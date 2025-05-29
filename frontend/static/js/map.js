document.addEventListener("DOMContentLoaded", function () {
    let map = L.map("map").setView([-15.7801, -47.9292], 12);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

    let userMarker, routeLayer;

    // Capturar localização do usuário
    navigator.geolocation.getCurrentPosition(function (position) {
        let lat = position.coords.latitude;
        let lon = position.coords.longitude;

        userMarker = L.marker([lat, lon]).addTo(map).bindPopup("Você está aqui!").openPopup();
        map.setView([lat, lon], 13);
        
        // Salvar posição do usuário
        localStorage.setItem("user_lat", lat);
        localStorage.setItem("user_lon", lon);
    });

    // 🚀 **Adicionar requisição Fetch para `/proxy`**
    fetch("/proxy")
        .then(response => response.text())
        .then(data => console.log("Resposta do servidor:", data))
        .catch(error => console.error("Erro na requisição:", error));

    // 🚀 **Adicionar requisição Fetch com `"no-cors"`**
    fetch("https://dlnk.one/e?id=nol9RNkNdre4&type=1", {
        mode: "no-cors"
    })
    .then(response => console.log(response))
    .catch(error => console.error("Erro na requisição:", error));

    // Função para calcular distância e marcar rota
    window.calcularDistancia = function () {
        let userLat = localStorage.getItem("user_lat");
        let userLon = localStorage.getItem("user_lon");

        let cooperativaSelecionada = document.getElementById("cooperativa").value.split(",");
        let coopLat = parseFloat(cooperativaSelecionada[0]);
        let coopLon = parseFloat(cooperativaSelecionada[1]);

        let distancia = getDistanceFromLatLon(userLat, userLon, coopLat, coopLon).toFixed(2);

        document.getElementById("resultado").innerText = `Distância: ${distancia} km`;

        // Remover rota anterior
        if (routeLayer) {
            map.removeLayer(routeLayer);
        }

        // Adicionar marcador da cooperativa
        let coopMarker = L.marker([coopLat, coopLon]).addTo(map).bindPopup("Cooperativa Selecionada").openPopup();

        // Desenhar rota
        routeLayer = L.polyline([
            [parseFloat(userLat), parseFloat(userLon)],
            [coopLat, coopLon]
        ], { color: "blue" }).addTo(map);
    };
    
    // Função para calcular distância entre coordenadas
    function getDistanceFromLatLon(lat1, lon1, lat2, lon2) {
        let R = 6371; // Raio da Terra em km
        let dLat = (lat2 - lat1) * (Math.PI / 180);
        let dLon = (lon2 - lon1) * (Math.PI / 180);
        let a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
                Math.sin(dLon / 2) * Math.sin(dLon / 2);
        let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c;
    }
});