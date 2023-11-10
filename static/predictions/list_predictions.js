$(function(){
   $("#data").DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      deferRender: true,

      columns: [
        { data: "index" },
        { data: "date" },
        { data: "name_high" },
        { data: "name_less_low" },
        { data: "name_less_high" },
        // { data: "id" },
      ],
      initComplete: function (settings, json) {},
    });

})
