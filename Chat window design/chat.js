
    function chat_add_message(message, isUser) {
      console.log(message);  
      var person = isUser ? 'user' : '';
      console.log('person: '+person)
      var html = '';

      if (person == 'user')
      {
        html = '<div class="msg user-message" id="userMessage" style="flex-direction: column;">\
            <div class="flexAligndiv1">\
                <div class="user-messagefull messageContent flex-design">\
                    <span id="userMsg">'+message+'</span>\
                </div>\
            </div>\
        </div>\
      ';
      }

      else
      {
        html = '<div class="msg bot-message" id="botMessage">\
          <div class="flex-design">\
              <div class="bot-image-container">\
              </div>\
              <div class="bot-messagefull messageContent">\
                  <span id="botMessage">'+message+'</span>\
              </div>\
          </div>\
        </div>';
      }

      chat_add_html(html);

    }
    
    // Add HTML to the chat
    function chat_add_html(html) {
        $("#messages").append(html);
        chat_scrolldown();
    }

    function chat_scrolldown() {
        $("#messages").animate({ scrollTop: $("#messages")[0].scrollHeight }, 500);
    }

    $(function() {
       $('#query').on('keypress', function(event) {
          if (event.which === 13 && $(this).val() != ""){
             var message = $(this).val();
             $(this).val("");
             chat_add_message(message, true);
             
            $.ajax({
                url: 'http://127.0.0.1:7000/',
                type: 'GET',
                cache: false,
                contentType:'application/x-www-form-urlencoded; charset=UTF-8',
                data : {"msg":message},
                dataType : "json",
                context: this,
                success: function(event) {
                    console.log(event);
                    console.log(event.text);
                    console.log(typeof(event.text));

                    if (typeof(event.text) == "object"){
                        event.text.forEach(element => {
                            console.log(element.text.text);
                            var message_received = element.text.text;
                            console.log(message_received);
                            chat_add_message(message_received, false);
                        });
                    }
                
                    else{

                        var message_received = event.text;
                        console.log(message_received);
                        chat_add_message(message_received, false);

                    }
                    
                }
             
            })
          }

       });
    });