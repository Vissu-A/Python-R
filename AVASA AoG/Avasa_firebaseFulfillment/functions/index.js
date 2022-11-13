/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';

const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const http = require('https');
const {Text, Card, Image, Suggestion, Payload} = require('dialogflow-fulfillment');
const host = 'osiintapp-osiusintranet.cs66.force.com';
const { dialogflow } = require('actions-on-google');
const { Carousel } = require('actions-on-google');
const { SimpleResponse } = require('actions-on-google');


const { Suggestions } = require('dialogflow-fulfillment');

//const app = dialogflow();
var speech='';
var dynaMessageChinese='';
var dynaMessageContinental='';
var dynaMessageHotelOffers='';
var dynaPartnerOffers='';
var userContext=null;
//const app = new DialogflowApp({request: request, response: response});
const app = dialogflow({debug: true});


process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements


exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
  var extResponse='';
  var position=0;
  var source='';
  
  
  function Selection_Option_Handler(agent){
      
      
      var index=0;
      KEY='';
       while(index<=request.body.queryResult.outputContexts.length-1)
      {
          console.log('Selection_Option_Handler->'+request.body.queryResult.outputContexts[index].name);
          if(request.body.queryResult.outputContexts[index].name.indexOf('actions_intent_option')>-1)
          {
              var KEY=request.body.queryResult.outputContexts[index].parameters.OPTION;
              console.log('Selection_Option_Handler->'+request.body.queryResult.outputContexts[index].parameters.OPTION);
              break;
          }
            
          index=index+1;
      }
      if(KEY=='Reservation')
        askArrivalDate(agent);
      else if(KEY=='Luxury' || KEY=='Premium'||KEY=='Studio' || KEY=='Royal Suite'||KEY=='Presidential Suite')
        giveFinalConfirmation(agent);
    else if (KEY=='Access Hotel Services')
        askForRoomNumber(agent);
    else if (KEY=='Offer1'||KEY=='Offer2')
    {
        dynaMessageHotelOffers='Offer Accepted.'
        hotelOffers(agent);
    }  
     else if (KEY=='Chinese')
    {
        chineseIntent(agent)
    } 
    else if(KEY=='Continental')
    {
         continentalIntent(agent);
    }
    else if(KEY=='Haka Noodle' || KEY=='Stir Fried Tofu with Rice' || KEY=='Date Pancakes' || KEY=='Hot and Sour Soup')
    {
        dynaMessageChinese='Order placed.'
        chineseIntent(agent)
    }
    else if(KEY=='SAFFRON SOUL' || KEY=='MEKONG' || KEY=='MYSTIQUE')
    {
        agent.add('Reservation made');
    }
    else if(KEY=='NEWS')
    {
        newsCategories(agent);
    }
    else if(KEY=='NDTV'||KEY=='Republic TV')
    {
        agent.add('Switching to '+KEY);
    }
        //agent.add('Offer Accepted');
      
  }
  
  function newsCategories(agent)
  {
       console.log('-->newsCategories<<-');
     // console.log('--->'+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);
     
            
agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Please tap on any option to switch to that channel"
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "NDTV"
              },
              "description": "",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/NDTV.jpg",
                "accessibilityText": "NDTV"
              },
              "title": "NDTV"
            },
            {
              "optionInfo": {
                "key": "Republic TV"
              },
              "description": "",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/Republic-TV.jpg",
                "accessibilityText": "Republic TV"
              },
              "title": "Republic TV"
            }
          ]
        }
      }
    }
  }));
  }
  
  
   function provideHotelServiceOptions(agent)
   {
       console.log('-->provideHotelServiceOptions<<-');
       
       let lastName=request.body.queryResult.parameters['lastName'];
       console.log(lastName)
       if(lastName===undefined)
            agent.add('Please select one of the Service options. You can say Home anytime to revisit these service options.');
        else
            agent.add('Hello Mr. '+lastName+', please select one of the Service options. You can say Home anytime to revisit these service options.');
            
       agent.context.set({
          name: 'guest-info',
          lifespan: 5,
          parameters:{'SOURCE':'','salutation': '', 'speaker': lastName,'CONTACTID':'','LOCATION':''}
    });
       
       
       //agent.add('Hello Mr. '+lastName+', you can choose from the below Service options.');
        agent.add(new Suggestion('Housekeeping'));
        agent.add(new Suggestion('Check Offers'));
        agent.add(new Suggestion('Explore Food'));
        agent.add(new Suggestion('Book a Cab'));
        agent.add(new Suggestion('TV'));
        agent.add(new Suggestion('City Information'));
        agent.add(new Suggestion('Book Gym or SPA'));
        agent.add(new Suggestion('Room Information'));
        agent.add(new Suggestion('Give feedback'));
   }
  
  
  function promiseFunc(path) {
    return new Promise(function(resolve, reject) {
        console.log('two');
     http.get({host: host, path: path}, (res) => {
      let body = ''; // var to store the response chunks
      res.on('data', (d) => { body += d;});
      res.on('error',(err) =>{
          console.log(err)
          reject(err);
          });// store each response chunk
      res.on('end', () => {
        console.log('BODY->'+body);
        extResponse = JSON.parse(body);
        resolve(extResponse);
      });
    });
}); 
    
}

