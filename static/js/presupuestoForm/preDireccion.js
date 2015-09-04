setTimeout(function() {
document.getElementById('id_direccion').focus();
},100);

function showContent() {
  element = document.getElementById("s_pisos_ascensor");
  pisos = document.getElementById("id_pisos_escalera").value;
  check = document.getElementById("id_ascensor");

  if (check.checked) {
    $('#s_pisos_ascensor').css('visibility','visible');
    if (pisos == "0"){
      document.getElementById("id_pisos_ascensor").value = "1";
    }else{
      document.getElementById("id_pisos_ascensor").value = pisos;
    }

  }
  else {
    $('#s_pisos_ascensor').css('visibility','hidden');
    document.getElementById("id_pisos_ascensor").value = "0";
  }
}
function showContent2() {
  element2 = document.getElementById("s_pisos_ascensor_servicio");
  pisos = document.getElementById("id_pisos_escalera").value;
  check2 = document.getElementById("id_ascensor_servicio");
  if (check2.checked) {
    $('#s_pisos_ascensor_servicio').css('visibility','visible');
    if (pisos == "0"){
      document.getElementById("id_pisos_ascensor_servicio").value = "1";
    }else{
      document.getElementById("id_pisos_ascensor_servicio").value = pisos;
    }
  }
  else {
    $('#s_pisos_ascensor_servicio').css('visibility','hidden');
    document.getElementById("id_pisos_ascensor_servicio").value = "0";
  }
}
  $("input[name=lista_tipoinmueble]").click(function () {
    id_tipoinmueble = $('input[name=lista_tipoinmueble]:checked').val();
    $.get('/presupuesto/direccion/nuevo',
      {id_tipoinmueble: id_tipoinmueble},
      function(data){
        $("#id_tipo_inmueble").val(data[0].tipoinmueble);
      });
  });

  $("input[name=lista_ocupacion]").click(function () {
    id_ocupacion = $('input[name=lista_ocupacion]:checked').val();
    $.get('/presupuesto/direccion/nuevo',
      {id_ocupacion: id_ocupacion},
      function(data){
        $("#id_ocupacidad_inmueble").val(data[0].ocupacion);
        $("#id_valor_ocupacidad").val(data[0].valorocupacion);
      });
  });
