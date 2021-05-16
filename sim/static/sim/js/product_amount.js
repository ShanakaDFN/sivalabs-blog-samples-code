if (!$) {
    $ = django.jQuery;
}
$(document).ready(function(){

    // Add event listener to "price" input
    $(".field-product").click(function(e){
        let id = e.target.id.toString();
        var arr = id.split("-");
        var element_id = arr[1];
        /*alert(id);*/

        $('#' + id).change(function() {
            var product_id = $('#' + id).find(":selected").val();
            /*alert(value);*/

            $.ajax({
                type: 'GET',
                url: "getProductUnitPrice",
                data: {"product_id": product_id},
                success: function (response) {
                    var quantity_id = 'id_shipmentdetail_set-'+element_id+'-quantity'
                    $('#' + quantity_id).val(1);  

                    var unit_price = response["unit_price"];
                    var unit_price_id ='id_shipmentdetail_set-'+element_id+'-unit_price';
                    $('#' + unit_price_id).val(unit_price);

                    var amount = unit_price * 1;
                    var amount_id = 'id_shipmentdetail_set-'+element_id+'-amount';
                    $('#' + amount_id).val(amount);
                },
                error: function (response) {
                    console.log(response)
                }
            })
        });

    });

    $(".field-quantity").click(function(e){
        let id = e.target.id.toString();
        var arr = id.split("-");
        var element_id = arr[1];

        $('#' + id).change(function() {
            var quantity_id = 'id_shipmentdetail_set-'+element_id+'-quantity';
            var quantity = parseFloat($('#' + quantity_id).val());

            var unit_price_id ='id_shipmentdetail_set-'+element_id+'-unit_price';
            var unit_price = parseFloat($('#' + unit_price_id).val());

            var amount = unit_price * quantity;
            var amount_id = 'id_shipmentdetail_set-'+element_id+'-amount';
            $('#' + amount_id).val(amount);

        });

    });
    
})