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
    title: '¡Vínculo copiado!',
    width: 350,
    padding: '1.5em',
    color: '#716add',
    background: '#fff url(/images/trees.png)',
    backdrop: `
      rgba(0,0,123,0.4)
      url("/static/loli-dance.gif")
      left top
      no-repeat
    `
  });
document.body.appendChild(alertElement);
setTimeout(() => document.body.removeChild(alertElement), 2000);
});