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
    $(setup)

    function setup() {
      $('#id_lista_mueble').zelect({ placeholder:'Seleccione el mueble' });
      $('#id_lista_ambiente').zelect({ placeholder:'Seleccione el ambiente' });
    }

