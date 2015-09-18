setTimeout(function () {
  $('label[for=id_direccion]').click();
}, 500);
$('#id_lista_tipoinmueble').click(function () {
  id_tipoinmueble = $('#id_lista_tipoinmueble').val();
  $.get('/presupuesto/direccion/nuevo',
    {id_tipoinmueble: id_tipoinmueble},
    function (data) {
      $("#id_tipo_inmueble").val(data[0].tipoinmueble);
    });
});
$("input[name=lista_ocupacion]").click(function () {
  id_ocupacion = $('input[name=lista_ocupacion]:checked').val();
  $.get('/presupuesto/direccion/nuevo',
    {id_ocupacion: id_ocupacion},
    function (data) {
      $("#id_ocupacidad_inmueble").val(data[0].ocupacion);
      $("#id_valor_ocupacidad").val(data[0].valorocupacion);
    });
});
$('input[name="rampa"]').bootstrapSwitch('state', false, true);
$('input[name="ascensor"]').bootstrapSwitch('state', false, true);
$('input[name="ascensor_servicio"]').bootstrapSwitch('state', false, true);
$('ul').attr('class', 'radioselect-ul');
function radioColorBlue (name) {
  $("label:has(input[name=" + name + "])").css("background-color", "#fff");
  $("label:has(input[name=" + name + "])").css("color", "#777");
  $("label:has(input[name=" + name + "]:checked)").css("background-color", "#337ab7");
  $("label:has(input[name=" + name + "]:checked)").css("color", "#fff");
}
$("input[name=pisos][value=1]").attr('checked', 'checked');
radioColorBlue('pisos_ascensor');
radioColorBlue('pisos_ascensor_servicio');
radioColorBlue('lista_ocupacion');
radioColorBlue('pisos');
radioColorBlue('pisos_escalera');

$('p:has(select[id=id_presupuesto])').css('display', 'none');
$('p:has(input[id=id_tipo_direccion])').css('display', 'none');
$('p:has(input[id=id_tipo_inmueble])').css('display', 'none');
$('p:has(input[id=id_ocupacidad_inmueble])').css('display', 'none');
$('p:has(input[id=valor_ocupacidad])').css('display', 'none');
$('p:has(input[id=id_complejidad])').css('display', 'none');
$('p:has(input[id=id_valor_ocupacidad])').css('display', 'none');
$('p:has(input[id=id_factor_complejidad])').css('display', 'none');
$('p:has(input[id=id_valor_ambiente_complejidad])').css('display', 'none');
$('p:has(input[id=id_valor_metrocubico_complejiadad])').css('display', 'none');

$('input[name="ascensor"]').on('switchChange.bootstrapSwitch', function(event, state) {
showContent();
});
$('input[name="ascensor_servicio"]').on('switchChange.bootstrapSwitch', function(event, state) {
showContent2();
});
$(document.getElementById("id_pisos_ascensor")).css('visibility','hidden');
$('label[for=id_pisos_ascensor_0]').css('visibility','hidden');
function showContent() {
  element = document.getElementById("id_pisos_ascensor");
  pisos = $('input:radio[name=pisos_escalera]:checked').val();
  check = document.getElementById("id_ascensor");
  label = $('label[for=id_pisos_ascensor_0]');
  if (check.checked) {
    $(element).css('visibility','visible');
    $(label).css('visibility','visible');
    if (pisos == "0"){
      $("input[name=pisos_ascensor][value=0]").attr('checked', 'checked');
      radioColorBlue('pisos_ascensor');
    }else{
      $("input[name=pisos_ascensor][value=" + pisos +  "]").attr('checked', 'checked');
      radioColorBlue('pisos_ascensor');
    }
  }
  else {
    $("input[name=pisos_ascensor][value=0]").attr('checked', 'checked');
    $(element).css('visibility','hidden');
    $(label).css('visibility','hidden');
  }
}
$(document.getElementById("id_pisos_ascensor_servicio")).css('visibility','hidden');
$('label[for=id_pisos_ascensor_servicio_0]').css('visibility','hidden');
function showContent2() {
  element = document.getElementById("id_pisos_ascensor_servicio");
  pisos = $('input:radio[name=pisos_escalera]:checked').val();
  check = document.getElementById("id_ascensor_servicio");
  label = $('label[for=id_pisos_ascensor_servicio_0]');

  if (check.checked) {
    $(element).css('visibility','visible');
    $(label).css('visibility','visible');
    if (pisos == "0"){
      $("input[name=pisos_ascensor_servicio][value=0]").attr('checked', 'checked');
      radioColorBlue('pisos_ascensor_servicio');
    }else{
      $("input[name=pisos_ascensor_servicio][value=" + pisos + "]").attr('checked', 'checked');
      radioColorBlue('pisos_ascensor_servicio');
    }
  }
  else {
    $("input[name=pisos_ascensor_servicio][value=0]").attr('checked', 'checked');
    $(element).css('visibility','hidden');
    $(label).css('visibility','hidden');
  }
}
