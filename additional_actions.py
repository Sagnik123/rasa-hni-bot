def create_config_url(features):
    
    base_url = "https://www.allsteeloffice.com/configurator/"
    # product- evo-task-chair
    # config-  47c8ba7b-d8fb-48fa-9bda-50b07e13f422
    # productFamily- evo
    # sku - DWW-MHWNO.BLK.C.L.2.BLK.B.APX13.TC00
    sku_mapping = {
            "evo_arms_adjustable": "EAA",
            "evo_cylinder_twice": "EC",
            "evo_lumbar_L": "EL",
            "evo_frameColor_Clay": "EVF",
            "evo_meshColor_Dusk": "EVMD",
            "evo_baseColor_Black": "EBC",
            "evo_casterType_H": "ECTH"
        }
    # for feature in features.values():
    url = "https://www.allsteeloffice.com/configurator/evo-task-chair?config=47c8ba7b-d8fb-48fa-9bda-50b07e13f422&productFamily=evo&sku=DWW-MHWNO.BLK.C.L.2.BLK.B.APX13.TC00"
    return url