function getContext()
{
     var index=0;
     while(index<=request.body.queryResult.outputContexts.length-1)
      {
          console.log('NAME->'+request.body.queryResult.outputContexts[index].name);
          if(request.body.queryResult.outputContexts[index].name.indexOf('guest-info')>-1)
            break;
          index=index+1;
      }
      return request.body.queryResult.outputContexts[index].parameters['speaker'];
}


 function getSourceAndPosition()
 {
     var index=0;
      //var size=request.body.queryResult.outputContexts.length;
      //console.log('SIZE->'+size);
      var strBody=JSON.stringify(request.body);
      console.log('HERE-->');
      console.log('ACTUAL REQUEST->'+strBody);
      if(strBody.indexOf('google_assistant_input_type_voice')>-1)
          source='GOOGLE_HOME';
      else if(strBody.indexOf('actions_capability_screen_output')>-1)
          source='GOOGLE_MOBILE';
          console.log('1->'+request.body.queryResult);
      while(index<=request.body.queryResult.outputContexts.length-1)
      {
          console.log('NAME->'+request.body.queryResult.outputContexts[index].name);
          if(request.body.queryResult.outputContexts[index].name.indexOf('guest-info')>-1)
            break;
          index=index+1;
      }
      position=index;
 }
 
  
  function welcomeMessageIntent(agent) {
     /*getSourceAndPosition();
     console.log('SOURCE->'+source);
     if(source=='GOOGLE_MOBILE') // fix for all mobiles
     {
         agent.add('Please identify yourself by providing your PIN');
     }
     else{
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CUSTOMER&LOCATION=&DEVICE=2';
      return promiseFunc(path).then(function(result){
          console.log('getWelcomeResponse->'+result);
          if(result.PIN == 'xxx')
            speech='Hello '+result.salutation+' '+result.speaker+', '+'How may I help you?'+' Also, if you want to use the Hotel conceirges on your mobile, you would have to set the PIN once by saying SET PIN';
          else
            speech='Hello '+result.salutation+' '+result.speaker+', '+'How may I help you?';
            //speech='Hello, How may I help you?';
          agent.setContext({
          name: 'guest-info',
          lifespan: 5,
          parameters:{'SOURCE':source,'salutation': result.salutation, 'speaker': result.speaker,'CONTACTID':result.CONTACTID,'LOCATION':result.LOCATION}
    });
         agent.add(speech);
     });
    }*/
    
    agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Please select from below options"
          }
        }
      ]
    },
    "systemIntent": {
      "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Access Hotel Services"
              },
              "description": "",
              "image": {
                "url": "http://www.neurosurg.cam.ac.uk/files/2017/09/yourstory_service_msme.jpg",
                "accessibilityText": "Access Hotel Services"
              },
              "title": "Access Hotel Services"
            },{
              "optionInfo": {
                "key": "Reservation"
              },
              "description": "",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/hotel.jpg",
                "accessibilityText": "Make Reservation"
              },
              "title": "Make Reservation"
            }
          ]
        }
      }
    }
  }));
    
    
  }
  
  function CityInfoIntent(agent) {
   /*   getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CITYINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('getCityInfo->'+result);
          
          
        // speech=result.response+'. Do you want me to email or text you this information?';
         //agent.add(speech);
     })*/
     
     
     
      agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Please select from below options"
          }
        }
      ]
    },
    "systemIntent": {
      "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "India gate"
              },
              "description": "",
              "image": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/India_Gate_in_New_Delhi_03-2016.jpg/230px-India_Gate_in_New_Delhi_03-2016.jpg",
                "accessibilityText": "India Gate"
              },
              "title": "India gate"
            },
             {
              "optionInfo": {
                "key": "Red fort"
              },
              "description": "",
              "image": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Red_Fort_Independence_Day.jpg/220px-Red_Fort_Independence_Day.jpg",
                "accessibilityText": "Red fort"
              },
              "title": "Red Fort"
            },
            {
              "optionInfo": {
                "key": "Jama Masjid"
              },
              "description": "",
              "image": {
                "url": "https://lonelyplanetimages.imgix.net/a/g/hi/t/c6e8881b27f038f983b0ff40154abbfc-jama-masjid.jpg",
                "accessibilityText": "Jama Masjid"
              },
              "title": "Jama Masjid"
            },
            {
              "optionInfo": {
                "key": "Lotus Temple"
              },
              "description": "",
              "image": {
                "url": "https://cdn1.goibibo.com/new-delhi-lotus-temple-14036146182-jpeg-l.jpg",
                "accessibilityText": "Lotus Temple"
              },
              "title": "Lotus Temple"
            }
          ]
        }
      }
    }
  }));
    
    
    
     
     
     
  }
  
    function GymOrSpaBooking(agent) {
   /*   getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CITYINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('getCityInfo->'+result);
          
          
        // speech=result.response+'. Do you want me to email or text you this information?';
         //agent.add(speech);
     })*/
     
     console.log("GYM AND SPA");
     
      agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Please select from below options"
          }
        }
      ]
    },
    "systemIntent": {
      "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Atlas - The Gym"
              },
              "description": "",
              "image": {
                "url": "http://www.marigoldhotels.com/images/atlas-big.jpg",
                "accessibilityText": "Atlas - The Gym"
              },
              "title": "Atlas - The Gym"
            },
             
            
            {
              "optionInfo": {
                "key": "Soul - Spa"
              },
              "description": "",
              "image": {
                "url": "http://www.marigoldhotels.com/images/soulspa-big.jpg",
                "accessibilityText": "Soul - Spa"
              },
              "title": "Soul - Spa"
            }
          ]
        }
      }
    }
  }));
    
    
    
     
     
     
  }
  
  
  
  
  
      function GymOrSpaBooking1(agent) {
   /*   getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CITYINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('getCityInfo->'+result);
          
          
        // speech=result.response+'. Do you want me to email or text you this information?';
         //agent.add(speech);
     })*/
     
     console.log("GYM AND SPA FINAL");
     
      agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Booking done"
          }
        }
      ]
    },
    "systemIntent": {
      "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Atlas - The Gym"
              },
              "description": "",
              "image": {
                "url": "http://www.marigoldhotels.com/images/atlas-big.jpg",
                "accessibilityText": "Atlas - The Gym"
              },
              "title": "Atlas - The Gym"
            },
             
            
            {
              "optionInfo": {
                "key": "Soul - Spa"
              },
              "description": "",
              "image": {
                "url": "http://www.marigoldhotels.com/images/soulspa-big.jpg",
                "accessibilityText": "Soul - Spa"
              },
              "title": "Soul - Spa"
            }
          ]
        }
      }
    }
  }));
    
    
    
     
     
     
  }
  
  
  function EmailIntent(agent) {
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=EMAILCITYINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('EmailIntent->'+result);
         speech=result.response;
         agent.add(speech);
     })
  }
  function RoomInfoIntent(agent) {
    /*  getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=ROOMINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('RoomInfoIntent->'+result);
         speech=result.response;
         agent.add(speech);
     })*/
     
     
     
     agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": " Your Room Contains Free Wifi, Satellite TV with free SPA booking. Feel Like upgrading Your Room? Tap on any of the upgrade options. "
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Royal Suite"
              },
              "description": "Spa, Satellite Tv, Extra Space - INR 11,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/suite1.jpg",
                "accessibilityText": "Royal Suite"
              },
              "title": "Royal Suite"
            },{
              "optionInfo": {
                "key": "Presidential Suite"
              },
              "description": "Spa, Gym, Satellite Tv with all channels, Extra Space - INR 21,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/presidential1.jpg",
                "accessibilityText": "Presidential Suite"
              },
              "title": "Presidential Suite"
            }
          ]
        }
      }
    }
  }));
  
  
  }
  
  
  
  
  
    function RoomInfoIntent1(agent) {
    /*  getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=ROOMINFO&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('RoomInfoIntent->'+result);
         speech=result.response;
         agent.add(speech);
     })*/
     
     
     
     agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": " Upgrading Process Initiated. Our executive will be in touch with you soon."
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Royal Suite"
              },
              "description": "Spa, Satellite Tv, Extra Space - INR 11,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/suite1.jpg",
                "accessibilityText": "Royal Suite"
              },
              "title": "Royal Suite"
            },{
              "optionInfo": {
                "key": "Presidential Suite"
              },
              "description": "Spa, Gym, Satellite Tv with all channels, Extra Space - INR 21,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/presidential1.jpg",
                "accessibilityText": "Presidential Suite"
              },
              "title": "Presidential Suite"
            }
          ]
        }
      }
    }
  }));
  
  
  }
  
  
  
  
  function SpecialOffersIntent(agent) {
        getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=SPECIALOFFERS&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('SpecialOffersIntent->'+result);
         speech=result.response;
         agent.add(speech);
     })
  }
  
 /*function GymIntent(agent) {
      speech='Due to heavy booking, only an 8 PM slot is available for tomorrow. Shall I book that one for you?';
      agent.add(speech);
     
  }*/
  function GymConfirmationIntent(agent) {
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('getCityInfo+START->'+contactId);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CONFIRMGYM&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('GymConfirmationIntent->'+result);
         speech=result.response+' '+request.body.queryResult.outputContexts[position].parameters['salutation']+' '+request.body.queryResult.outputContexts[position].parameters['speaker'];
         agent.add(speech);
     })
  }
  function HouseKeepingIntent(agent) {
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      let requestMsg=request.body.queryResult.parameters['housekeepingItems'];
      console.log('HouseKeepingIntent+START->'+requestMsg);
      let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=HOUSEKEEPING&CONTACTID='+contactId+'&MESSAGE='+requestMsg);
      console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
          console.log('HouseKeepingIntent->'+result);
         speech=result.response;
         agent.add(speech);
     })
  }
