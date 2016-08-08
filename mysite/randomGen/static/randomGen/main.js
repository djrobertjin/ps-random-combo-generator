
$(function() {


    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        generate();
    });

    function generate() {
      console.log("generate is working")
      console.log($('#id_excl_family_choices').val())
      $.ajax({
        url : "./generate/", // endpoint
        type : "POST", // http method
        data : { 
          excl_Sonic: $('#id_excl_Sonic').is(':checked'),
          excl_Palm : $('#id_excl_Palm').is(':checked'), 
          excl_family_choices : $('#id_excl_family_choices').val(),
          the_length : $('#id_length').val()
          },  
        // handle a successful response
        success : function(json) {

          console.log(json);
          console.log("success");
          $('#results').html(json.result)
          console.log(json.result)
        },

        // handle a non-successful response
        error : function(xhr, errmsg, err) {
        $('#results').html("<div class ='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+"<a href='#' class = 'close'>&times;</a></div>"); // add error to DOM
          console.log(xhr.status + ": " + xhr.responseText); // log error info
        }
      });
    };


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

});