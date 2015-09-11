//Ajusta el tamaño de un iframe al de su contenido interior para evitar scroll
function autofitIframe(id){
    if (!window.opera && document.all && document.getElementById){
        id.style.height=id.contentWindow.document.body.scrollHeight;
    } else if(document.getElementById) {
        id.style.height=id.contentDocument.body.scrollHeight+"px";
    }
}
window.onload=cerrar;
function cerrar(){
    $("#cargar").animate({"opacity":"0"},1000,function(){$("#cargar").css("display","none");});
}
$("#carga").click(function(){cerrar();});
$(".botonmodalEliminar").on('click',function(evento){
    evento.preventDefault();
    var opcion = $(this).data('opcion');
    var numero = $(this).data('numero');
    $('.id_opcionEliminar').attr('src', opcion);
    $('.id_opcionEliminar').attr('id', numero);
});
$(".botonmodalServicio").on('click',function(evento){
    evento.preventDefault();
    var opcion = $(this).data('opcion');
    var name = $(this).data('name');
    $('.id_opcionServicio').attr('src', opcion);
    $('#name-mueble').text(name);
});
$(".botonmodalDireccion").on('click',function(ev){
    ev.preventDefault();
    var numero = $(this).data('numero');
    var opcion = $(this).data('opcion');
    $('.id_opcionDireccion').attr('src', opcion);
    $('.id_opcionDireccion').attr('id', numero);
});
$(".botonmodalMueble").on('click',function(eve){
    eve.preventDefault();
    var numero = $(this).data('numero');
    var opcion = $(this).data('opcion');
    $('.id_opcionMueble').attr('src', opcion);
    $('.id_opcionMueble').attr('id', numero);
});
$(".botonmodalDatosPersonales").on('click',function(even){
    even.preventDefault();
    var numero = $(this).data('numero');
    var opcion = $(this).data('opcion');
    $('.id_opcionDatosPersonales').attr('src', opcion);
    $('.id_opcionDatosPersonales').attr('id', numero);
});
$(document).ready(function() {
    $(function () {
        $('[data-toggletooltip="tooltip"]').tooltip()
    })
    document.getElementById('id_body').setAttribute('data-spy','scroll');
    document.getElementById('id_body').setAttribute('data-target','#navbar-example');
    document.getElementById('id_body').setAttribute('data-offset','70');
    $(function(){
//clic en un enlace de la lista
$('.linknav a').on('click',function(e){
//prevenir en comportamiento predeterminado del enlace
e.preventDefault();
//obtenemos el id del elemento en el que debemos posicionarnos
var strAncla=$(this).attr('href');

//utilizamos body y html, ya que dependiendo del navegador uno u otro no funciona
$('body,html').stop(true,true).animate({
//realizamos la animacion hacia el ancla
//-126 indica que baja el scroll 126px que es la altura de la cabecera para que se coloque correctamente
scrollTop: $(strAncla).offset().top-70
},1000);
});
$('.modal-footer a').on('click',function(e){
//prevenir en comportamiento predeterminado del enlace
e.preventDefault();
//obtenemos el id del elemento en el que debemos posicionarnos
var strAncla=$(this).attr('href');

//utilizamos body y html, ya que dependiendo del navegador uno u otro no funciona
$('body,html').stop(true,true).animate({
//realizamos la animacion hacia el ancla
//-126 indica que baja el scroll 126px que es la altura de la cabecera para que se coloque correctamente
scrollTop: $(strAncla).offset().top-70
},1000);
});
});

});