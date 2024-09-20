onload = () => {
  document.body.classList.remove("container");
};

document.addEventListener('DOMContentLoaded', function() {
  const textoContainer = document.getElementById('texto-container');
  textoContainer.innerHTML = "Aunque nos conocemos<br> desde hace tiempo,<br>hay tanto por descubrir y <br>algo nuevo que explorar";
});

