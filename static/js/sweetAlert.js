
const shareBtn = document.getElementById("share-btn");
shareBtn.addEventListener("click", () => {
// Obtenemos la URL actual de la página
const currentUrl = window.location.href;
// Creamos un elemento de tipo input
const inputElement = document.createElement("input");

// Agregamos la URL actual como valor del input
inputElement.value = currentUrl;

// Agregamos el input al DOM
document.body.appendChild(inputElement);

// Seleccionamos el texto del input
inputElement.select();

// Copiamos el texto seleccionado al portapapeles
document.execCommand("copy");

// Removemos el input del DOM
document.body.removeChild(inputElement);

// Creamos y mostramos la alerta personalizada
const alertElement = document.createElement("div");
Swal.fire({
    position: 'center',
    icon: 'success',
    title: '¡Enlace copiado!',
    showConfirmButton: false,
    timer: 2000
});
document.body.appendChild(alertElement);
setTimeout(() => document.body.removeChild(alertElement), 2000);
});