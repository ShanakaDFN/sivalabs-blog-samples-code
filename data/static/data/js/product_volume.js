if (!$) {
    $ = django.jQuery;
}
$(document).ready(function(){
    // Add event listener to "price" input
    $("#id_volume").focus(function(e){
        let volume = 1
        $("#id_volume").val(volume);
        // Get Height
        //let height = parseFloat($(this).val());
        let height = parseFloat($("#id_height").val())

        // Get Length
        let length = parseFloat($("#id_length").val())

        // Get Length
        let width = parseFloat($("#id_width").val())

        // Compute total price in whatever way you want
        volume = length * width * height;

        // Set value in read-only "total_price" field.
        $("#id_volume").val(volume);
    });
})