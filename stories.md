
## Greet
* greet
    - utter_greet

## Thanks
* thanks
    - utter_np
    - utter_anymore

## Goodbye
* goodbye
    - utter_goodbye
    - utter_smiley

## Path 1
* greet
    - utter_greet
* location_check{"startup":"Zepo"}
    - action_check_location
    - action_restart


## Path 2
* greet
    - utter_greet
* fundingType_check{"startup":"VDeliver"}
    - action_check_fundingType
    - action_restart


## Path 3
* fundingStatus_city{"fundingType": "Seed Funding","city": "Bangalore"}
    - action_check_NoOfStartups
    - action_restart


## Path 4
* fundingStatus_city{"fundingType": "Seed Funding"}
    - utter_what_city
* inform{"city": "Bangalore"}
    - action_check_NoOfStartups
    - action_restart

## Path 5
* fundingStatus_city{"city": "Bangalore"}
    - utter_what_fundingType
* inform{"fundingType": "Seed Funding"}
    - action_check_NoOfStartups
    - action_restart

## Path 6
* AvgFunding_query{"fundingType": "Seed Funding","city": "Bangalore","year":"2017"}
    - action_check_avgFunding
    - action_restart

## Path 7
* AvgFunding_query{"city": "Bangalore"}
    - utter_what_fundingType
* inform{"fundingType": "Seed Funding"}
    - utter_which_year
* inform{"year":"2017"}
    - action_check_avgFunding
    - action_restart   

## Path 8
* AvgFunding_query{"fundingType": "Seed Funding"}
    - utter_what_city
* inform{"city": "Bangalore"}
    - utter_which_year
* inform{"year":"2017"}
    - action_check_avgFunding
    - action_restart    

## Path 9
* AvgFunding_query{"year":"2017","city": "Bangalore" }
    - utter_what_fundingType
* inform{"fundingType": "Seed Funding"}
    - action_check_avgFunding
    - action_restart   

## Path 10
* AvgFunding_query{"year":"2017"}
    - utter_what_fundingType
* inform{"fundingType": "Seed Funding"}
    - utter_what_city
* inform{"city": "Bangalore"}
    - action_check_avgFunding
    - action_restart  
        
## Path 11
* AvgFunding_query
    - utter_which_year
* inform{"year":"2017"}
    - utter_what_fundingType
* inform{"fundingType": "Seed Funding"}
    - utter_what_city
* inform{"city": "Bangalore"}
    - action_check_avgFunding
    - action_restart   


