$(function () {
  let tabla = $("#data").DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: { action: "searchdata" }, // parametros
      dataSrc: "",
    },
    columns: [
      { data: "id" },
      { data: "id" },
      { data: "fecha_servicio" },
      { data: "fecha_caducidad_servicio" },
      { data: "monto_descuento_servicio" },
      { data: "con_sin_igv_servicio" },
      { data: "sub_total_servicio" },
      { data: "total_impuesto_servicio" },
      { data: "total_servicio" },
      { data: "estado_servicio" },
      { data: "nota_admin_servicio" },
      { data: "nota_cliente_servicio" },
      { data: "terminos_condiciones_servicio" },
      { data: "monto_descuento_oficial" },
      { data: "sede.nombre" },
      { data: "id" },
    ],
    columnDefs: [
      {
        targets: [1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return `<button class="servi-modal btn btn-outline-primary">Servicios</button>`;
        },
      },
      {
        targets: [-7],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          if (data) {
            return "Activo";
          } else {
            return "Inactivo";
          }
        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          var buttons =
            '<a  href="/crm/presupuesto/update/' +
            row.id +
            '/" class="btn btn-primary btn-s btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons +=
            '<a href="/crm/presupuesto/delete/' +
            row.id +
            '/" type="button" class="btn btn-danger btn-s btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {
      $("#data").on("click", ".servi-modal", function (e) {
        //poner evento a los botones de la imagen de cada producto
        let fila = $(this).closest("tr, li");
        let data_fila = tabla.row(fila).data();
        console.log(data);
        //peticion servis
        $.ajax({
          url: window.location.pathname, //se la paso por la función
          type: "POST",
          data: { action: "searchservi", id: data_fila.id }, //se lo paso por la función
          dataType: "json",
        })
          .done(function (data) {
            if (!data.hasOwnProperty("error")) {
              console.log(data);
              let html = "";
              for (let i of data) {
              html += `<h2>${i.nombre}</h2>`;
              }
              html+=`<a href="/crm/servicio/list/">Lista servicios</a>`
              $("#modal-img .modal-title b").html(
                `<i class="far fa-info"></i> Servicios`
              );
              $("#modal-img .modal-body").html(
                html
              );
              $("#modal-img").modal("show");
              return false;
            }
            message_error(data.error);
          })
          .fail(function (jqXHR, textStatus, errorThrown) {
            //Este se ejecuta si la peticion tiene algun error
            alert(`${textStatus} : ${errorThrown}`);
          })
          .always(function () {
            //este se ejecuta siempre
          });
      });
    },
  });
});
