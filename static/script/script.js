function App() {}

window.onload = function(event) {
    let app = new App();
    window.app = app;

    // Asegúrate de añadir los eventos a los botones al cargar
    const prevButton = document.getElementById('button-prev');
    const nextButton = document.getElementById('button-next');

    if (prevButton) prevButton.addEventListener('click', app.processingButton.bind(app));
    if (nextButton) nextButton.addEventListener('click', app.processingButton.bind(app));
}

App.prototype.processingButton = function(event) {
    const btn = event.currentTarget;
    const carruselList = btn.parentNode;
    const track = carruselList.querySelector('#track');
    const carruseles = track.querySelectorAll('.carrusel');
    const carruselWidth = carruseles[0].offsetWidth;

    const trackWidth = track.scrollWidth; // Total width of all items
    const listWidth = carruselList.offsetWidth; // Width of the visible area
    let leftPosition = parseFloat(track.style.transform.replace('translateX(', '').replace('px)', '')) || 0;

    if (btn.dataset.button === 'button-prev') {
        this.prevAction(leftPosition, carruselWidth, track, trackWidth, listWidth);
    } else {
        this.nextAction(leftPosition, carruselWidth, track, trackWidth, listWidth);
    }
}

App.prototype.prevAction = function(leftPosition, carruselWidth, track, trackWidth, listWidth) {
    if (leftPosition < 0) {
        const newLeft = Math.min(leftPosition + carruselWidth, 0);
        track.style.transform = `translateX(${newLeft}px)`;
    }
}

App.prototype.nextAction = function(leftPosition, carruselWidth, track, trackWidth, listWidth) {
    if (-leftPosition < (trackWidth - listWidth)) {
        const newLeft = Math.max(leftPosition - carruselWidth, -(trackWidth - listWidth));
        track.style.transform = `translateX(${newLeft}px)`;
    }
}

const peliculasLink = document.querySelector('.nav_list li:nth-child(1)'); // Selecciona el enlace "Películas"
    
    peliculasLink.addEventListener('mouseenter', () => {
        peliculasLink.classList.add('active'); // Agrega la clase cuando el mouse entra
    });

    peliculasLink.addEventListener('mouseleave', () => {
        peliculasLink.classList.remove('active'); // Remueve la clase cuando el mouse sale
    });


