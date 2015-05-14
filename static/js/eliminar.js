// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id

// Fin de configuraciones
    $(document).on('ready',function(){
        $(".delete").on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_id').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response){

                    if(response.status=="True"){
                        alert("Eliminado!");
                        var id = response.item_id;
                        var elementos= $(nombre_tabla +' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+id).remove();
                            $("#myModal").modal('hide');

                        }

                    }else{
                        alert("Hubo un error al eliminar! " + response.msj);
                        $("#myModal").modal('hide');
                    }


                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
    });
