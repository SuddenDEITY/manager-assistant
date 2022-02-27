
window.addEventListener("load", function() {
        django.jQuery('#id_type').change(function(){
            
            if (django.jQuery('#id_type').val() == 'withdata') {
                django.jQuery(".field-sort_field").show();
                django.jQuery(".field-sort_value").show();
            } else {
                django.jQuery(".field-sort_field").hide();
                django.jQuery(".field-sort_value").hide();
                
            }
        })
});