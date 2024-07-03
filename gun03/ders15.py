yemekler = {"çorbalar":{"etli": ["işkembe", "kelle paça", "tavuk suyu"],
                         "etsiz": ["mercimek", "ezo gelin"],
                         "sebze": ["domates", "brokoli"]},
           "Kebaplar": {"acılı": ["adana", "beyti"],
                        "acısız": ["urfa","mardin"],
                        "dürümler":["ciger","adana"]},
            "icecek":"çay"
            }
print(yemekler["çorbalar"]["etli"][0])
yemekler["çorbalar"]["etli"].append("bayma çorbası")
sutlu_tatlilar = ["sütlaç"]
yemekler["tatlilar"] = {"sütlü":sutlu_tatlilar}
for menubasligi in yemekler:
    print(menubasligi)
    if type(yemekler[menubasligi]) is dict:
        for altmenu in yemekler[menubasligi]:
            print("\t",altmenu)
            for yemek in yemekler[menubasligi][altmenu]:
                print("\t\t",yemek)
    else:
        print(yemekler[menubasligi])
