$(function () {
  $('[data-toggletooltip="tooltip"]').tooltip();
});
function justNumbers(e) {
  var keynum = window.event ? window.event.keyCode : e.which;
  if ((keynum == 8) || (keynum == 43) || (keynum == 45))
    return true;

  return /\d/.test(String.fromCharCode(keynum));
}

function cerrarModal(btn, msj ) {
  $(btn).click();
}

function cerrarEliminar() {
  var closep = parent.document.getElementById("cerrarEliminar");
  $(closep).click();
}

$(".botonmodalEliminar").on('click', function(evento) {
  evento.preventDefault();
  var opcion = $(this).data('opcion');
  var numero = $(this).data('numero');
  var nombre = $(this).data('nombre');
  $('.id_opcionEliminar').attr('src', opcion);
  $('.id_opcionEliminar').attr('id', numero);
  $('.nombreEliminar').text(nombre);
});

$('#btn-cancelarEliminar').click(function() {
  cerrarModal(document.getElementById('cerrarEliminar'),
    document.getElementById('msjEliminado')
    );
});