function CancelGymBookingIntent(agent) {
    getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //console.log('CancelGymBookingIntent+START->'+requestMsg);
      let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=CANCELGYM&CONTACTID='+contactId);
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('CancelGymBookingIntent->'+result);
         speech=result.response+' '+request.body.queryResult.outputContexts[position].parameters['salutation']+' '+request.body.queryResult.outputContexts[position].parameters['speaker'];
         agent.add(speech);
     })
  }
  function ExtendStayIntent(agent) {
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      let requestedDuration=request.body.queryResult.parameters['extension_duration'].amount;
      console.log('ExtendStayIntent+START->'+requestedDuration);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=EXTENDSTAY&CONTACTID='+contactId+'&DAYS='+requestedDuration;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('ExtendStayIntent->'+result);
         speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
         agent.add(speech);
     })
  }
  function ExtendStayIntent(agent) {
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      let requestedDuration=request.body.queryResult.parameters['extension_duration'].amount;
      console.log('ExtendStayIntent+START->'+requestedDuration);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=EXTENDSTAY&CONTACTID='+contactId+'&DAYS='+requestedDuration;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('RestaturantBookingIntent->'+result);
         speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
         agent.add(speech);
     })
  }
  
  
function InRoomDiningMenuIntent(agent) {
    getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      //let requestedDuration=request.body.queryResult.parameters['extension_duration'].amount;
      //console.log('InRoomDiningMenuIntent+START->'+requestedDuration);
      let path = '/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=RECOMMENDATIONS&CONTACTID='+contactId;
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('InRoomDiningMenuIntent->'+result);
         speech=result.response+'. The Restaurant options are Mekong, Saffron Soul and Mystique. Which one would you prefer for In Room dining?';//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
         agent.add(speech);
     })
  }
