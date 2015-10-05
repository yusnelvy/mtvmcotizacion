//Ajusta el tamaño de un iframe al de su contenido interior para evitar scroll
function autofitIframe (id) {
    alert(id);
    if (!window.opera && document.all && document.getElementById) {
        id.style.height = id.contentWindow.document.body.scrollHeight;
    } else if(document.getElementById) {
        id.style.height = id.contentDocument.body.scrollHeight + "px";
    }
}

$(".resumenPresupuesto").on('click', function(evento2) {
    evento2.preventDefault();
    var opcion = $(this).data('opcion');
    $('#msjGuardado').css('width', '300px');
    $('#msjGuardado').fadeIn();
    $('#msjGuardado').text('Cargando resumen del presupuesto');
    setTimeout(function() {
        window.location = opcion;
    }, 500);
});

$(".botonmodalFormulario").on('click', function(even) {
    even.preventDefault();
    var opcion = $(this).data('opcion');
    var numero = $(this).data('numero');
    var nombre = $(this).data('nombre');
    $('.id_opcionFormulario').attr('src', opcion);
    $('.id_opcionFormulario').attr('id', numero);
    $('.nombreTitulo').text(nombre);
});

$(document).ready(function() {
    $(function () {
        $('[data-toggletooltip="tooltip"]').tooltip();
    });
    document.getElementById('id_body').setAttribute('data-spy', 'scroll');
    document.getElementById('id_body').setAttribute('data-target', '#navbar-example');
    document.getElementById('id_body').setAttribute('data-offset', '90');
    $(function() {
        //clic en un enlace de la lista
        $('.scrollSpy').on('click', function(e) {
            e.preventDefault();
            //obtenemos el id del elemento en el que debemos posicionarnos
            var strAncla = $(this).attr('href');
            //utilizamos body y html, ya que dependiendo del navegador uno u otro no funciona
            $('body,html').stop(true, true).animate( {
                //realizamos la animacion hacia el ancla
                //-126 indica que baja el scroll 126px que es la altura de la cabecera
                //para que se coloque correctamente
                scrollTop: $(strAncla).offset().top - 60
            }, 1000);
        });

        $(".botonOrden").on('click', function() {
            var numero = $(this).data('numero');
            var action = $(this).data('opcion');
            $.ajax( {
                url: action,
                type: 'GET',
                data: numero,
                success: function(data) {
                    if (data.estatus == "ok") {
                        setTimeout(function() {
                            parent.location.reload();
                        }, 1000);
                    } else {
                        alert('Ocurrio un error ' + data.estatus);
                    }
                },
                error: function (ajaxContext) {
                    alert('No se puede cambiar el orden.');
                }
            });
            return false;
        });
    });
});
