$(function () {
  const data_table = $("#data").DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "searchdata",
      },
      dataSrc: "",
    },
    columns: [
      { data: "id" },
      { data: "nombre" },
      { data: "descripcion" },
      { data: "precio" },
      { data: "categoria.nombre" },
      { data: "es_activo" },
      { data: "empresa.nombre" },
      { data: "sede.nombre" },
      { data: "id" },
    ],
    columnDefs: [
      {
        targets: [-6],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return "$" + parseFloat(data).toFixed(2);
        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          var buttons =
            '<a href="/crm/producto/update/' +
            row.id +
            '/" class="btn btn-primary btn-s btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons +=
            '<a href="/crm/producto/delete/' +
            row.id +
            '/" type="button" class="btn btn-danger btn-s btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {},
  });
});
