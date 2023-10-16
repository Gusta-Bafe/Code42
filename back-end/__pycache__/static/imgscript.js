
document.addEventListener("DOMContentLoaded", function () {
    // Captura todos os links com a classe "conteudo"
    const links = document.querySelectorAll('.conteudo');

    // Adiciona um evento de clique a cada link
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();

            // Obtém o valor do atributo "data-image" da div clicada
            const imageName = this.getAttribute('data-image');
            

            // Constrói o caminho da imagem com base no nome
            const imagePath = `/static/videos/${imageName}`;

            // Atualiza a imagem exibida
            const rpgImage = document.getElementById('rpgImage');
            rpgImage.src = imagePath;
        });
    });
});
