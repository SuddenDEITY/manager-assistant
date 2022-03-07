var filter_by_arr = [];
var filter_json = {};
(function ($) {
    $('.item-wrapper').click(function (e) {
      e.stopPropagation();
      var thisDiv = $(this).find('ul');
      var category_id = $(this).find('a').attr('cat-id');
      $.get(`/get_equipment/${category_id}/${JSON.stringify({})}`,
            function(data){
                if (!thisDiv.hasClass('active')){
                    thisDiv.html('');
                    thisDiv.addClass('active').append(data).hide();
                    thisDiv.slideDown();
                }else{
                    thisDiv.removeClass('active').slideUp();
                }
            }
        );
        $(this).find('.material-icons').toggleClass('item-wrapper-down');
        $(this).find('.item-li').toggleClass('active-cat');
    });

    $('.answer-btn').click(function () {
        var thisDiv = $('.answer-wrapper');
        var question_id = $('.question-field').attr('quest-id');
        var answer_id = $(this).attr('ans-id');
        var category = $('.item-container');
        $.get(`/apply_answer/${question_id}/`,
              function(data){
                thisDiv.html('');
                thisDiv.append(data);
                $('.next-quest').html('');
                $('.next-quest').append($('#ajax-next-quest').text());
                
              }
          );
          
          $.get(`/get_filter_val/${answer_id}/${JSON.stringify(filter_json)}`,
              function(data){
                category.html('');
                category.append(data);
                var filter_field = $('#filter_by').find('#filter_by_field').text();
                var filter_value = $('#filter_by').find('#filter_by_value').text();
                filter_by_arr.push([filter_field,filter_value]);
                $.each(filter_by_arr, function(i, obj){
                    var key = obj[0];
                    var value = obj[1];
                    filter_json[key] = value;
                    console.log(filter_json);
                });
                $('#filter_by').remove();
              }
          );
      });

  })(jQuery);
