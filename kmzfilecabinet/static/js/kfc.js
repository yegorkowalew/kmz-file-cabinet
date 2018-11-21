jQuery(document).ready(function($){
    $(".close").click(function(){
        $("#myAlert").alert("close");
    });

    $('input[type=text]').bind('input propertychange', function() {
        // console.log( $(this).val().length );
        if ($(this).val().length > 4) {
        $.getJSON( "/search/"+this.value, function( json ) {
            $(".table > tbody > tr").remove();
            $.each( json, function( key, val ) {
                $('.table > tbody:last-child').append(
                    `<tr><td><div class="form-check form-check-inline"><input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"></div>
                    </td><td>${val.fields.nom_num}</td><td><a href="">${val.fields.designation}</a></td><td>${val.fields.edit_date}</td></tr>`);
                })
            });
        };
    });
});