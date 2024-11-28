# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from additional_actions import create_config_url

class ActionShowChairFeatures(Action):

    def name(self) -> str:
        return "action_product_chair_family_evo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        features = [
            ("Arms", "evo_arms_adjustable"),
            ("Cylinder", "evo_cylinder_twice"),
            ("Lumbar", "evo_lumbar_L"),
            # ("Frame Color", "evo_frameColor_Clay"),
            ("Mesh Color", "evo_meshColor_Dusk"),
            ("Base Color", "evo_baseColor_Black"),
            # ("Caster Type", "evo_casterType_H")
        ]

        # Get the current selected features or initialize as an empty list if not set
        selected_features = tracker.get_slot("selected_features") or []
        print("Selected features before update:", selected_features)

        # Get the latest feature selected by the user
        latest_feature = tracker.latest_message['intent']['name']
        print("Latest feature intent:", latest_feature)

        # Check if the latest feature is valid and not already selected
        if latest_feature in [feature[1] for feature in features] and latest_feature not in selected_features:
            selected_features.append(latest_feature)
        print("Selected features after update:", selected_features)

        # Filter out the already selected features to get the remaining available features
        available_features = [feature for feature in features if feature[1] not in selected_features]
        print("Available features:", available_features)

        # Generate buttons for the remaining available features
        buttons = [{"title": feature[0], "payload": f"/{feature[1]}"} for feature in available_features]

        # Respond with the remaining available features or a message indicating no more features to select
        if buttons:
            dispatcher.utter_message(text="Here are the next product features to choose:", buttons=buttons)
        else:
            url = create_config_url(available_features)
            dispatcher.utter_message(text=f'Config url for the product: <a href="{url}" target="_blank">{url}</a>')
            # dispatcher.utter_message(text=f"Config url for the product: {url}")
            # dispatcher.utter_message(text="No more features to select.")

        # Update the slot with the selected features
        # if [ f for f in available_features] == selected_features:
        #     url = create_config_url(available_features)
        #     dispatcher.utter_message(text=f"Config url for the product: {url}")
        return [SlotSet("selected_features", selected_features)]


class ActionSetSKUonArms(Action):
    def name(self):
        return "action_set_sku_on_arms"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_arms_adjustable":
            dispatcher.utter_message(text="You have selected: 4D adjustable arms")
            return [SlotSet("evo_arms", "evo_arms_adjustable")]
       
        return []
    
class ActionSetSKUonCylinder(Action):
    def name(self):
        return "action_set_sku_on_cylinder"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_cylinder_twice":
            dispatcher.utter_message(text="You have selected: 2 cylinders")
            return [SlotSet("evo_cylinder", "evo_cylinder_twice")]
       
        return []
    
class ActionSetSKUonLumbar(Action):
    def name(self):
        return "action_set_sku_on_lumbar"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_lumbar_L":
            dispatcher.utter_message(text="You have selected: L lumbar")
            return [SlotSet("evo_lumbar", "evo_lumbar_L")]
       
        return []
class ActionSetSKUonFrameColor(Action):
    def name(self):
        return "action_set_sku_on_frameColor"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_frameColor_Black":
            dispatcher.utter_message(text="You have selected: black frame color")
            return [SlotSet("evo_frameColor", "evo_frameColor_Black")]
       
        return []
    
class ActionSetSKUonMeshColor(Action):
    def name(self):
        return "action_set_sku_on_meshColor"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_meshColor_Dusk":
            dispatcher.utter_message(text="You have selected: Dusk mesh color")
            return [SlotSet("evo_meshColor", "evo_meshColor_Dusk")]
       
        return []
    
class ActionSetSKUonBaseColor(Action):
    def name(self):
        return "action_set_sku_on_baseColor"

    def run(self, dispatcher, tracker, domain):
        
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_baseColor_Black":
            dispatcher.utter_message(text="You have selected: black base color")
            return [SlotSet("evo_baseColor", "evo_baseColor_Black")]
       
        return []
    
class ActionSetSKUonCasterType(Action):
    def name(self):
        return "action_set_sku_on_caster_type"

    def run(self, dispatcher, tracker, domain):
       
        intent = tracker.latest_message["intent"].get("name")

        if intent == "evo_casterType_H":
            dispatcher.utter_message(text="You have selected: H caster type")
            return [SlotSet("evo_caster_type", "evo_casterType_H")]
       
        return []
