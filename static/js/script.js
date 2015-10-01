$(function () {
  $('[data-toggletooltip="tooltip"]').tooltip();
})
function justNumbers(e) {
  var keynum = window.event ? window.event.keyCode : e.which;
  if ((keynum == 8) || (keynum == 43) || (keynum == 45))
    return true;

  return /\d/.test(String.fromCharCode(keynum));
}

function cerrarModal(btn, msj ) {
  $(btn).click();
  $(msj).text('Acción cancelada');
  $(msj).fadeIn();
  setTimeout(function () {
    $(msj).fadeOut();
  }, 2000);
}

function cerrarEliminar() {
  var closep = parent.document.getElementById("cerrarEliminar");
  var msj = parent.document.getElementById('msjEliminado');
  $(closep).click();
  $(msj).text('Acción cancelada');
  $(msj).fadeIn();
  setTimeout(function () {
    $(msj).fadeOut();
  }, 2000);
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
