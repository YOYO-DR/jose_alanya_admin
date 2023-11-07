document.addEventListener('DOMContentLoaded', function () {
  const section = document.querySelector(".section-formulario");
  const form = section.querySelector("form");
  
  form.addEventListener("submit", function (e) { 
    e.preventDefault();
    const data = new FormData(form);
    submit_with_ajax(
      window.location.pathname,
      "Encuesta",
      "¿Seguro que desea enviar la encuesta?",
      data,
      (data) => {
        form.remove();
        section.insertAdjacentHTML(
          "beforeend",
          `<div class="alert alert-success alert-dismissible">
            <h5><i class="icon fas fa-check"></i>¡Encuesta enviada!</h5>
          </div>
        `
        );
      }
    );
  });
})