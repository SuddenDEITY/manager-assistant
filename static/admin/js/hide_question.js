hide_fields=false;
window.addEventListener("load", function() {
    django.jQuery(document).ready(function(){
        if (django.jQuery('#id_answer_set-0-type').is('withdata')) {
            django.jQuery("#id_answer_set-0-sort_field").show();
            django.jQuery("#id_answer_set-0-sort_value").show();
            hide_fields=false;      
        } else {
            django.jQuery("#id_answer_set-0-sort_field").hide();
            django.jQuery("#id_answer_set-0-sort_value").hide();
            hide_fields=true;
        }
        django.jQuery("#id_answer_set-0-type").click(function(){
            hide_fields=!hide_fields;
            if (hide_fields) {
                django.jQuery("#id_answer_set-0-sort_field").show();
                django.jQuery("#id_answer_set-0-sort_value").show();
            } else {
                django.jQuery("#id_answer_set-0-sort_field").hide();
                django.jQuery("#id_answer_set-0-sort_value").hide();
                
            }
        })
    })
});