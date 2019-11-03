## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## get weather
* get_weather
- action_get_weather

## my name is
* my_name_is
- utter_its_nice_to_meet_you

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Generated Story 3320800183399695936
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "uk"}
    - slot{"location": "uk"}
    - action_get_weather
    - slot{"location": "uk"}
* goodbye
    - utter_goodbye
    - export

## bot challenge
* enquire_greet
    - utter_mood_great

## weather
* greet
    - utter_greet
* inform[location=London]
    - slot{"location": "London"}
    - action_get_weather
* goodbye
    - utter_goodbye
    - export