//$(function () {
  //$('[data-toggle="tooltip"]').tooltip()
//})
function justNumbers(e)
{
var keynum = window.event ? window.event.keyCode : e.which;
if ((keynum == 8) || (keynum == 43) || (keynum == 45))
return true;

return /\d/.test(String.fromCharCode(keynum));
}
function cerrar (){
   var closep = parent.document.getElementById("btn-cerrarModal");
   var msj = parent.document.getElementById('msjEliminado');
   $(closep).click();
   $(msj).text('Acción cancelada');
   $(msj).fadeIn();
   setTimeout(function() {$(msj).fadeOut();}, 2000);
}
