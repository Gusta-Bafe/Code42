document.getElementById('arquivo').addEventListener('change', function(event) {
    const capaPreview = document.getElementById('capa-preview');
    const file = event.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            capaPreview.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});
