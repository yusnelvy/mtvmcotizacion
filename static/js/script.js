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

 /*ayuda*/

$(document).ready(main);

var contador = 1;

function main(){
    $('.ayuda_btn').click(function(){
        // $('nav').toggle();

        if(contador == 1){
            $('.ayuda').animate({
                right: '1%'
            });
            contador = 0;
        } else {
            contador = 1;
            $('.ayuda').animate({
                right: '-100%'
            });
        }

    });
            $('#page-wrap').click(function(){
        // $('nav').toggle();

        if(contador == 0){

            $('.ayuda').animate({
                right: '-100%'
            });
            contador = 1;
        }

    });
          $('#footer').click(function(){
        // $('nav').toggle();

        if(contador == 0){

            $('.ayuda').animate({
                right: '-100%'
            });
            contador = 1;
        }

    });

};

/*Eliminar*/

// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id

// Fin de configuraciones
    $(document).on('ready',function(){
        $(".delete").on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_id').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response){

                    if(response.status=="True"){
                        alert("Eliminado!");
                        var id = response.item_id;
                        var elementos= $(nombre_tabla +' >tbody >tr').length;
                        var count_reg = $("#count_reg").text();

                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+id).remove();
                            $("#myModal").modal('hide');
                            parseInt
                            $('#count_reg').text(count_reg-1);

                        }

                    }else{
                        alert("Hubo un error al eliminar! " + response.msj);
                        $("#myModal").modal('hide');
                    }


                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
    });

/*Ajax*/


function objetoAjax(){
        var xmlhttp=false;
        try{
            xmlHttp=new XMLHttpRequest(); // Firefox, Opera 8.0+, Safari
        } catch (e){
            try {
                xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                try {
                   xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (E) {
                        xmlhttp = false;
                }
            }
        }

        if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
                xmlhttp = new XMLHttpRequest();
        }
        return xmlhttp;
}

function eliminar(Pag,idEliminar,descripc) {

    var agree=confirm('Desea eliminar el registro: ' + descripc + '?');
    if (agree){
        ajax=objetoAjax();
        ajax.open("GET",Pag,true);
        ajax.onreadystatechange=function() {
                if (ajax.readyState==4) {
                    $('#tr'+idEliminar).remove();
                }
        }
        ajax.send(null)
    }
}


/*bootstrapSwitch para los form*/

function Switchbootstrap(name) {
  if ($('input[name="' + name + '"]').attr('checked') === 'checked'){
    $('input[name="' + name + '"]').bootstrapSwitch('state', true);
  }else{
    $('input[name="' + name + '"]').bootstrapSwitch('state', false);
  }
}

Switchbootstrap('activo');
Switchbootstrap('trasladable');
Switchbootstrap('apilable');
Switchbootstrap('capacidad_carga');
Switchbootstrap('capacidad_interna');
Switchbootstrap('predefinido');
Switchbootstrap('rampa');
Switchbootstrap('ascensor');
Switchbootstrap('ascensor_servicio');
Switchbootstrap('recuperable');
Switchbootstrap('contenedor');

