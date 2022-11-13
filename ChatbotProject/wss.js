const dialogflow = require('dialogflow');
const uuid = require('uuid');

var WebSocketServer = require('ws').Server;
var PORT = 7000;
var wss = new WebSocketServer({port: PORT});

wss.on('connection', function (ws) {
    ws.on('message', function (message) {
      console.log('received: %s', message)
      ///////////////////////////////////////////////////////////////////////

      async function runSample(projectId = 'osione-44ec8') {
        // A unique identifier for the given session
        const sessionId = uuid.v4();
      
        // Create a new session
        const sessionClient = new dialogflow.SessionsClient();
        const sessionPath = sessionClient.sessionPath(projectId, sessionId);
      
        // The text query request.
        const request = {
          session: sessionPath,
          queryInput: {
            text: {
              // The query to send to the dialogflow agent
              text: message,
              // The language used by the client (en-US)
              languageCode: 'en-US',
            },
          },
        };
      
        // Send request and log result
        const responses = await sessionClient.detectIntent(request);
        console.log('Detected intent');
        const result = responses[0].queryResult;
        console.log(`  Query: ${result.queryText}`);
        console.log(`  Response: ${result.fulfillmentText}`);
        if (result.intent) {
          console.log(`  Intent: ${result.intent.displayName}`);
        } else {
          console.log(`  No intent matched.`);
        }
      }

      ///////////////////////////////////////////////////////////////////////

    
    })    
    
    // ws.send(res); 

    

    
})