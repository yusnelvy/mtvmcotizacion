
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
