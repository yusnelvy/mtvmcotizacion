$('input[name=lista_ocupacion]').click(function() {
  radioColorBlue('lista_ocupacion');
});

radioColorBlue('lista_ocupacion');

$('input[name=lista_tamano]').click(function() {
  radioColorBlue('lista_tamano');
});

radioColorBlue('lista_tamano');

$('input[name=descripcion_densidadcontenido]').click(function() {
  radioColorBlue('descripcion_densidadcontenido');
});

radioColorBlue('descripcion_densidadcontenido');

$('input[name="trasladable"]').bootstrapSwitch();

function inputContenido(funcion) {
    if (funcion == 'ocultar'){
      $('p:has(select[id=id_descripcion_densidadcontenido])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(input[id=id_densidadcontenido])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(button[id=btn-calcularcontenedor])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(input[id=id_volumen_contenido])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(select[id=id_descripcion_contenedor])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p[id=msjcontenedor]').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('#id_descripcion_densidadcontenido').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(label[for=id_descripcion_densidadcontenido_0])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('p:has(label[for=id_descripcion_contenido])').fadeOut( 200, function() {
        $(this).css('display', 'none');
    });

    $('label[for=id_descripcion_densidadcontenido_1]').click();
      radioColorBlue('descripcion_densidadcontenido');
    }

    if (funcion == 'mostrar'){
    $('p:has(select[id=id_descripcion_densidadcontenido])').fadeIn(200);
    $('p:has(button[id=btn-calcularcontenedor])').fadeIn(200);
    $('p:has(input[id=id_densidadcontenido])').fadeIn(200);
    $('p:has(input[id=id_volumen_contenido])').fadeIn(200);
    $('p:has(select[id=id_descripcion_contenedor])').fadeIn(200);
    $('p[id=msjcontenedor]').fadeIn(200);
    $('#id_descripcion_densidadcontenido').fadeIn(200);
    $('p:has(label[for=id_descripcion_densidadcontenido_0])').fadeIn(200);
    $('p:has(label[for=id_descripcion_contenido])').fadeIn(200);
    }

  }

$('p:has(select[id=id_presupuesto])').css('display', 'none');
$('p:has(input[id=id_ambiente])').css('display', 'none');
$('p:has(input[id=id_mueble])').css('display', 'none');
$('p:has(input[id=id_tamano])').css('display', 'none');
$('p:has(input[id=id_ocupacidad])').css('display', 'none');
$('p:has(input[id=id_valor_ocupacidad])').css('display', 'none');
$('p:has(input[id=id_cantidad_contenedor])').css('display', 'none');
//$('p:has(input[id=id_volumen_contenido])').css('display', 'none');
$('p:has(input[id=id_volumen_contenedor])').css('display', 'none');
$('p:has(input[id=id_volumen_mueble])').css('display', 'none');
$('p:has(input[id=id_capacidad_peso_contenedor])').css('display', 'none');
$('p:has(input[id=id_capacidad_volumen_contenedor])').css('display', 'none');
$('p:has(input[id=id_peso_contenido])').css('display', 'none');
$('p:has(input[id=id_descripcion_contenedor])').css('display', 'none');
$('p:has(input[id=id_peso_contenedor])').css('display', 'none');
$('input[id=capacidadmueble]').css('display', 'none');
$('input[id=densidadcontenido]').css('display', 'none');
$('input[id=volmaterial]').css('display', 'none');
$('input[id=pesomaterial]').css('display', 'none');
$('#id_lista_ocupacion').addClass('radioselect-ul');
$('#id_lista_tamano').addClass('radioselect-ul');
$('#id_descripcion_densidadcontenido').addClass('radioselect-ul');


$('input[name="lista_tamano"]').focus(function() {
  $('li:has(input[name="lista_tamano"])').attr('class', 'focusBlue');
  var v = $(this);
  var p = v.position();
  scrollWin(p.top);
});
$('input[name="lista_tamano"]').focusout(function() {
  $('li:has(input[name="lista_tamano"])').removeClass('focusBlue');
});

$('input[name="lista_ocupacion"]').focus(function() {
  $('li:has(input[name="lista_ocupacion"])').attr('class', 'focusBlue');
});
$('input[name="lista_ocupacion"]').focusout(function() {
  $('li:has(input[name="lista_ocupacion"])').removeClass('focusBlue');
});

$('input[name="descripcion_densidadcontenido"]').focus(function() {
  $('li:has(input[name="descripcion_densidadcontenido"])').attr('class', 'focusBlue');
});
$('input[name="descripcion_densidadcontenido"]').focusout(function() {
  $('li:has(input[name="descripcion_densidadcontenido"])').removeClass('focusBlue');
});

function l_mueble() {
  $('#id_lista_mueble').zelect( {
    placeholder:'Seleccione el mueble'
  });
}
function l_ambiente() {
  $('#id_lista_ambiente').zelect( {
    placeholder:'Seleccione el ambiente'
  });
}