function FeedbackIntent(agent) {
    getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      let feedback=request.body.queryResult.queryText;
      //console.log('CancelGymBookingIntent+START->'+requestMsg);
      let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=FEEDBACK&CONTACTID='+contactId+'&FEEDBACKTEXT='+feedback);
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('FeedbackIntent->'+result);
         speech=result.response+' '+request.body.queryResult.outputContexts[position].parameters['salutation']+' '+request.body.queryResult.outputContexts[position].parameters['speaker'];
         agent.add(speech);
     })
  }
function continentalIntent(agent) {
    getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
      let order=request.body.queryResult.queryText;
      //console.log('CancelGymBookingIntent+START->'+requestMsg);
      let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=PLACEORDER&CONTACTID='+contactId+'&ORDER='+order);
      //console.log('PATH->'+path);
      return promiseFunc(path).then(function(result){
         console.log('continentalIntent->'+result);
         speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
         agent.add(speech);
     })
  }
  function setPINIntent(agent) {
      getSourceAndPosition();
      source=request.body.queryResult.outputContexts[position].parameters['SOURCE'];
      console.log('SOURCEPIN->'+source);
      if(source=='GOOGLE_MOBILE')
        agent.add('Sorry, but you need to set your PIN from the Google Home device placed in your Hotel Room');
      else{
          let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
          let PIN=request.body.queryResult.parameters['PIN'];
          console.log('PIN->'+PIN);
          //console.log('CancelGymBookingIntent+START->'+requestMsg);
          let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=SETPIN&CONTACTID='+contactId+'&PIN='+PIN);
          //console.log('PATH->'+path);
          return promiseFunc(path).then(function(result){
             console.log('setPINIntent->'+result);
             speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
             agent.add(speech);
             })
        }
  }
 
