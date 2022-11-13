
    var ws = new WebSocket("ws://localhost:7000");
    $(window).on('beforeunload', function(){
       ws.close();
    });

    ws.onerror = function(event) {
        location.reload();
    }
    ws.onmessage = function(event)  {
        var message_received = event.data;
        chat_add_message(message_received, false);
    };

    function chat_add_message(message, isUser) {
      var person = isUser ? 'user' : '';
        var html = '\
        <div class="chat_line">\
            <div class="chat_bubble'+person+'">\
              <div class="chat_triangle'+person+'"></div>\
               '+message+' \
            </div>\
        </div>\
        ';
        chat_add_html(html);
    }
    // Add HTML to the chat
    function chat_add_html(html) {
        $("#chat_log").append(html);
        chat_scrolldown();
    }

    function chat_scrolldown() {
        $("#chat_log").animate({ scrollTop: $("#chat_log")[0].scrollHeight }, 500);
    }

    $(function() {
       $('#chat_input').on('keypress', function(event) {
          if (event.which === 13 && $(this).val() != ""){
             var message = $(this).val();
             $(this).val("");
             chat_add_message(message, true);
             ws.send(message);
          }
       });
    });

    $(document).ready(function(){
   $("img").click(function(){
        $("div").slideToggle();
    });
    });