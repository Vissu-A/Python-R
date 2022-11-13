const express = require('express')
const dialogflow = require('dialogflow');
const uuid = require('uuid');
const cors = require('cors')


const app = express()
app.use(cors())
const port = 7000

app.get('/', function(req, res){


    const projectId = 'internal-d5ea3';
    //const sessionId = uuid.v4();

//https://dialogflow.com/docs/agents#settings
// generate session id (currently hard coded)
    const sessionId = '981dbc33-7c54-5419-2cce-edf90efd2170';
    const query = 'hello';
    const languageCode = 'en-US';

    // Instantiate a DialogFlow client.

    let privateKey = '-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCjitEyoAazUgRi\nQqUQauqEAiFivzxuT/JbJr81ytavrn5LOJ/7Gn+itcnhdDrAqGAZyjJFZ+QBrkEO\nMpXOs4sF3PGZeGCp9uad06SIe7Dk3OeYiUfbqRj84ozCLCxh+xNd2db25oiv8BpN\nOSJ83XX3vAFSk9XMucn5Y1ZaqdId/hJ4+W0RLDSf2H6AhkDlaidfO4sGDvoVLzbw\nPc8A444n62NH1VSZuGgyGBiP7WOyKkhOSyWSLHgnoPlczVK7A86yEBJ7Q3FgJfMb\nXLBKNtdQdQGw1KL0faPiXd6W6Db1Nvc0CYyfXwWPXaejuLjvaT3SoH0zIww7zQwY\nDqNPXhYlAgMBAAECggEAA4ZlicUOZ+qREB92Hdi5cHoi8eqDzlqNnikuDruDbZrM\npj6Un4MGdGwdK21yf75mqzT4aOu7QSME9siggdRNCeW61Q9AbCFs0+2Ler/0bou+\nt9hg/WB+GqNKcTv7rT/4vqQy9d7psXsdd1kk1RKpQoX29FVIktv/+Q61qN4cr+Cb\ncGLltzjTniOhy7TEfdNfsgN9FCxN3NKOULM4WHZ/zQxz7M7pq+qxKOMvIyM3xDxs\nm455WQvWiPycXiSAS/TWVKpA8u1KpSQgH33IKrXbpIAx37AJIp0SYugndm+qKMwf\n5qAhEdnJAM5vcLnqRkDRdcnrxOdrVQNn+G4s73778QKBgQDlnjIuaBWMW4YfYu+0\nReJpLzrSisDY0kMAhfJLs94e8nL3W3uxRfzrV41K9lwDDa08lSdIc39YP22SerZi\nZLV7Y8qOcH7FQxdkhZEW9f2NJpqDHCLZI3mPfi7RdxVUWkT8p96Dl82RAEWJTkM8\nqCbP/AMW8qEsvCIb8NOPy8869QKBgQC2VR82bFbTdz837JHJVTStGNFMLv/Fv5eh\nKFYquPxiteZukGva54ib713PCWWZGn5u7x2/4MSraLXh5Cb1VB8+oVWUQmwRoO1I\nr3TSheQUI0SkNP3/KUBtvaCwnwIAlx5Ayd7xxoxz5JmL14gPrVHLd/mO/+kdgY7C\nkuJUMkbQcQKBgHKxDQGvDaxY/upogbC7A3dklu4ZTnA+vibhwP/dLQKqOZCiSmtm\nuQlYZwPdgGIqD7DmE4QV5LLQo8t5reYBxcCHPOLfAANKGsIkES+12VsKwDzi7ekl\n1g89iOcpoybKHBFTTErQpWZbC2ClDeKbXx+eEnEA6k6s/iCUryfxNmaNAoGAHoGN\ncFieClF4RU4SckIMRy3QztNKPfa5UuBh0lITABz5CeSl9wEoDRb2dg5Xbk9NehgN\nvS3JGfix/bJjhkZl19+8ZsraM/Td3nxkqlh2eZwQ/vxSxt9LBVFl0kc4WYrvJ93e\nrEsQ8s77lbcg76aK+eT/3xoYEbS8gvd6YKXszTECgYA9LQanQiVOpAmxBW43XDag\n6H+J0FRJqvujO4i//qBn2zwuefostUu1fitEVg0IraTNIXJKAqFr/0Ttqup7NHeZ\nbKTt1/AKYGggbMDfJwruDTrMme5ZExRLSOtM8LbUSYmKCgwJ6KCJeGWbJjrL/lbJ\nB0KknLaD/ath7ELNKEIKmg==\n-----END PRIVATE KEY-----\n';

// as per goolgle json
    let clientEmail = "internal-d5ea3@appspot.gserviceaccount.com";
    let config = {
        credentials: {
            private_key: privateKey,
            client_email: clientEmail
        }
    }
    const sessionClient = new dialogflow.SessionsClient(config);

    // Define session path
    const sessionPath = sessionClient.sessionPath(projectId, sessionId);

    // The text query request.
    const request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: query,
                languageCode: languageCode,
            },
        },
    };

// Send request and log result
sessionClient
  .detectIntent(request)
  .then(responses => {
    console.log('Detected intent');
    const result = responses[0].queryResult;
    console.log(`  Query: ${result.queryText}`);
    console.log(`  Response: ${result.fulfillmentText}`);
    reply = {"text":`${result.fulfillmentText}`};
    res.send(reply);
    if (result.intent) {
      console.log(`  Intent: ${result.intent.displayName}`);
    } else {
      console.log(`  No intent matched.`);
    }
  })
  .catch(err => {
    console.error('ERROR:', err);
  });

    //var message = req.query.msg;

   
        // A unique identifier for the given session
    

    
    // console.log(req.query.msg);
    // reply = {"text":"welcome"};
    // res.send(reply);
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))