function IdentifyMeIntent(agent) {
      getSourceAndPosition();
      source=request.body.queryResult.outputContexts[position].parameters['SOURCE'];
      console.log('SOURCEPIN->'+source);
          let PIN=request.body.queryResult.queryText;
          console.log('PIN->'+PIN);
          //console.log('CancelGymBookingIntent+START->'+requestMsg);
          let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=IDENTIFYME&PIN='+PIN);
          //console.log('PATH->'+path);
          return promiseFunc(path).then(function(result){
             console.log('IdentifyMeIntent->'+result);
             //speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
             if(result.isSuccess=='TRUE'){
             //speech='Hello '+result.salutation+' '+result.speaker+', '+'How may I help you?';
             speech='Hello '+result.salutation+' '+result.speaker+', '+'How may I help you?';
             agent.setContext({
                    name: 'guest-info',
                    lifespan: 5,
                    parameters:{'SOURCE':source,'salutation': result.salutation, 'speaker': result.speaker,'CONTACTID':result.CONTACTID,'LOCATION':result.LOCATION}
            })
            }
            else
                speech=' I am sorry but I have not been able to identify you.If you may want to try again, just state your PIN again';
             agent.add(speech);
        })
        
  }  
  function MenuChoiceHandlerIntent(agent) {
      console.log('Menu Intent->');
      
    /*  console.log("MENU REQUEST-->"+JSON.stringify(request.body));
      console.log('--->'+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);
      getSourceAndPosition();
      let contactId=request.body.queryResult.outputContexts[position].parameters['CONTACTID'];
         // let food=request.body.queryResult.parameters['foodChoice'];
          //console.log('FOOD->'+food);
          //console.log('CancelGymBookingIntent+START->'+requestMsg);
          let path = encodeURI('/MobileRequestPageHandler?PARTNER=GOOGLE&SERVICE=PLACEORDER&CONTACTID='+contactId+'&ORDER='+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);
          //console.log('PATH->'+path);
          return promiseFunc(path).then(function(result){
             console.log('foodChoice->'+result);
             speech=result.response;//+' '+request.body.queryResult.outputContexts[1].parameters['salutation']+' '+request.body.queryResult.outputContexts[1].parameters['speaker'];
             agent.add(speech);
             })*/
             agent.add('Order Placed. Please expect to be delivered in 15-20 minutes');
             
             
  }
