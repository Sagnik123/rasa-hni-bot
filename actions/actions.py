from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from sanic import Sanic
from sanic.response import file
from additional_actions import create_config_url

app = Sanic("custom_action_server")

# Serve the static assets folder
@app.route('/assets/<filename>')
async def serve_file(request, filename):
    return await file(f'./assets/{filename}')

class ActionShowImage(Action):
    def name(self) -> Text:
        return "action_show_image"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Here's an image for you!",
            image="https://cdn.photographylife.com/wp-content/uploads/2014/09/Nikon-D750-Image-Samples-2.jpg"
        )
        return []

class ActionShowPdf(Action):
    def name(self) -> Text:
        return "action_show_pdf"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Here's the PDF document you requested:",
            custom={"payload": "pdf_attachment", "title": "PDF Title", "url": "https://ptgmedia.pearsoncmg.com/images/9780133387520/samplepages/0133387526.pdf"}
        )
        return []

class ActionShowVideo(Action):
    def name(self) -> Text:
        return "action_show_video"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Here's the YouTube video you requested:",
            attachment= { "type":"video", "payload":{ "src": "https://youtube.com/embed/9C1Km6xfdMA" }}
        )
        return []

class ActionShowChairFeatures(Action):

    def name(self) -> str:
        return "action_product_chair_family_evo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        features = [
            ("Arms", "evo_arms_adjustable"),
            ("Cylinder", "evo_cylinder_twice"),
            ("Lumbar", "evo_lumbar_L"),
            ("Mesh Color", "evo_meshColor_Dusk"),
        ]

        selected_features = tracker.get_slot("selected_features") or []
        latest_feature = tracker.latest_message['intent']['name']

        if latest_feature in [feature[1] for feature in features] and latest_feature not in selected_features:
            selected_features.append(latest_feature)

        available_features = [feature for feature in features if feature[1] not in selected_features]

        buttons = [{"title": feature[0], "payload": f"/{feature[1]}"} for feature in available_features]

        if buttons:
            dispatcher.utter_message(text="Here are the next product features to choose:", buttons=buttons)
        else:
            url = create_config_url(selected_features)
            dispatcher.utter_message(text=f'Config url for the product: <a href="{url}" target="_blank">{url}</a>')

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
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5055)
