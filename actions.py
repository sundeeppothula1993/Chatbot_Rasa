from rasa_core_sdk import Action

import pandas as pd
import requests

data = pd.read_csv("startup_funding.csv")

class LocationCheck(Action):

    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):
        startup = tracker.get_slot('startup')
        try:
            ## Extract data from dataset containing the Startup Information user mentioned.
            results_location = data[data.StartupName.str.lower() == startup.lower()]
            ## If a startup received multiple fundings (since they will have same location so we are taking only one entry)
            city_name = list(set(results_location.CityLocation))[0]
            ## ## dispatching thecity location for startup
            dispatcher.utter_message("{} is in the city {}".format(startup, city_name))
        except:
            ## exception given when errors occur due to particular entity not found in the query
            dispatcher.utter_message("Sorry! I dont have information about that.")

class FundingType_query(Action):

    def name(self):
        return "action_check_fundingType"

    def run(self, dispatcher, tracker, domain):
        startup = tracker.get_slot('startup')
        try:
            ## Extract data from dataset containing the Startup Information user mentioned.
            results_location = data[data.StartupName.str.lower() == startup.lower()]
            ## If a startup received multiple fundings (since they will have same location so we are taking only one entry)
            funding_type = list(set(results_location.InvestmentType))[0]
            funding_year = list(set(results_location.Year))[0]
            ## dispatching the type of funding received message with latest year in which it got funding
            dispatcher.utter_message("{} received {} type investment in the year {}".format(startup, funding_type, funding_year))
        except:
            dispatcher.utter_message("Sorry! I dont have information about that.")


class StartupsInCity(Action):
    def name(self):
        return "action_check_NoOfStartups"

    def run(self, dispatcher, tracker, domain):
        fundingType = tracker.get_slot('fundingType')
        city = tracker.get_slot('city')
        ## Extract data from dataset containing the city user mentioned.
        city_results = data[data.CityLocation.str.lower() == city.lower()]
         ## Extract data from the above screened dataa conating the type of funding user queryed
        results = city_results[city_results.InvestmentType.str.lower() == fundingType.lower()]
        ## Calculate the number of data entries in this final screened data and returning the message
        dispatcher.utter_message("Number of Startups receiving {} type investment in the  {} city is {}!".format(fundingType, city, len(results)))


class AverageFundingCalculation(Action):
    def name(self):
        return "action_check_avgFunding"

    def run(self, dispatcher, tracker, domain):
        fundingType = tracker.get_slot('fundingType')
        city = tracker.get_slot('city')
        year = tracker.get_slot('year')
        try:
            ## Extract data from dataset containing the city user mentioned.
            city_results = data[data.CityLocation.str.lower() == city.lower()]
            ## Extract data from the above screened data for the type of funding user mentioned.
            funding_results = city_results[city_results.InvestmentType.str.lower() == fundingType.lower()]
            ## Extract data from the above screened data for the user mentioned year
            final_list = funding_results[funding_results.Year == int(year)]
            ## Dropping all rows which dont have funding amounts
            final_list = (final_list.AmountInUSD.dropna())
             ## Calculate the stats for the funding amount for the above screened data and dispatch the result
            dispatcher.utter_message("This is the Overall Statistics of {} investment received by startups in the {} city in {} is:- Median funding amount is {} USD & Average funding amount is {} USD & Maximum funding amount is {} USD".format(fundingType, city, year, final_list.median(),fundingType,final_list.mean(),final_list.max()))
        except:
            ## exception given when errors occur due to particular entity not found in the query
            dispatcher.utter_message("Sorry! I dont have information about that.")