function restaurantBooking(agent) {
      console.log('-->restaurantBooking<<-');
     // console.log('--->'+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);
     
            
agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Which Restaurant?"
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "SAFFRON SOUL"
              },
              "description": "World Cafe",
              "image": {
                "url": "http://www.marigoldhotels.com/images/saffron_big.jpg",
                "accessibilityText": "SAFFRON SOUL"
              },
              "title": "SAFFRON SOUL"
            },
            {
              "optionInfo": {
                "key": "MEKONG"
              },
              "description": "PAN ASIAN SPECIALITY",
              "image": {
                "url": "http://www.marigoldhotels.com/images/mekon_big.jpg",
                "accessibilityText": "MEKONG"
              },
              "title": "MEKONG"
            },
            {
              "optionInfo": {
                "key": "MYSTIQUE"
              },
              "description": "LOUNGE",
              "image": {
                "url": "http://www.marigoldhotels.com/images/mystique_big.jpg",
                "accessibilityText": "MYSTIQUE"
              },
              "title": "MYSTIQUE"
            }
          
          ]
        }
      }
    }
  }));
  }
  function TV_NEWSCategoryIntent(agent) {
      console.log('HERE->  News category');
      //console.log('--->'+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);

  
  
  
  
  
  // NEWS STARTED
  
  
  



  }
  
  
  
  function chineseIntent(agent) {
      
      console.log('-->chineseIntent<<-');
      if(dynaMessageChinese==='')
        dynaMessageChinese='Tap on the dishes to place order'
    
      //console.log('--->'+request.body.originalDetectIntentRequest.payload.inputs[0].arguments[0].textValue);
      


agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": dynaMessageChinese
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Haka Noodle"
              },
              "description": "INR 500",
              "image": {
                "url": "https://i0.wp.com/mypullzone.9vexd6dl53at.maxcdn-edge.com/wp-content/uploads/2017/03/veg-hakka-noodles-recipe-with-step-by-step-instructions.jpg",
                "accessibilityText": "Haka Noodle"
              },
              "title": "Haka Noodle"
            },
            {
              "optionInfo": {
                "key": "Stir Fried Tofu with Rice"
              },
              "description": "INR 600",
              "image": {
                "url": "https://i.ndtvimg.com/i/2016-06/tofu-with-rice_625x350_81466070125.jpg",
                "accessibilityText": "Stir Fried Tofu with Rice"
              },
              "title": "Stir Fried Tofu with Rice"
            },
            {
              "optionInfo": {
                "key": "Date Pancakes"
              },
              "description": "INR 300",
              "image": {
                "url": "https://i.ndtvimg.com/i/2015-02/date-pancake_625x350_61424325124.jpg",
                "accessibilityText": "Date Pancakes"
              },
              "title": "Date Pancakes"
            },
            {
              "optionInfo": {
                "key": "Hot and Sour Soup"
              },
              "description": "INR 250",
              "image": {
                "url": "https://i.ndtvimg.com/i/2016-06/soup-625_625x350_81466064298.jpg",
                "accessibilityText": "Hot and Sour Soup"
              },
              "title": "Hot and Sour Soup"
            },
          ]
        }
      }
    }
  }));
     
   


  }
 
 

  
  
  
  
  
  
  
  
  
  function askArrivalDate(agent)
  {
      console.log('-->askArrivalDate<<-');
      agent.add('Arrival Date?');
  }
  
  
  function gotReservationDates(agent)
  {
      
      console.log('-->gotReservationDates<<-');
      makeMyReservationIntent(agent);
  }
  
  function askForRoomNumber(agent)
  {
        console.log('-->askForRoomNumber<<-');
        agent.add('Your Room Number?');
  }
  function bookaCabIntent(agent)
  {
      console.log('-->Cab booking conformation<<-');
      // const conv = agent.conv();
      // conv.close = 'The pickup has been arranged as requested.'
      // agent.add(conv);

      agent.add('The pickup has been arranged as requested.')
  }
  function askForLastName(agent)
  {
        console.log('-->askForRoomNumber<<-');
        
        agent.add('Your Last Name?');
  }
  
  function hotelOffers(agent)
  {
     agent.add(new Suggestion('Access Hotel Services'));
     if(dynaMessageHotelOffers==='')
     dynaMessageHotelOffers='We currently have 2 offers running. Please tap on one or more of them to accept the offer.';
     console.log('-->hotelOffers<<-'+dynaMessageHotelOffers);
    
     agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": dynaMessageHotelOffers
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Offer1"
              },
              "description": "11am - 4pm",
              "image": {
                "url": "http://www.marigoldhotels.com/images/sunday-brunch-inner.jpg",
                "accessibilityText": "The Lazy Sunday Brunch at Mekong"
              },
              "title": "The Lazy Sunday Brunch at Mekong"
            },
            {
              "optionInfo": {
                "key": "Offer2"
              },
              "description": "12pm - 2pm",
              "image": {
                "url": "http://www.marigoldhotels.com/images/soulspa-big.jpg",
                "accessibilityText": "Premium"
              },
              "title": "Free SPA session"
            },
            
          ]
        }
      }
    }
  }));
  agent.add(new Suggestion('Access Hotel Services'));
  }
  
  function makeMyReservationIntent(agent) {
      console.log('-->makeMyReservationIntent<<-');
  

    agent.add(new Payload(agent.ACTIONS_ON_GOOGLE,   {
    "expectUserResponse": true,
    "richResponse": {
      "items": [
        {
          "simpleResponse": {
            "textToSpeech": "Please select a Room Type"
          }
        }
      ]
    },
    "systemIntent": {
         "intent": "actions.intent.OPTION",
      "data": {
        "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
        "carouselSelect": {
          "items": [
            {
              "optionInfo": {
                "key": "Luxury"
              },
              "description": "INR 5,225 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/luxury1.jpg",
                "accessibilityText": "Luxury"
              },
              "title": "Luxury"
            },
            {
              "optionInfo": {
                "key": "Premium"
              },
              "description": "INR 5,995 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/premium1.jpg",
                "accessibilityText": "Premium"
              },
              "title": "Premium"
            },
            {
              "optionInfo": {
                "key": "Studio"
              },
              "description": "INR 7,535 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/studio1.jpg",
                "accessibilityText": "Studio"
              },
              "title": "Studio"
            },
            {
              "optionInfo": {
                "key": "Royal Suite"
              },
              "description": "INR 11,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/suite1.jpg",
                "accessibilityText": "Royal Suite"
              },
              "title": "Royal Suite"
            },{
              "optionInfo": {
                "key": "Presidential Suite"
              },
              "description": "INR 21,850 / Night",
              "image": {
                "url": "https://s3.amazonaws.com/hotelgreenpark/room/presidential1.jpg",
                "accessibilityText": "Presidential Suite"
              },
              "title": "Presidential"
            }
          ]
        }
      }
    }
  }));
  

