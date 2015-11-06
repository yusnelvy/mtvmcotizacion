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

function scrollWin(top) {
    window.scrollTo(0, top - 200);
}

$(".botonmodalEliminar").on('click', function(evento) {
  evento.preventDefault();
  var opcion = $(this).data('opcion');
  var numero = $(this).data('numero');
  var nombre = $(this).data('nombre');
  var boton = $(this).data('boton');
  var ask = $(this).data('ask');
  $('.askEliminar').text(ask);
  $('.id_opcionEliminar').attr('src', opcion);
  $('.id_opcionEliminar').attr('id', numero);
  $('.nombreEliminar').text(nombre);
  $('#boton').val(boton);

});

$('#btn-cancelarEliminar').click(function() {
  cerrarModal(document.getElementById('cerrarEliminar'),
    document.getElementById('msjEliminado')
    );
});

$(".botonmodalAnular").on('click', function(evento) {
  evento.preventDefault();
  var opcion = $(this).data('opcion');
  var numero = $(this).data('numero');
  var nombre = $(this).data('nombre');
  var boton = $(this).data('boton');
  var ask = $(this).data('ask');
  $('.askEliminar').text(ask);
  $('.id_opcionEliminar').attr('src', opcion);
  $('.id_opcionEliminar').attr('id', numero);
  $('.nombreEliminar').text(nombre);
  $('#boton').val(boton);

});

function disabledBtn(boton) {
    $(boton).attr('disabled', 'disabled');
    setTimeout(function() {
            $(boton).removeAttr('disabled', 'disabled');
          }, 4000);
}

function radioColorBlue (name) {
  $("label:has(input[name=" + name + "])").css("background-color", "#fff");
  $("label:has(input[name=" + name + "])").css("color", "#777");
  $("label:has(input[name=" + name + "]:checked)").css("background-color", "#337ab7");
  $("label:has(input[name=" + name + "]:checked)").css("color", "#fff");
}

function enterNone() {
  $('#myform').keypress(function(e){
    if(e == 13){
      return false;
    }
  });

  $('input').keypress(function(e){
    if(e.which == 13){
      return false;
    }
  });

  $('li').keypress(function(e){
    if(e.which == 13){
      return false;
    }
  });
}

$('.eliminar').on('hidden.bs.modal', function () {
    setTimeout(function() {
        $('.id_opcionEliminar').attr('src', '');
        $('.id_opcionEliminar').attr('height', '80');
        $('#search').focus();
    }, 600);
});
var cont = 1;
 $(".menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $(".navbarPrincipal").toggleClass("toggled");

        //$(".navbarPrincipal").css('margin-left', '0');

         if(cont == 1){

            cont = 0;
            $('#menuSidebar').css('display', 'block');
        } else {
            cont = 1;

            $('#menuSidebar').css('display', 'none');
        }
    });
