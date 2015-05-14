// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_productos"; // id
var nombre_boton_eliminar = ".edit"; // Clase
var nombre_formulario_modal = "#frmEdit"; //id

// Fin de configuraciones
    $(document).on('ready',function(){

        $(".edit").on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            var opcion = $(this).data('opcion');
            $('#modal_idModulo').val(Pid);
            $('#modal_name2').text(name);
            $('#id_modulo').val(name);
            $('#id_orden').val(opcion);
        });

        var options = {
            success:function(response){

                if(response.form=="edit"){
                    if(response.status=="True"){
                        alert("registrado exitosamente!");

                        location.reload();
                    }else{
                        alert("Hubo un error al edit!");
                        $("#myModal2").modal('hide');
                    }
                }

            }
        };

        $(nombre_formulario_modal).ajaxForm(options);
    });
