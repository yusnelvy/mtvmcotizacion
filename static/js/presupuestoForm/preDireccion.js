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

$('input[name="rampa"]').bootstrapSwitch();
$('input[name="ascensor"]').bootstrapSwitch();
$('input[name="ascensor_servicio"]').bootstrapSwitch();
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

function proponerPisos (pisos, check, msj, name ) {
  if (check.checked) {
    if (pisos == "0") {
      $("input[name=" + name + "][value=" + 0 + "]").click();
      radioColorBlue(name);
      $(msj).text(
        'Seleccione cantidad de pisos a recorrer por escaleras para agregar ascensor.'
        );
      $(msj).fadeIn();
      setTimeout(function () {
         $(msj).fadeOut();
      }, 4000);
      check.click();
    }else {
      $("input[name=" + name + "][value=" + pisos + "]").click();
      radioColorBlue(name);
    }
  }else {
    $("input[name=" + name + "][value=" + pisos + "]").click();
}
}

function showContent (element, check, label ) {
  if (check.checked) {
    $(element).fadeIn('fast');
    $(label).fadeIn('fast');
  }
  else {
    $(element).fadeOut('fast');
    $(label).fadeOut('fast');
  }
}

$('input[name="ascensor"]').on('switchChange.bootstrapSwitch', function(event, state) {

showContent(
  document.getElementById("id_pisos_ascensor"),
  document.getElementById("id_ascensor"),
  $('label[for=id_pisos_ascensor_0]')
    );

proponerPisos(
  $('input:radio[name=pisos_escalera]:checked').val(),
  document.getElementById("id_ascensor"),
  document.getElementById("msjError"),
  $("input[name=pisos_ascensor]").attr('name')
  );

});

$('input[name="ascensor_servicio"]').on('switchChange.bootstrapSwitch', function(event, state) {

showContent(
  document.getElementById("id_pisos_ascensor_servicio"),
  document.getElementById("id_ascensor_servicio"),
  $('label[for=id_pisos_ascensor_servicio_0]')
   );

proponerPisos(
  $('input:radio[name=pisos_escalera]:checked').val(),
  document.getElementById("id_ascensor_servicio"),
  document.getElementById("msjError"),
  $("input[name=pisos_ascensor_servicio]").attr('name')
  );

});

$('input:radio[name=pisos_escalera]').click(function () {

  proponerPisos(
  $('input:radio[name=pisos_escalera]:checked').val(),
  document.getElementById("id_ascensor"),
  document.getElementById("msjError"),
  $("input[name=pisos_ascensor]").attr('name')
  );

  proponerPisos(
  $('input:radio[name=pisos_escalera]:checked').val(),
  document.getElementById("id_ascensor_servicio"),
  document.getElementById("msjError"),
  $("input[name=pisos_ascensor_servicio]").attr('name')
  );

});

showContent(
  document.getElementById("id_pisos_ascensor"),
  document.getElementById("id_ascensor"),
  $('label[for=id_pisos_ascensor_0]')
   );

showContent(
  document.getElementById("id_pisos_ascensor_servicio"),
  document.getElementById("id_ascensor_servicio"),
  $('label[for=id_pisos_ascensor_servicio_0]')
   );
