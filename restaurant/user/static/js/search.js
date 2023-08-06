function filterTable() {
    // Obtenemos el valor del campo de entrada
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
  
    // Obtenemos la tabla y sus filas
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
  
    // Recorremos todas las filas y ocultamos las que no coinciden con el filtro
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0]; // Columna a filtrar (en este caso, la primera)
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = ""; // Mostrar la fila si coincide con el filtro
        } else {
          tr[i].style.display = "none"; // Ocultar la fila si no coincide con el filtro
        }
      }
    }
  }