$(function(){
    $("#data").DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      deferRender: true,
      ajax: {
        url: window.location.pathnam,
        type: "POST",
        data: { action: "searchdata" }, // parametros
        dataSrc: "",
      },
      columns: [
        { data: "id" },
        { data: "servicio.nombre" },
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
      initComplete: function (settings, json) {},
    });
})