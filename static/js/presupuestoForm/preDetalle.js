function radioColorOcupacion(){
  $("label:has(input[name=lista_ocupacion])").css("background-color", "#fff");
  $("label:has(input[name=lista_ocupacion])").css("color", "#777");
  $("label:has(input[name=lista_ocupacion]:checked)").css("background-color", "#08c");
  $("label:has(input[name=lista_ocupacion]:checked)").css("color", "#fff");
}
function radioColorTamano(){
  $("label:has(input[name=lista_tamano])").css("background-color", "#fff");
  $("label:has(input[name=lista_tamano])").css("color", "#777");
  $("label:has(input[name=lista_tamano]:checked)").css("background-color", "#08c");
  $("label:has(input[name=lista_tamano]:checked)").css("color", "#fff");
}
$(setup);

function setup() {
  $('#id_lista_mueble').zelect({ placeholder:'Seleccione el mueble' });
  $('#id_lista_ambiente').zelect({ placeholder:'Seleccione el ambiente' });
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
$('p:has(input[id=id_trasladable])').css('display', 'none');
$('input[id=capacidadmueble]').css('display', 'none');
$('input[id=densidadcontenido]').css('display', 'none');
$('input[id=volmaterial]').css('display', 'none');
$('input[id=pesomaterial]').css('display', 'none');
$('#id_lista_ocupacion li label').addClass('btn-radio');
$('#id_lista_tamano li label').addClass('btn-radio');
