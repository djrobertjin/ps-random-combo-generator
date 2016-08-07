

// // // Submit post on submit
// $('#post-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     generate();
// });

// function generate() {
//   console.log("generate is working")
//   //console.log($('#id_length').val())
//   $.ajax({
//     url : "", // endpoint
//     type : "POST", // http method
//     data : { csrfmiddlewaretoken: "{{ csrf_token }}", the_length : $('#id_length').val()
//     }, // data sent with the post request

//     // handle a successful response
//     success : function(json) {
//       $('#id_length').val('');
//       console.log(json);
//       console.log("success");
//     },

//     // handle a non-successful response
//     error : function(xhr, errmsg, err) {
//     $('#results').html("<div class ='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+"<a href='#' class = 'close'>&times;</a></div>"); // add error to DOM
//       console.log(xhr.status + ": " + xhr.responseText); // log error info
//     }
//   });
// };

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
          }, // data sent with the post request
// csrfmiddlewaretoken: "{{ csrf_token }}", 
        // handle a successful response
        success : function(json) {
          // $('#id_length').val('');
          console.log(json);
          console.log("success");
          $('#results').html(json.result)
          console.log(json.result)
          // $('form').unbind().submit();
        },

        // handle a non-successful response
        error : function(xhr, errmsg, err) {
        $('#results').html("<div class ='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+"<a href='#' class = 'close'>&times;</a></div>"); // add error to DOM
          console.log(xhr.status + ": " + xhr.responseText); // log error info
        }
      });
    };

    // // AJAX for posting
    // function create_post() {
    //     console.log("create post is working!") // sanity check
    //     $.ajax({
    //         url : "create_post/", // the endpoint
    //         type : "POST", // http method
    //         data : { the_post : $('#post-text').val() }, // data sent with the post request
    //         // handle a successful response
    //         success : function(json) {
    //             $('#post-text').val(''); // remove the value from the input
    //             console.log(json); // log the returned json to the console
    //             $("#talk").prepend("<li><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+
    //                 "</span> - <a id='delete-post-"+json.postpk+"'>delete me</a></li>");
    //             console.log("success"); // another sanity check
    //         },
    //         // handle a non-successful response
    //         error : function(xhr,errmsg,err) {
    //             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
    //                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
    //             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    //         }
    //     });
    // };
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