/*else if(KEY=='Presidential')
{
    agent.add('Thanks for the details. Please check your gmail for completing payment. Have a nice day');
}

else if (KEY=='Access Hotel Services')
{
    agent.add('Hello There , How can I help you?.');
       agent.add(new Suggestion('Special Offers'));
    agent.add(new Suggestion('Explore Food'));
        agent.add(new Suggestion('Cab booking'));
    agent.add(new Suggestion('TV Menu'));
     agent.add(new Suggestion('City Information');
      agent.add(new Suggestion('Gym or Spa Booking'));
     agent.add(new Suggestion('Room Info'));
   
    
    agent.add(new Suggestion('Suggestions/Feedback'));
}
//agent.setContext({ name: 'Presidential', lifespan: 5, parameters: { city: 'Rome' }});*/
  }
 
 
 
 
   
  
  
 function giveFinalConfirmation(agent)
 {
    let conv = agent.conv();
    console.log('conv object is: ',conv)
    conv.close('Thanks for the details. Please check your gmail for completing payment. Have a nice day');
    agent.add(conv);
 }

  let intentMap = new Map(); // Map functions to Dialogflow intent names
  intentMap.set('welcomeMessageIntent', welcomeMessageIntent);
  intentMap.set('CityInfoIntent', CityInfoIntent);
  intentMap.set('EmailIntent', EmailIntent);
  intentMap.set('RoomInfoIntent', RoomInfoIntent);
  intentMap.set('SpecialOffersIntent', SpecialOffersIntent);
  //intentMap.set('GymIntent', GymIntent);
  intentMap.set('GymConfirmationIntent', GymConfirmationIntent);
  intentMap.set('HouseKeepingIntent', HouseKeepingIntent);
  intentMap.set('CancelGymBookingIntent', CancelGymBookingIntent);
  intentMap.set('ExtendStayIntent', ExtendStayIntent);
  intentMap.set('InRoomDiningMenuIntent', InRoomDiningMenuIntent);
  intentMap.set('inRoomdiningIntent', InRoomDiningMenuIntent);
  intentMap.set('FeedbackIntent', FeedbackIntent);
  intentMap.set('continentalIntent', continentalIntent);
  intentMap.set('setPINIntent', setPINIntent);
  intentMap.set('IdentifyMeIntent', IdentifyMeIntent);
  intentMap.set('ChineseIntent - custom', MenuChoiceHandlerIntent);
  intentMap.set('ContinentalIntent - custom', MenuChoiceHandlerIntent);
  intentMap.set('RestaurantBooking - custom', restaurantBooking);
  intentMap.set('TV_NEWSCategoryIntent', newsCategories);
  intentMap.set('MakeMyReservationIntent', askArrivalDate);
  intentMap.set('TomorrowIntent', gotReservationDates);
  intentMap.set('PresidentialSuiteIntent', giveFinalConfirmation);
  intentMap.set('RegisterUserIntent', askForRoomNumber);
  intentMap.set('RoomNumberIntent', askForLastName);
  intentMap.set('LastNameIntent', provideHotelServiceOptions);
  intentMap.set('HotelOffersIntent', hotelOffers);
  intentMap.set('HomeIntent', provideHotelServiceOptions);
  intentMap.set('ChineseIntent', chineseIntent);
  intentMap.set('RestaurantBookingIntent', restaurantBooking);
  intentMap.set('RoomInfoIntent - custom', RoomInfoIntent1);
  intentMap.set('Gym_or_spa_Booking', GymOrSpaBooking); 
  intentMap.set('Gym_or_spa_Booking___custom', GymOrSpaBooking1);
  //intentMap.set('ChineseIntent', ChineseIntent);
  intentMap.set('Selection_Option_Handler', Selection_Option_Handler);
  intentMap.set('BookaCabIntent', bookaCabIntent);
  //intentMap.set('ChineseIntent', WalkInStatusIntent);
  //intentMap.set('Default Fallback Intent', fallback);
  agent.handleRequest(intentMap);
});