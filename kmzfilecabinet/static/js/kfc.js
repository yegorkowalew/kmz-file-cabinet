jQuery(document).ready(function($){
    $(".close").click(function(){
        $("#myAlert").alert("close");
    });

    $('input[type=text]').bind('input propertychange', function() {
        if ($(this).val().length > 2) {
        $(".search-table").css({'display':'block'});
        $.getJSON( "/search/"+this.value, function( json ) {
            $(".alert").removeClass( "alert-danger" );
            $(".alert").text('Нашлось: ' + json.length);
            if (json.length) {
                console.log('json.length')
                $(".table > tbody > tr").remove();
                $.each( json, function( key, val ) {
                    $('.table > tbody:last-child').append(
                        `<tr><td><div class="form-check form-check-inline"><input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"></div>
                        </td><td>${val.fields.nom_num}</td><td><a href="">${val.fields.designation}</a></td><td>${val.fields.edit_date}</td></tr>`);
                    })
            } else {
                $(".search-table").css({'display':'none'});
                $(".alert").text('Ничего не нашлось');
                $(".alert").addClass( "alert-danger" );
                $(".table > tbody > tr").remove();
            }

            });
        } else {
            $(".search-table").css({'display':'none'});
            $(".alert").text('Минимальное количество символов для поиска - 3');
            $(".alert").removeClass( "alert-danger" );
            $(".alert").addClass( "alert-primary" );
        }
    });
});

