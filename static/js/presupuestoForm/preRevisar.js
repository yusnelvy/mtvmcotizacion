$(document).ready(function () {
    if ($('#id_tipo_calculo').val() === 'Optimizado') {
        $("#optimizado").attr("checked", "checked");
        radioColorBlue();
        checkOptimizado();
    }else if($('#id_tipo_calculo').val() == 'Basico'){
        $("#basico").attr("checked","checked");
        radioColorBlue();
        checkBasico();
    }else if ($('#id_tipo_calculo').val() == 'Revisado'){
        $("#revisado").attr("checked","checked");
        radioColorBlue();
        checkRevisado();
        EnableRevisadoInput();
        radioBenable();
    }
    if ($('#id_descuento_recargo').val() == $('#descuento').val()){
        $("#descuento").attr("checked","checked");
        descuentoRecargoj();
    }
    if ($('#id_descuento_recargo').val() == $('#recargo').val()){
        $("#recargo").attr("checked","checked");
        descuentoRecargoj();
    }
    $('#basico').click(function(){
        radioColorBlue();
        checkBasico();
        radioBdisabled();
        limpiar('totalRecurso',0);
        limpiar('descuentoRecargo',0);
        radioTotal();
        DisableRevisadoInput();
        descuentoRecargoj();
    });
    $('#optimizado').click(function(){
        radioColorBlue();
        checkOptimizado();
        radioBdisabled();
        limpiar('totalRecurso',0);
        limpiar('descuentoRecargo',0);
        radioTotal();
        DisableRevisadoInput();
        descuentoRecargoj();
    });
    $('#revisado').click(function(){
        EnableRevisadoInput();
        radioColorBlue();
        checkRevisado();
        radioBenable();
        descuentoRecargoj();
        proponerMontoTotalRecurso();
    });
    proponerMontoTotalRecurso();
    $('#m3').click(function(){
        $('#id_monto_recursos_revisado').val(parseFloat($('#montom3inmueble').text().replace(',','')).toFixed(2));
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#amb').click(function(){
        $('#id_monto_recursos_revisado').val(parseFloat($('#montoambinmueble').text().replace(',','')).toFixed(2));
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#rrhh').click(function(){
        $('#id_monto_recursos_revisado').val(parseFloat($('#montopersonateorica').text().replace(',','')).toFixed(2));
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#rrhha').click(function(){
        $('#id_monto_recursos_revisado').val(parseFloat($('#montopersonaoptima').text().replace(',','')).toFixed(2));
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#descuento').click(function(){
        $('#id_descuento_recargo').val($('#descuento').val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#id_monto_descuento_recargo').val(), $('#id_descuento_recargo').val());
        totalmudanzarevisadooptmo = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_recargooptimo').val(), $('#id_descuento_recargo').val());
        totalmudanzarevisadobasico = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_regargobasico').val(), $('#id_descuento_recargo').val());
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
        $("#mudanzamontorevisadooptimo").val(totalmudanzarevisadooptmo);
        $("#mudanzamontorevisadotoerico").val(totalmudanzarevisadobasico);
    });
    $('#recargo').click(function(){
        $('#id_descuento_recargo').val($('#recargo').val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#id_monto_descuento_recargo').val(), $('#id_descuento_recargo').val());
        totalmudanzarevisadooptmo = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_recargooptimo').val(), $('#id_descuento_recargo').val());
        totalmudanzarevisadobasico = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_regargobasico').val(), $('#id_descuento_recargo').val());
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
        $("#mudanzamontorevisadooptimo").val(totalmudanzarevisadooptmo);
        $("#mudanzamontorevisadotoerico").val(totalmudanzarevisadobasico);
    });
    $('#id_monto_recursos_revisado').on('keyup', function(){
        limpiar('totalRecurso',0);
        radioTotal();
        proponerMontoTotalRecurso();
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#id_monto_vehiculo_revisado').on('keyup', function(){
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#id_monto_servicios_revisado').on('keyup', function(){
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#id_monto_materiales_revisado').on('keyup', function(){
        totalmudanza = calcular_totalmudanza($("#id_monto_recursos_revisado").val(), $("#id_monto_vehiculo_revisado").val(), $("#id_monto_servicios_revisado").val(), $("#id_monto_materiales_revisado").val());
        porc_descuento = calcular_porcdescuentorecargo(totalmudanza, $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado(totalmudanza, $("#id_monto_descuento_recargo").val(), $('#id_descuento_recargo').val());
        $("#id_monto_mundanza_revisada").val(totalmudanza);
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#id_monto_descuento_recargo').on('keyup', function(){
        porc_descuento = calcular_porcdescuentorecargo($("#id_monto_mundanza_revisada").val(), $("#id_monto_descuento_recargo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#id_monto_descuento_recargo').val(), $('#id_descuento_recargo').val());
        $("#porc_descuento").val(porc_descuento);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#porc_descuento').on('keyup', function(){
        descuentorecargo = calcular_descuentorecargo($("#id_monto_mundanza_revisada").val(), $("#porc_descuento").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), descuentorecargo, $('#id_descuento_recargo').val());
        $("#id_monto_descuento_recargo").val(descuentorecargo);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#descuento_recargooptimo').on('keyup', function(){
        porc_descuento = calcular_porcdescuentorecargo($("#id_monto_mundanza_revisada").val(), $("#descuento_recargooptimo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_recargooptimo').val(), $('#id_descuento_recargo').val());
        $("#porc_descuentooptimo").val(porc_descuento);
        $("#mudanzamontorevisadooptimo").val(totalmudanzarevisado);
        $("#porc_descuento").val(porc_descuento);
        $("#id_monto_descuento_recargo").val($('#descuento_recargooptimo').val());
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#porc_descuentooptimo').on('keyup', function(){
        descuentorecargo = calcular_descuentorecargo($("#id_monto_mundanza_revisada").val(), $("#porc_descuentooptimo").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), descuentorecargo, $('#id_descuento_recargo').val());
        $("#descuento_recargooptimo").val(descuentorecargo);
        $("#mudanzamontorevisadooptimo").val(totalmudanzarevisado);
        $("#porc_descuento").val($('#porc_descuentooptimo').val());
        $("#id_monto_descuento_recargo").val(descuentorecargo);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#descuento_regargobasico').on('keyup', function(){
        porc_descuento = calcular_porcdescuentorecargo($("#id_monto_mundanza_revisada").val(), $("#descuento_regargobasico").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_regargobasico').val(), $('#id_descuento_recargo').val());
        $("#porc_descuentobasico").val(porc_descuento);
        $("#mudanzamontorevisadotoerico").val(totalmudanzarevisado);
        $("#porc_descuento").val(porc_descuento);
        $("#id_monto_descuento_recargo").val($('#descuento_regargobasico').val());
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
    $('#porc_descuentobasico').on('keyup', function(){
        descuentorecargo = calcular_descuentorecargo($("#id_monto_mundanza_revisada").val(), $("#porc_descuentobasico").val());
        totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), descuentorecargo, $('#id_descuento_recargo').val());
        $("#descuento_regargobasico").val(descuentorecargo);
        $("#mudanzamontorevisadotoerico").val(totalmudanzarevisado);
        $("#porc_descuento").val($('#porc_descuentobasico').val());
        $("#id_monto_descuento_recargo").val(descuentorecargo);
        $("#mudanzamontorevisado").val(totalmudanzarevisado);
    });
});
// funcion para calcular el total de la mudanza antes del desc/recargo
function calcular_totalmudanza(valorrecurso,valorvehiculo,valorservicio,valormaterial){
    var resultado = 0;
    resultado= parseFloat(valorrecurso) + parseFloat(valorvehiculo) + parseFloat(valorservicio) + parseFloat(valormaterial);
    if (isNaN(parseFloat(resultado))) {
        resultado=0;
    }
    return resultado.toFixed(2);
}
function calcular_porcdescuentorecargo(totalmudanza, descuentorecargo){
    var resultado=0;
    resultado=(descuentorecargo/totalmudanza)*100;
    if (isNaN(parseFloat(resultado))) {
        resultado=0;
    }
    return resultado.toFixed(2);
}
function calcular_descuentorecargo(totalmudanza, porcdescuentorecargo){
    var resultado=0;
    resultado=(totalmudanza*porcdescuentorecargo)/100;
    if (isNaN(parseFloat(resultado))) {
        resultado=0;
    }
    return resultado.toFixed(2);
}
function calcular_totalmudanzarevisado(totalmudanza, descuentorecargo, operador){
    var resultado = 0;
    resultado=eval(parseFloat(totalmudanza) + operador +  parseFloat(descuentorecargo));
    if (isNaN(parseFloat(resultado))) {
        resultado=0;
    }
    return resultado.toFixed(2);
}
function proponerMontoTotalRecurso () {
    var montoRecursoRevisado = $('#id_monto_recursos_revisado').val();
    var montoM3 = parseFloat($('#montom3inmueble').text().replace(',','')).toFixed(2);
    var montoInmueble = parseFloat($('#montoambinmueble').text().replace(',','')).toFixed(2);
    var montoRRHH = parseFloat($('#montopersonateorica').text().replace(',','')).toFixed(2);
    var montoRRHHAdicional = parseFloat($('#montopersonaoptima').text().replace(',','')).toFixed(2);
    if(montoRecursoRevisado == montoM3){
        $('#montom3inmueble').click();
    }
    if(montoRecursoRevisado == montoInmueble){
        $('#montoambinmueble').click();
    }
    if(montoRecursoRevisado == montoRRHH){
        $('#montopersonateorica').click();
    }
    if(montoRecursoRevisado == montoRRHHAdicional){
        $('#montopersonaoptima').click();
    }
}
function radioColorBlue () {
    $("td:has(input[name=enviarPresupuesto])").removeClass('checkedBlue');
    $("td:has(input[name=enviarPresupuesto]:checked)").addClass('checkedBlue');
}
function radioTotal () {
    $("td:has(input[name=totalRecurso])").removeClass('checkedBlue');
    $("td:has(input[name=totalRecurso]:checked)").addClass('checkedBlue');
}
function descuentoRecargoj () {
    $("td:has(input[name=descuentoRecargo])").removeClass('checkedBlue');
    $("td:has(input[name=descuentoRecargo]:checked)").addClass('checkedBlue');
}
function limpiar (cual, accion) {
    var f = document.formulario;
    for (var i=0; i<f.elements.length; i++){
        var obj = f.elements[i];
        var name = obj.name;
        if (name==cual){
            obj.checked = ((accion==1)? true : ((accion===0)? false : !obj.checked));
        }
    }
}
function radioBdisabled () {
    document.getElementById("m3").disabled = true;
    document.getElementById("amb").disabled = true;
    document.getElementById("rrhh").disabled = true;
    document.getElementById("rrhha").disabled = true;
}
function radioBenable () {
    document.getElementById("m3").disabled = false;
    document.getElementById("amb").disabled = false;
    document.getElementById("rrhh").disabled = false;
    document.getElementById("rrhha").disabled = false;
}
function RecargodisabledBasico () {
    document.getElementById("descuento_regargobasico").disabled = true;
    document.getElementById("porc_descuentobasico").disabled = true;
    $('#descuento_regargobasico').css('background', 'none');
    $('#porc_descuentobasico').css('background', 'none');
    document.getElementById("descuento_regargobasico").value = 0;
    document.getElementById("porc_descuentobasico").value = 0;
}
function RecargoEnableBasico ()  {
    document.getElementById("descuento_regargobasico").disabled = false;
    document.getElementById("porc_descuentobasico").disabled = false;
}
function RecargodisabledOptimo () {
    document.getElementById("descuento_recargooptimo").disabled = true;
    document.getElementById("porc_descuentooptimo").disabled = true;
    $('#descuento_recargooptimo').css('background', 'none');
    $('#porc_descuentooptimo').css('background', 'none');
    document.getElementById("descuento_recargooptimo").value = 0;
    document.getElementById("porc_descuentooptimo").value = 0;
}
document.getElementById("descuento_recargooptimo").value = 0;
document.getElementById("porc_descuentooptimo").value = 0;
function RecargoEnableOptimo () {
    document.getElementById("descuento_recargooptimo").disabled = false;
    document.getElementById("porc_descuentooptimo").disabled = false;
}
function RecargodisabledRevisado () {
    document.getElementById("id_monto_descuento_recargo").disabled = true;
    document.getElementById("porc_descuento").disabled = true;
    $('#id_monto_descuento_recargo').css('background', 'none');
    $('#porc_descuento').css('background', 'none');
    document.getElementById("id_monto_descuento_recargo").value = 0;
    document.getElementById("porc_descuento").value = 0;
}
function RecargoEnableRevisado () {
    document.getElementById("id_monto_descuento_recargo").disabled = false;
    document.getElementById("porc_descuento").disabled = false;
}
function DisableRevisadoInput () {
    document.getElementById("id_monto_recursos_revisado").disabled = true;
    document.getElementById("id_monto_vehiculo_revisado").disabled = true;
    document.getElementById("id_monto_servicios_revisado").disabled = true;
    document.getElementById("id_monto_materiales_revisado").disabled = true;
}
DisableRevisadoInput();
function EnableRevisadoInput () {
    document.getElementById("id_monto_recursos_revisado").disabled = false;
    document.getElementById("id_monto_vehiculo_revisado").disabled = false;
    document.getElementById("id_monto_servicios_revisado").disabled = false;
    document.getElementById("id_monto_materiales_revisado").disabled = false;
}
$('#id_monto_recursos_revisado').css('background', 'none');
$('#id_monto_vehiculo_revisado').css('background', 'none');
$('#id_monto_servicios_revisado').css('background', 'none');
$('#id_monto_materiales_revisado').css('background', 'none');
function checkBasico () {
    $('.check').addClass('selec');
    $('.check2').removeClass('selec');
    $('.check3').removeClass('selec');
    $('#id_tipo_calculo').val('Basico');
    $('#id_monto_recursos_revisado').val(parseFloat($('#montorecursobasico').text().replace(',','')).toFixed(2));
    $('#id_monto_vehiculo_revisado').val(parseFloat($('#vehiculomontobasico').text().replace(',','')).toFixed(2));
    $('#id_monto_servicios_revisado').val(parseFloat($('#montoserviciosbasico').text().replace(',','')).toFixed(2));
    $('#id_monto_materiales_revisado').val(parseFloat($('#montomaterialesbasico').text().replace(',','')).toFixed(2));
    $('#id_monto_mundanza_revisada').val(parseFloat($('#montomudanzahrsdirectas').text().replace(',','')).toFixed(2));
    $('#id_monto_descuento_recargo').val(parseFloat($('#descuento_regargobasico').val().replace(',','')).toFixed(2));
    $('#porc_descuento').val(parseFloat($('#porc_descuentobasico').val().replace(',','')).toFixed(2));
    $('#mudanzamontorevisado').val(parseFloat($('#mudanzamontorevisadotoerico').val().replace(',','')).toFixed(2));
    RecargoEnableBasico();
    RecargodisabledOptimo();
    RecargodisabledRevisado();
    totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_recargooptimo').val(), $('#id_descuento_recargo').val());
    $("#mudanzamontorevisadooptimo").val(totalmudanzarevisado);
    $('.input-descuento-recargo').addClass('input-re-no-border');
    $('.input-re').addClass('input-re-no-border');
    $('#descuento_regargobasico').removeClass('input-re-no-border');
    $('#porc_descuentobasico').removeClass('input-re-no-border');
}
function checkOptimizado () {
    $('.check').removeClass('selec');
    $('.check3').removeClass('selec');
    $('.check2').addClass('selec');
    $('#id_tipo_calculo').val('Optimizado');
    $('#id_monto_recursos_revisado').val(parseFloat($('#montorecursooptimo').text().replace(',','')).toFixed(2));
    $('#id_monto_vehiculo_revisado').val(parseFloat($('#vehiculomontooptima').text().replace(',','')).toFixed(2));
    $('#id_monto_servicios_revisado').val(parseFloat($('#montoserviciosoptima').text().replace(',','')).toFixed(2));
    $('#id_monto_materiales_revisado').val(parseFloat($('#montomaterialesoptima').text().replace(',','')).toFixed(2));
    $('#id_monto_mundanza_revisada').val(parseFloat($('#montomundanzahrsoptimas').text().replace(',','')).toFixed(2));
    $('#id_monto_descuento_recargo').val(parseFloat($('#descuento_recargooptimo').val().replace(',','')).toFixed(2));
    $('#porc_descuento').val(parseFloat($('#porc_descuentooptimo').val().replace(',','')).toFixed(2));
    $('#mudanzamontorevisado').val(parseFloat($('#mudanzamontorevisadooptimo').val().replace(',','')).toFixed(2));
    RecargodisabledBasico();
    RecargoEnableOptimo();
    RecargodisabledRevisado();
    totalmudanzarevisado = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_regargobasico').val(), $('#id_descuento_recargo').val());
    $("#mudanzamontorevisadotoerico").val(totalmudanzarevisado);
    $('.input-descuento-recargo').addClass('input-re-no-border');
    $('.input-re').addClass('input-re-no-border');
    $('#descuento_recargooptimo').removeClass('input-re-no-border');
    $('#porc_descuentooptimo').removeClass('input-re-no-border');
}
function checkRevisado () {
    $('.check3').addClass('selec');
    $('.check2').removeClass('selec');
    $('.check').removeClass('selec');
    $('#id_tipo_calculo').val('Revisado');
    RecargodisabledBasico();
    RecargodisabledOptimo();
    RecargoEnableRevisado();
    totalmudanzarevisadooptmo = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_recargooptimo').val(), $('#id_descuento_recargo').val());
    totalmudanzarevisadobasico = calcular_totalmudanzarevisado($("#id_monto_mundanza_revisada").val(), $('#descuento_regargobasico').val(), $('#id_descuento_recargo').val());
    $("#mudanzamontorevisadooptimo").val(totalmudanzarevisadooptmo);
    $("#mudanzamontorevisadotoerico").val(totalmudanzarevisadobasico);
    $('.input-descuento-recargo').removeClass('input-re-no-border');
    $('.input-re').removeClass('input-re-no-border');
    $('#descuento_regargobasico').addClass('input-re-no-border');
    $('#porc_descuentobasico').addClass('input-re-no-border');
    $('#descuento_recargooptimo').addClass('input-re-no-border');
    $('#porc_descuentooptimo').addClass('input-re-no-border');
    $('#mudanzamontorevisadooptimo').addClass('input-re-no-border');
    $('#mudanzamontorevisadotoerico').addClass('input-re-no-border');
    $('#mudanzamontorevisado').addClass('input-re-no-border');
    $('#id_monto_mundanza_revisada').addClass('input-re-no-border');
}
$('#myform').submit(function () {
    EnableRevisadoInput();
});
