document.addEventListener('DOMContentLoaded', function() {
    const usuarioId = 1;  // Aquí puedes obtener dinámicamente el ID del usuario
    const url = `/recomendaciones/${usuarioId}`;
    
    fetch(url)
    .then(response => response.json())
    .then(data => {
        const recommendationsList = document.getElementById('recommendations-list');
        recommendationsList.innerHTML = '';
        
        data.forEach(recommendation => {
            const recommendationDiv = document.createElement('div');
            recommendationDiv.classList.add('recommendation');
            
            recommendationDiv.innerHTML = `
                <h3>${recommendation.nombre}</h3>
                <p class="price">$${recommendation.precio}</p>
            `;
            recommendationsList.appendChild(recommendationDiv);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
