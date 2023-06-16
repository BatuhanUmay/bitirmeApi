from flask import Flask, request
import pickle
import numpy as np
import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v1/arabam', methods=["GET", 'POST'])
def calculate_arabam():
    args = request.args
    brand = args["brand"],
    series = args["series"],
    model = args["model"],
    productionYear = args["productionYear"],
    mileage = args["mileage"],
    gearbox = args["gearbox"],
    fuelType = args["fuelType"],
    bodyType = args["bodyType"],
    engineSize = args["engineSize"],
    enginePower = args["enginePower"],
    drivetrain = args["drivetrain"],
    fuelEfficiency = args["fuelEfficiency"],
    fuelTank = args["fuelTank"],
    replacedParts = args["replacedParts"],
    exchange = args["exchange"],
    yas = args["yas"]

    print(args)
    print(brand)

    dict_Marka = {'Audi': 0, 'BMW': 1, 'Chevrolet': 2, 'Citroen': 3, 'DS Automobiles': 4, 'Dacia': 5, 'Fiat': 6,
                  'Ford': 7, 'Honda': 8, 'Hyundai': 9, 'Kia': 10, 'MINI': 11, 'Mazda': 12, 'Mercedes - Benz': 13,
                  'Mitsubishi': 14, 'Nissan': 15, 'Opel': 16, 'Peugeot': 17, 'Renault': 18, 'Seat': 19, 'Skoda': 20,
                  'Suzuki': 21, 'Tofaş': 22, 'Toyota': 23, 'Volkswagen': 24, 'Volvo': 25}
    dict_Seri = {'1 Serisi': 0, '206': 1, '206+': 2, '207': 3, '208': 4, '3': 5, '3 Serisi': 6, '301': 7, '307': 8,
                 '308': 9, '407': 10, '5 Serisi': 11, '508': 12, 'A': 13, 'A3': 14, 'A4': 15, 'Accent': 16,
                 'Accent Blue': 17, 'Accent Era': 18,
                 'Albea': 19, 'Astra': 20, 'Auris': 21, 'Avensis': 22, 'Bora': 23, 'Brava': 24, 'C': 25,
                 'C-Elysee': 26, 'C-Max': 27, 'C3': 28, 'C3 Picasso': 29, 'C4': 30, 'C4 Picasso': 31, 'CLA': 32,
                 'Carisma': 33, 'Ceed': 34, 'City': 35, 'Civi\
    c': 36, 'Clio': 37, 'Cooper': 38, 'Cordoba': 39, 'Corolla': 40, 'Corsa': 41, 'Cruze': 42, 'DS3': 43,
                 'Doğan': 44, 'E': 45, 'Egea': 46, 'Elantra': 47, 'Escort': 48, 'Felicia': 49, 'Fiesta': 50,
                 'Fluence': 51, 'Focus': 52, 'Fusion\
    ': 53, 'Getz': 54, 'Golf': 55, 'Ibiza': 56, 'Insignia': 57, 'Jazz': 58, 'Jetta': 59, 'Kartal': 60, 'Laguna': 61,
                 'Leon': 62, 'Linea': 63, 'Lodgy': 64, 'Logan': 65, 'Marea': 66, 'Megane': 67, 'Micra': 68,
                 'Modus': 69, 'Mondeo': 70, 'Octavia': 71, 'One': 72, 'Palio': 73, 'Panda': 74, 'Passat': 75,
                 'Picanto': 76, 'Polo': 77, 'Primera': 78, 'Punto': 79, 'R 12': 80, 'R 19': 81, 'Rapid': 82,
                 'Rio': 83, 'S40': 84, 'S60': 85, 'Sandero': 86, 'Scenic': 87, 'Scir\
    occo': 88, 'Siena': 89, 'Solenza': 90, 'SuperB': 91, 'Swift': 92, 'Symbol': 93, 'Talisman': 94, 'Tipo': 95,
                 'Toledo': 96, 'Uno': 97, 'V40': 98, 'Vectra': 99, 'Yaris': 100, 'Zafira': 101, 'i20': 102,
                 'i20 Active': 103, 'i20 Troy': 104, 'i30': 105, 'Şahin': 106}
    dict_Model = {'1.0 TSi Life': 0, '1.1 EX': 1, '1.2 Active': 2, '1.2 Ambiance': 3, '1.2 Authentique': 4,
                  '1.2 Authentique Edition': 5, '1.2 D-CVVT Jump': 6, '1.2 D-CVVT Sense': 7, '1.2 DOHC Mode': 8,
                  '1.2 Dynamic': 9, '1.2 EL': 10, '1.2 Enjoy\
    ': 11, '1.2 Essentia': 12, '1.2 Expression': 13, '1.2 GL': 14, '1.2 Grandtour Authentique': 15, '1.2 Joy': 16,
                  '1.2 Match': 17, '1.2 Platinum': 18, '1.2 Popstar': 19, '1.2 PureTech Active': 20,
                  '1.2 PureTech Allure Selection': 21, '1.2 PureTech Feel Bold': 22, '1.2 PureTech GT': 23,
                  '1.2 PureTech Live': 24, '1.2 S': 25, '1.2 SL': 26, '1.2 TDi Trendline': 27, '1.2 TSI Style': 28,
                  '1.2 TSi BlueMotion Comfortline': 29, '1.2 TSi Comfortline': 30, '1.2 TSi\
    Highline': 31, '1.2 TSi Midline Plus': 32, '1.2 TSi Trendline': 33, '1.2 Tekna': 34, '1.2 Touch': 35,
                  '1.2 Twinport Essentia': 36, '1.2 VTi Comfort': 37, '1.2 Visia': 38, '1.25 Flair': 39,
                  '1.3 CDTI Active': 40, '1.3 CDTI Editio\
    n': 41, '1.3 CDTI Enjoy': 42, '1.3 CDTI Enjoy 111.Yıl': 43, '1.3 CDTI Enjoy Active': 44,
                  '1.3 CDTI Enjoy Plus': 45, '1.3 CDTI Essentia': 46, '1.3 CDTI Sport': 47,
                  '1.3 CDTI ecoFLEX Cosmo': 48, '1.3 Elegance': 49, '1.3 GLS': 50,
                  '1.3 GLX': 51, '1.3 Multijet Active Plus': 52, '1.3 Multijet Actual': 53,
                  '1.3 Multijet Dynamic': 54, '1.3 Multijet Easy': 55, '1.3 Multijet Easy Plus': 56,
                  '1.3 Multijet Emotion': 57, '1.3 Multijet Emotion Plus': 58, '1.3 Multi\
    jet Pop': 59, '1.3 Multijet Urban': 60, '1.3 Multijet Urban Plus': 61, '1.3 TCe Icon': 62, '1.3 TCe Joy': 63,
                  '1.3 TCe Joy Comfort': 64, '1.3 TCe RS Line': 65, '1.33 Comfort': 66, '1.33 Fun Special': 67,
                  '1.33 Life': 68, '1.33 S\
    tyle Red Skypack': 69, '1.33 Style Skypack': 70, '1.4': 71, '1.4 Alize': 72, '1.4 Authentique': 73,
                  '1.4 CRDi Concept': 74, '1.4 CRDi Jump': 75, '1.4 CRDi Mode': 76, '1.4 CRDi Style': 77,
                  '1.4 CRDi Team': 78, '1.4 CVVT Cool': 79
        , '1.4 Classic': 80, '1.4 Comfort': 81, '1.4 Comfortline': 82, '1.4 D-4D Advance': 83,
                  '1.4 D-4D Comfort': 84, '1.4 D-4D Comfort Extra': 85, '1.4 D-4D Elegant': 86,
                  '1.4 D-4D Terra': 87, '1.4 D-4D Touch': 88, '1.4 D-CVVT Mode Pl\
    us': 89, '1.4 DOHC AB AC': 90, '1.4 DOHC HY KLM': 91, '1.4 Design': 92, '1.4 Dynamique': 93, '1.4 E': 94,
                  '1.4 EL': 95, '1.4 EcoTSI FR': 96, '1.4 Elite': 97, '1.4 Enjoy': 98, '1.4 Essentia': 99,
                  '1.4 Europa RNA': 100, '1.4 Expre\
    ssion': 101, '1.4 Expression Plus': 102, '1.4 Fire Dynamic': 103, '1.4 Fire Easy': 104,
                  '1.4 Fire Easy Plus': 105, '1.4 Fire Easy Stil': 106, '1.4 Fire Premio Sole': 107,
                  '1.4 Fire Street': 108, '1.4 Fire Urban': 109, '1.4 Fire\
    Urban Plus': 110, '1.4 Fun': 111, '1.4 HDi Active': 112, '1.4 HDi Attraction': 113, '1.4 HDi Comfort': 114,
                  '1.4 HDi Fever': 115, '1.4 HDi Look': 116, '1.4 HDi SX': 117, '1.4 HDi Urban Move': 118,
                  '1.4 MPI Elite Smart': 119, '1.\
    4 MPI Jump': 120, '1.4 MPI Style': 121, '1.4 MPI Style Plus': 122, '1.4 MPi Elite': 123, '1.4 Prima': 124,
                  '1.4 Privilege': 125, '1.4 RN': 126, '1.4 RNA': 127, '1.4 Reference': 128, '1.4 S': 129,
                  '1.4 Signo': 130, '1.4 Stella': 131,
                  '1.4 Swing': 132, '1.4 T Edition Plus': 133, '1.4 TDCi 5K': 134, '1.4 TDCi Comfort': 135,
                  '1.4 TDCi Titanium X': 136, '1.4 TDCi Trend': 137, '1.4 TDI Ambition': 138, '1.4 TDI Style': 139,
                  '1.4 TDi Comfortline': 140, '1.4 TD\
    i Trendline': 141, '1.4 TSI Style': 142, '1.4 TSi ACT BlueGT': 143, '1.4 TSi Allstar': 144,
                  '1.4 TSi BlueMotion Comfortline': 145, '1.4 TSi BlueMotion Highline': 146,
                  '1.4 TSi Comfortline': 147, '1.4 TSi Highline': 148, '1.4 TSi\
    Sportline': 149, '1.4 TSi Tour': 150, '1.4 TSi Trendline': 151, '1.4 Team': 152, '1.4 Titanium X': 153,
                  '1.4 Trendline': 154, '1.4 Trendy': 155, '1.4 Twinport Enjoy': 156, '1.4 VTi Active': 157,
                  '1.4 VTi Attraction': 158, '1.4X-Line': 159, '1.5 1.5i GL': 160, '1.5 Blue DCI Icon': 161,
                  '1.5 Blue DCI Joy Comfort': 162, '1.5 Blue DCI Touch': 163, '1.5 BlueDCI Laureate': 164,
                  '1.5 BlueDCI Stepway': 165, '1.5 BlueHDI Active': 166, '1.5 BlueHDi Feel': 167,
                  '1.5 BlueHDi Feel Bold': 168, '1.5 BlueHDi Shine': 169, '1.5 CDTI Dynamic': 170,
                  '1.5 Classic': 171, '1.5 T3 Momentum': 172, '1.5 TDCi Titanium': 173, '1.5 TDCi Trend': 174,
                  '1.5 TDCi Trend X': 175, '1.5 TSi Business': 176, '1.\
    5 dCi Alize': 177, '1.5 dCi Authentique': 178, '1.5 dCi Business': 179, '1.5 dCi Dynamique': 180,
                  '1.5 dCi Expression': 181, '1.5 dCi Expression Plus': 182, '1.5 dCi Extreme': 183,
                  '1.5 dCi Icon': 184, '1.5 dCi Joy': 185, '1.5 d\
    Ci Laureate': 186, '1.5 dCi MCV Ambiance': 187, '1.5 dCi MCV Black Line': 188, '1.5 dCi Privilege': 189,
                  '1.5 dCi Sport Tourer Expression': 190, '1.5 dCi SportTourer Joy': 191, '1.5 dCi Stepway': 192,
                  '1.5 dCi Touch': 193, '1.5\
    dCi Touch Plus': 194, '1.5 e-Tec Premium': 195, '1.5 i-VTEC Eco Elegance': 196, '1.6': 197,
                  '1.6 Authentique': 198, '1.6 BlueHDI Active': 199, '1.6 BlueHDI Allure': 200,
                  '1.6 BlueHDi Active': 201, '1.6 BlueHdi Active': 202, '1.6\
    CD': 203, '1.6 CDTI Cosmo': 204, '1.6 CDTI Design': 205, '1.6 CDTI Edition Elegance': 206,
                  '1.6 CDTI Elite': 207, '1.6 CDTI Grand Sport Design': 208, '1.6 CDTI Grand Sport Excellence': 209,
                  '1.6 CL': 210, '1.6 CLX': 211, '1.6 C\
    RDI Biz': 212, '1.6 CRDI Mode Plus': 213, '1.6 CRDi Concept Plus': 214, '1.6 CRDi Elite': 215,
                  '1.6 CRDi Motion': 216, '1.6 CRDi Premium': 217, '1.6 CRDi Style Design Pack': 218,
                  '1.6 CRDi Team': 219, '1.6 Classic': 220, '1.6 Co\
    llection': 221, '1.6 Comfort': 222, '1.6 Comfortline': 223, '1.6 Cosmo': 224, '1.6 D': 225,
                  '1.6 D Advance': 226, '1.6 D-CVVT Mode': 227, '1.6 D-CVVT Style': 228, '1.6 Dynamic': 229,
                  '1.6 E-Torq Lounge Plus': 230, '1.6 E-Torq Mi\
    rror': 231, '1.6 Edition': 232, '1.6 Edition Plus': 233, '1.6 Enjoy': 234, '1.6 Essentia Konfor': 235,
                  '1.6 Europa RNE': 236, '1.6 Expo Platinum': 237, '1.6 Expression': 238, '1.6 Extreme': 239,
                  '1.6 FSi Comfortline': 240, '1.6\
    FSi Exclusive': 241, '1.6 GDi Elite': 242, '1.6 GL': 243, '1.6 GLi': 244, '1.6 GX': 245, '1.6 Ghia': 246,
                  '1.6 HDi Active': 247, '1.6 HDi Allure': 248, '1.6 HDi Attraction': 249,
                  '1.6 HDi Comfort Pack': 250, '1.6 HDi Exclusive':
                      251, '1.6 HDi Executive Black': 252, '1.6 HDi SX': 253, '1.6 HDi Shine': 254, '1.6 LS': 255,
                  '1.6 LT Plus': 256, '1.6 Liberty': 257, '1.6 Linea': 258, '1.6 Linea Luna': 259,
                  '1.6 Linea Terra': 260, '1.6 Multijet Easy': 261, '1.\
    6 Multijet Lounge': 262, '1.6 Multijet Urban': 263, '1.6 Pacific': 264, '1.6 Primeline': 265, '1.6 RTE': 266,
                  '1.6 RXE': 267, '1.6 SX': 268, '1.6 SXE': 269, '1.6 Signo Plus': 270, '1.6 Sol': 271,
                  '1.6 T Edition': 272, '1.6 TDCi\
    Collection': 273, '1.6 TDCi Style': 274, '1.6 TDCi Titanium': 275, '1.6 TDCi Trend': 276,
                  '1.6 TDCi Trend X': 277, '1.6 TDI Ambiente': 278, '1.6 TDI CR Style': 279, '1.6 TDI Comfort': 280,
                  '1.6 TDI Elegance': 281, '1.6 TDI Optim\
    al': 282, '1.6 TDI Prestige': 283, '1.6 TDI Style': 284, '1.6 TDI Style CR': 285,
                  '1.6 TDi BlueMotion Business': 286, '1.6 TDi BlueMotion Comfortline': 287,
                  '1.6 TDi BlueMotion Highline': 288, '1.6 TDi BlueMotion Impression': 289,
                  '1.6 TDi BlueMotion Trendline': 290, '1.6 TDi Business': 291, '1.6 TDi Comfortline': 292,
                  '1.6 TDi Highline': 293, '1.6 Terra': 294, '1.6 Ti-VCT Titanium': 295, '1.6 Ti-VCT Trend': 296,
                  '1.6 Ti-VCT Trend X': 297, '1.6 Titaniu\
    m': 298, '1.6 VTi Active': 299, '1.6 VTi Comfort': 300, '1.6 XEi': 301, '1.6 XT': 302, '1.6 dCi Icon': 303,
                  '1.6 e-HDi Access': 304, '1.6 e-HDi Confort': 305, '1.6 e-HDi DStyle': 306,
                  '1.6 e-HDi Exclusive': 307, '1.6 e-HDi Inten\
    sive': 308, '1.6 i ES': 309, '1.6 i-DTEC Executive': 310, '1.6 i-DTEC Executive Plus': 311,
                  '1.6 i-VTEC ECO Elegance': 312, '1.6 i-VTEC ES': 313, '1.6 i-VTEC Eco Executive': 314,
                  '1.6 i-VTEC Elegance': 315, '1.6 ie': 316, '1.8 H\
    ighline': 317, '1.8 Hybrid Advance Skypack': 318, '1.8 Hybrid Dream': 319, '1.9 Europa RT': 320,
                  '1.9 TDi Midline': 321, '116i Comfort': 322, '116i Premium': 323, '118i Joy': 324,
                  '118i M Plus': 325, '180 AMG': 326, '180 CDI AMG\
    ': 327, '2.0 GLS': 328, '2.0 RXE': 329, '200 Urban': 330, '316i Comfort': 331, '316i M Sport': 332,
                  '316i Standart': 333, '318i Edition M Sport': 334, '318i Sport Plus': 335,
                  '318i Techno Plus': 336, '320i ED 40th Year Edition':
                      337, '320i ED Techno Plus': 338, '520d Exclusive': 339, '520d Standart': 340,
                  '520i Comfort': 341, '520i M Sport': 342, '520i Premium': 343, '70 S': 344,
                  'A 180 BlueEFFICIENCY AMG Sport': 345, 'A 180 CDI BlueEFFICIENCY AMG': 346,
                  'A 180 CDI BlueEFFICIENCY Style': 347, 'A 180 d Style': 348,
                  'A 200 BlueEFFICIENCY AMG Sport': 349, 'A3 Sedan 1.5 TFSI Design Line': 350,
                  'A3 Sedan 1.6 TDI Design Line': 351, 'A3 Sedan 1.6 TDI Dynamic': 352, 'A3 Sedan 1.6 TDI\
    Sport Line': 353, 'A3 Sportback 1.4 TFSI Attraction': 354, 'A3 Sportback 1.6 FSI': 355,
                  'A3 Sportback 1.6 TDI Ambition': 356, 'A3 Sportback 1.6 TDI Attraction': 357,
                  'A3 Sportback 1.6 TDI Sport Line': 358, 'A4 Sedan 1.4 TFSI':
                      359, 'A4 Sedan 1.6': 360, 'C 180 BlueEFFICIENCY AMG': 361,
                  'C 180 BlueEFFICIENCY Fascination': 362, 'C 180 Kompressor BlueEFFICIENCY AMG': 363,
                  'C 180 Kompressor BlueEfficiency Fascination': 364, 'C 200 D Comfort': 365,
                  'C 200 d BlueTEC AMG': 366, 'C 200 d BlueTEC Exclusive': 367, 'EVO 1.3 Multijet Dynamic': 368,
                  'EVO 1.4 Active': 369, 'S': 370, 'SLX': 371, 'Toros': 372, 'Şahin 5 Vites': 373}
    dict_KasaTipi = {'Coupe': 0, 'Hatchback/3': 1, 'Hatchback/5': 2, 'MPV': 3, 'Sedan': 4, 'Station wagon': 5}
    dict_BoyaDegisen = {'1 boyalı': 0, '1 değişen': 1, '1 değişen, 1 boyalı': 2, '1 değişen, 11 boyalı': 3,
                        '1 değişen, 12 boyalı': 4, '1 değişen, 2 boyalı': 5, '1 değişen, 3 boyalı': 6,
                        '1 değişen, 4 boyalı': 7, '1 değişen, 5 boyalı': 8, '1 değişen,7 boyalı': 9,
                        '1 değişen, 8 boyalı': 10, '10 boyalı': 11, '2 boyalı': 12, '2 değişen': 13,
                        '2 değişen, 1 boyalı': 14, '2 değişen, 10 boyalı': 15, '2 değişen, 11 boyalı': 16,
                        '2 değişen, 2 boyalı': 17, '2 değişen, 3 boyalı': 18,
                        '2 değişen, 4 boyalı': 19, '2 değişen, 5 boyalı': 20, '2 değişen, 6 boyalı': 21,
                        '2 değişen, 7 boyalı': 22, '2 değişen, 8 boyalı': 23, '2 değişen, 9 boyalı': 24,
                        '3 boyalı': 25, '3 değişen': 26, '3 değişen, 1 boyalı': 27, '3 değişen, 10 boyalı': 28,
                        '3 değişen, 2 boyalı': 29, '3 değişen, 3 boyalı': 30, '3 değişen, 4 boyalı': 31,
                        '3 değişen, 5 boyalı': 32, '3 değişen, 7 boyalı': 33, '4 boyalı': 34, '4 değişen': 35,
                        '4 değişen, 1 boyalı': 36, '4 değişen,2 boyalı': 37, '4 değişen, 5 boyalı': 38,
                        '4 değişen, 6 boyalı': 39, '5 boyalı': 40, '5 değişen, 7 boyalı': 41, '6 boyalı': 42,
                        '7 boyalı': 43, '8 boyalı': 44, '9 boyalı': 45, 'Belirtilmemiş': 46, 'Tamamı boyalı': 47,
                        'Tamamı orjinal': 48}
    dict_vites_tipi = {'Düz': 0, 'Otomatik': 1, 'Yarı Otomatik': 2}
    dict_yakit_tipi = {'Benzin': 0, 'Dizel': 1, 'Hibrit': 2, 'LPG & Benzin': 3}
    dict_cekis = {'Arkadan İtiş': 0, 'Önden Çekiş': 1}
    dict_takas = {'Takasa Uygun': 0, 'Takasa Uygun Değil': 1}

    newCar = [
        int(dict_Marka.get(str(brand[0]))),
        int(dict_Seri.get(str(series[0]))),
        int(dict_Model.get(str(model[0]))),
        int(productionYear[0]),
        int(mileage[0]),
        int(dict_vites_tipi.get(str(gearbox[0]))),
        int(dict_yakit_tipi.get(str(fuelType[0]))),
        int(dict_KasaTipi.get(str(bodyType[0]))),
        int(engineSize[0]),
        int(enginePower[0]),
        int(dict_cekis.get(str(drivetrain[0]))),
        float(fuelEfficiency[0]),
        int(fuelTank[0]),
        int(dict_BoyaDegisen.get(str(replacedParts[0]))),
        int(dict_takas.get(str(exchange[0]))),
        int(yas[0])
    ]

    model_ctb = pickle.load(open('catboost.pkl', 'rb'))
    newCar = np.array(newCar).reshape(1, -1)
    y_pred = int(model_ctb.predict(newCar))

    result_arabam = {
        'fiyat': y_pred
    }
    return result_arabam, 200


@app.route('/api/v1/emlak', methods=["GET", 'POST'])
def calculate_emlak():
    args = request.args
    brut_metrakere = args["brut_metrakere"],
    net_metrakere = args["net_metrakere"],
    esya_durumu = args["esya_durumu"],
    sitemi = args["sitemi"],
    balkon_durumu = args["balkon_durumu"],
    aidat = args["aidat"],
    takas = args["takas"],
    il = args["il"],
    ilce = args["ilce"],
    mahalle = args["mahalle"],
    oda_sayisi = args["oda_sayisi"],
    banyo_sayisi = args["banyo_sayisi"],
    tapu = args["tapu"],
    kat_sayisi = args["kat_sayisi"],
    yasi = args["yasi"],
    isitma_tipi = args["isitma_tipi"],

    df = pd.read_excel("emlakjet-2.xlsx")
    df.drop(["full_isim"], axis=1, inplace=True)
    df.drop(["kategorisi"], axis=1, inplace=True)
    df.dropna(how="all", inplace=True)
    df.drop_duplicates(inplace=True)

    df[['il', 'ilce', 'mahalle']] = df['kisa_isim'].str.split(' - ', expand=True)
    df.drop(['kisa_isim'], axis=1, inplace=True)
    df = df[df["oda_sayisi"] != "Stüdyo"]

    df["fiyat"] = df["fiyat"].apply(
        lambda x: str(x).replace("arrow_downward%", "").replace(".", "").split("TL")[0].strip("GBP"))
    df["aidat"] = df["aidat"].apply(lambda x: str(x).strip("TL").replace(" ", ""))
    df["brut_metrakere"] = df["brut_metrakere"].apply(lambda x: str(x).replace(" M2", "").replace(".", ""))
    df["net_metrakere"] = df["net_metrakere"].apply(lambda x: str(x).replace(" M2", "").replace(".", ""))
    df["banyo_sayisi"] = df["banyo_sayisi"].apply(lambda x: str(x).strip("+").replace("Yok", "0"))
    df["oda_sayisi"] = df["oda_sayisi"].apply(lambda x: str(x).strip(".").replace("Oda", "")[-3:])
    df["yasi"] = df["yasi"].apply(lambda x: str(x).split("-")[0].strip(" Ve Üzeri (Yeni)"))

    def grab_col_names(dataframe, cat_th=10, car_th=20):
        # cat_cols, cat_but_car
        cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
        num_but_cat = [col for col in dataframe.columns if
                       dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
        cat_but_car = [col for col in dataframe.columns if
                       dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
        cat_cols = cat_cols + num_but_cat
        cat_cols = [col for col in cat_cols if col not in cat_but_car]

        # num_cols
        num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
        num_cols = [col for col in num_cols if col not in num_but_cat]

        return cat_cols, num_cols, cat_but_car, num_but_cat

    cat_cols, num_cols, cat_but_car, num_but_cat = grab_col_names(df)

    def quick_missing_imp(data, num_method="median", cat_length=20, target="fiyat"):
        variables_with_na = [col for col in data.columns if
                             data[col].isnull().sum() > 0]  # Eksik değere sahip olan değişkenler listelenir

        temp_target = data[target]
        # değişken object ve sınıf sayısı cat_lengthe eşit veya altındaysa boş değerleri mode ile doldur
        data = data.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= cat_length) else x,
                          axis=0)

        # num_method mean ise tipi object olmayan değişkenlerin boş değerleri ortalama ile dolduruluyor
        if num_method == "mean":
            data = data.apply(lambda x: x.fillna(x.mean()) if x.dtype != "O" else x, axis=0)
        # num_method median ise tipi object olmayan değişkenlerin boş değerleri ortalama ile dolduruluyor
        elif num_method == "median":
            data = data.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0)

        data[target] = temp_target
        return data

    df = quick_missing_imp(df, num_method="median", cat_length=17)

    df['aidat'] = df['aidat'].replace('nan', np.nan)
    df["aidat"].fillna(0, inplace=True)

    df["brut_metrakere"] = df['brut_metrakere'].astype('int')
    df["net_metrakere"] = df['net_metrakere'].astype('int')
    df["yasi"] = df['yasi'].astype('int')
    df["banyo_sayisi"] = df['banyo_sayisi'].astype('int')
    df["kat_sayisi"] = df['kat_sayisi'].astype('int')
    df["aidat"] = df['aidat'].astype('int')
    df["fiyat"] = df['fiyat'].astype('int64')

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.98)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]


    def toplam_ayir_ve_hesapla(deger):
        if pd.isnull(deger):  # NaN değerleri kontrol etmek için
            return np.nan
        degerler = deger.split('+')  # "+" işaretine göre veriyi böler
        toplam = 0
        for deger in degerler:
            try:
                toplam += int(deger)  # parçalanan veriyi toplar
            except ValueError:
                continue  # sayısal olmayan değerleri atlar
        return toplam

    df['total_rooms'] = df['oda_sayisi'].apply(toplam_ayir_ve_hesapla) + df["banyo_sayisi"]
    df["brut_div_net"] = df["brut_metrakere"] / df["net_metrakere"]
    df['rooms_per_bathroom'] = df['banyo_sayisi'] / df['total_rooms']
    df['air_conditioning'] = np.where(df['isitma_tipi'].isin(['Isıtma Yok']), 'yok', 'var')
    df['maintenance_status'] = np.where(df['aidat'] > 0, 'var', 'yok')
    df['room_size_ratio'] = df['net_metrakere'] / df['total_rooms']
    df['total_room_size'] = df['net_metrakere'] * df['total_rooms']

    binary_cols = [col for col in df.columns if df[col].dtypes == "O" and len(df[col].unique()) == 2]
    df_copy = df.copy()

    dict_il = {'Adana': 0, 'Afyonkarahisar': 1, 'Aksaray': 2, 'Ankara': 3, 'Antalya': 4, 'Aydın': 5, 'Balıkesir': 6, 'Batman': 7,
     'Bilecik': 8, 'Bolu': 9, 'Burdur': 10, 'Bursa': 11, 'Denizli': 12, 'Diyarbakır': 13, 'Düzce': 14, 'Edirne': 15,
     'Elazığ': 16, 'Erzurum': 17, 'Eskişehir': 18, 'Gaziantep': 19, 'Giresun': 20, 'Isparta': 21, 'KKTC': 22,
     'Karabük': 23, 'Karaman': 24, 'Kars': 25, 'Kayseri': 26, 'Kilis': 27, 'Kocaeli': 28, 'Konya': 29, 'Kırklareli': 30,
     'Kırıkkale': 31, 'Kırşehir': 32, 'Malatya': 33, 'Manisa': 34, 'Mardin': 35, 'Mersin': 36, 'Muğla': 37,
     'Nevşehir': 38, 'Niğde': 39, 'Ordu': 40, 'Sakarya': 41, 'Samsun': 42, 'Sivas': 43, 'Tekirdağ': 44, 'Trabzon': 45,
     'Uşak': 46, 'Van': 47, 'Yalova': 48, 'Zonguldak': 49, 'Çanakkale': 50, 'İstanbul': 51, 'İzmir': 52,
     'Şanlıurfa': 53}
    dict_ilce = {'Adapazarı': 0, 'Afyonkarahisar Merkez': 1, 'Akdeniz': 2, 'Akhisar': 3, 'Aksaray Merkez': 4, 'Akyurt': 5,
     'Akçaabat': 6, 'Akşehir': 7, 'Aladağ': 8, 'Alanya': 9, 'Alaşehir': 10, 'Altıeylül': 11, 'Altındağ': 12,
     'Altınordu': 13, 'Anamur': 14, 'Arifiye': 15, 'Arnavutköy': 16, 'Artuklu': 17, 'Atakum': 18, 'Ataşehir': 19,
     'Avcılar': 20, 'Ayaş': 21, 'Ayvacık': 22, 'Ayvalık': 23, 'Bafra': 24, 'Bahçelievler': 25, 'Bakırköy': 26,
     'Balçova': 27, 'Batman Merkez': 28, 'Battalgazi': 29, 'Bayraklı': 30, 'Bayrampaşa': 31, 'Bayındır': 32,
     'Bağcılar': 33, 'Bağlar': 34, 'Başakşehir': 35, 'Başiskele': 36, 'Bergama': 37, 'Beylikdüzü': 38, 'Beşiktaş': 39,
     'Birecik': 40, 'Bodrum': 41, 'Bolu Merkez': 42, 'Bolvadin': 43, 'Bor': 44, 'Buca': 45, 'Burdur Merkez': 46,
     'Burhaniye': 47, 'Büyükçekmece': 48, 'Canik': 49, 'Dalaman': 50, 'Darıca': 51, 'Datça': 52, 'Develi': 53,
     'Didim': 54, 'Dikili': 55, 'Döşemealtı': 56, 'Düzce Merkez': 57, 'Edirne Merkez': 58, 'Edremit': 59, 'Efeler': 60,
     'Elazığ Merkez': 61, 'Elmalı': 62, 'Erdemli': 63, 'Erenler': 64, 'Ereğli': 65, 'Esenyurt': 66, 'Etimesgut': 67,
     'Eyyübiye': 68, 'Eyüpsultan': 69, 'Fatih': 70, 'Fatsa': 71, 'Fethiye': 72, 'Foça': 73, 'Gaziemir': 74,
     'Gazimağusa': 75, 'Gaziosmanpaşa': 76, 'Gebze': 77, 'Gemlik': 78, 'Germencik': 79, 'Giresun Merkez': 80,
     'Girne': 81, 'Gölbaşı': 82, 'Gölcük': 83, 'Gömeç': 84, 'Haliliye': 85, 'Havran': 86, 'Hendek': 87,
     'Isparta Merkez': 88, 'Kadıköy': 89, 'Kahramankazan': 90, 'Kapaklı': 91, 'Karabağlar': 92, 'Karabük Merkez': 93,
     'Karaköprü': 94, 'Karaman Merkez': 95, 'Karamürsel': 96, 'Karasu': 97, 'Karatay': 98, 'Karataş': 99, 'Karesi': 100,
     'Kars Merkez': 101, 'Kartal': 102, 'Kartepe': 103, 'Karşıyaka': 104, 'Kayapınar': 105, 'Kağıthane': 106,
     'Kemalpaşa': 107, 'Kepez': 108, 'Keçiören': 109, 'Kilis Merkez': 110, 'Kocaali': 111, 'Kocasinan': 112,
     'Konak': 113, 'Konyaaltı': 114, 'Korkuteli': 115, 'Kozlu': 116, 'Kuşadası': 117, 'Körfez': 118, 'Köyceğiz': 119,
     'Küçükçekmece': 120, 'Kırklareli Merkez': 121, 'Kırıkkale Merkez': 122, 'Kırşehir Merkez': 123, 'Lüleburgaz': 124,
     'Maltepe': 125, 'Mamak': 126, 'Manavgat': 127, 'Marmaraereğlisi': 128, 'Melikgazi': 129, 'Menderes': 130,
     'Menemen': 131, 'Menteşe': 132, 'Meram': 133, 'Merkezefendi': 134, 'Mezitli': 135, 'Milas': 136, 'Mudanya': 137,
     'Muratpaşa': 138, 'Mustafakemalpaşa': 139, 'Narlıdere': 140, 'Nazilli': 141, 'Nevşehir Merkez': 142,
     'Nilüfer': 143, 'Niğde Merkez': 144, 'Nusaybin': 145, 'Odunpazarı': 146, 'Ortaca': 147, 'Ortahisar': 148,
     'Osmangazi': 149, 'Pamukkale': 150, 'Pendik': 151, 'Perşembe': 152, 'Polatlı': 153, 'Pursaklar': 154,
     'Safranbolu': 155, 'Salihli': 156, 'Sapanca': 157, 'Sarayköy': 158, 'Saruhanlı': 159, 'Sarıyer': 160,
     'Sarıçam': 161, 'Seferihisar': 162, 'Selçuk': 163, 'Selçuklu': 164, 'Serdivan': 165, 'Serik': 166, 'Seyhan': 167,
     'Silivri': 168, 'Sincan': 169, 'Sivas Merkez': 170, 'Sultanbeyli': 171, 'Sultangazi': 172, 'Susurluk': 173,
     'Söke': 174, 'Söğüt': 175, 'Süleymanpaşa': 176, 'Talas': 177, 'Tarsus': 178, 'Tepebaşı': 179, 'Tire': 180,
     'Torbalı': 181, 'Toroslar': 182, 'Turgutlu': 183, 'Tuzla': 184, 'Ulukışla': 185, 'Urla': 186, 'Uşak Merkez': 187,
     'Yakutiye': 188, 'Yalova Merkez': 189, 'Yenimahalle': 190, 'Yenişehir': 191, 'Yeşilyurt': 192, 'Yomra': 193,
     'Yunusemre': 194, 'Yüreğir': 195, 'Yıldırım': 196, 'Zeytinburnu': 197, 'Zonguldak Merkez': 198, 'Çamlıyayla': 199,
     'Çan': 200, 'Çanakkale Merkez': 201, 'Çankaya': 202, 'Çarşamba': 203, 'Çayırova': 204, 'Çekmeköy': 205,
     'Çerkezköy': 206, 'Çeşme': 207, 'Çiftlikköy': 208, 'Çiğli': 209, 'Çorlu': 210, 'Çubuk': 211, 'Çukurova': 212,
     'Çınarcık': 213, 'Ümraniye': 214, 'Üsküdar': 215, 'İpekyolu': 216, 'İzmit': 217, 'İznik': 218, 'Şahinbey': 219,
     'Şarköy': 220, 'Şehitkamil': 221, 'Şehzadeler': 222, 'Şile': 223, 'Şişli': 224}
    dict_mahalle = {'1 Nolu Beşirli Mahallesi': 0, '1 Nolu Bostancı Mahallesi': 1, '1. Murat Mahallesi': 2, '100. Yıl Mahallesi': 3,
     '1200 Evler Mahallesi': 4, '14 Mayıs Mahallesi': 5, '19 Mayıs Mahallesi': 6, '2 Nolu Beşirli Mahallesi': 7,
     '2000 Evler Mahallesi': 8, '29 Ekim Mahallesi': 9, '30 Ağustos Mahallesi': 10, '4 Temmuz Mahallesi': 11,
     '50. Yıl Mahallesi': 12, '75. Yıl Mahallesi': 13, 'Abdulkadirpaşa Mahallesi': 14, 'Abdullah Paşa Mahallesi': 15,
     'Abidinpaşa Mahallesi': 16, 'Acıbadem Mahallesi': 17, 'Acıgöl Mahallesi': 18, 'Adakale Mahallesi': 19,
     'Adalet Mahallesi': 20, 'Adatepe Mahallesi': 21, 'Adnan Kahveci Mahallesi': 22, 'Adnan Menderes Mahallesi': 23,
     'Akbük Mahallesi': 24, 'Akdeniz Mahallesi': 25, 'Akevler Mahallesi': 26, 'Akkonak Mahallesi': 27,
     'Akpınar Mahallesi': 28, 'Akpıyar Mahallesi': 29, 'Aksaray Mahallesi': 30, 'Aktepe Mahallesi': 31,
     'Akyarlar Mahallesi': 32, 'Akçay Mahallesi': 33, 'Akın Simav Mahallesi': 34, 'Akıncılar Mahallesi': 35,
     'Akşemsettin Mahallesi': 36, 'Alakova Mahallesi': 37, 'Alandere Mahallesi': 38, 'Alaybey Mahallesi': 39,
     'Alaçatı Mahallesi': 40, 'Albay İbrahim Karaoğlanoğlu Mahallesi': 41, 'Alipaşa Mahallesi': 42,
     'Alsancak Mahallesi': 43, 'Altunkalem Mahallesi': 44, 'Altıağaç Mahallesi': 45, 'Altınkaya Mahallesi': 46,
     'Altınkum Mahallesi': 47, 'Altınoluk Mahallesi': 48, 'Altınova Mahallesi': 49, 'Altınova Sinan Mahallesi': 50,
     'Altıntas Mahallesi': 51, 'Altıntaş Mahallesi': 52, 'Altıntepe Mahallesi': 53, 'Ambarlı Mahallesi': 54,
     'Anadolu Mahallesi': 55, 'Andiçen Mahallesi': 56, 'Arap Hasan Mahallesi': 57, 'Arapçeşme Mahallesi': 58,
     'Arnavutköy Merkez Mahallesi': 59, 'Arpaçbahşiş Mahallesi': 60, 'Asmalıevler Mahallesi': 61,
     'Ataevler Mahallesi': 62, 'Atakent Mahallesi': 63, 'Atalar Mahallesi': 64, 'Atapark Mahallesi': 65,
     'Atatürk Mahallesi': 66, 'Ataşehir Mahallesi': 67, 'Avsallar Mahallesi': 68, 'Ayazağa Mahallesi': 69,
     'Aydoğdu Mahallesi': 70, 'Aydoğmuş Mahallesi': 71, 'Aydınlar Mahallesi': 72, 'Aydınlı Mahallesi': 73,
     'Aydınpınar Mahallesi': 74, 'Ayrancılar Mahallesi': 75, 'Ayvalı Mahallesi': 76, 'Ayvansaray Mahallesi': 77,
     'Aziziye Mahallesi': 78, 'Ağaçlı Mahallesi': 79, 'Aşağı Öveçler Mahallesi': 80, 'Aşağıpazar Mahallesi': 81,
     'Bademlidere Mahallesi': 82, 'Bademlik Mahallesi': 83, 'Bahadınlı Mahallesi': 84, 'Bahar Mahallesi': 85,
     'Bahariye Mahallesi': 86, 'Bahriye Üçok Mahallesi': 87, 'Bahçelievler Mahallesi': 88,
     'Bahçeşehir 1. Kısım Mahallesi': 89, 'Bahçeşehir 2. Kısım Mahallesi': 90, 'Bahçeşehir Mahallesi': 91,
     'Bala Mahallesi': 92, 'Balatçık Mahallesi': 93, 'Ballıkpınar Mahallesi': 94, 'Balıkyolu Mahallesi': 95,
     'Barbaros Hayrettin Paşa Mahallesi': 96, 'Barbaros Hayrettinpaşa Mahallesi': 97, 'Barbaros Mahallesi': 98,
     'Battalgazi Mahallesi': 99, 'Bayraklıdede Mahallesi': 100, 'Bayındır Mahallesi': 101, 'Bağcılar Mahallesi': 102,
     'Bağlar Mahallesi': 103, 'Bağlarbaşı Mahallesi': 104, 'Bağlarçeşme Mahallesi': 105, 'Bağlarüstü Mahallesi': 106,
     'Başak Mahallesi': 107, 'Belediye Evleri Mahallesi': 108, 'Belek Mahallesi': 109, 'Belçınar Mahallesi': 110,
     'Beyhekim Mahallesi': 111, 'Beykent Mahallesi': 112, 'Beylikdüzü OSB Mahallesi': 113, 'Beytepe Mahallesi': 114,
     'Beşikkaya Mahallesi': 115, 'Beşköprü Mahallesi': 116, 'Binevler Mahallesi': 117, 'Birlik Mahallesi': 118,
     'Bostancı Mahallesi': 119, 'Bostanlı Mahallesi': 120, 'Boyalık Mahallesi': 121, 'Boztepe Mahallesi': 122,
     'Bozyaka Mahallesi': 123, 'Buca Koop. Mahallesi': 124, 'Buruk Cumhuriyet Mahallesi': 125,
     'Bülbülzade Mahallesi': 126, 'Büyükesat Mahallesi': 127, 'Büyükhusun Köyü': 128, 'Caddebostan Mahallesi': 129,
     'Cebeci Mahallesi': 130, 'Cedit Mahallesi': 131, 'Cemalgürsel Mahallesi': 132, 'Cengizhan Mahallesi': 133,
     'Ceritler Mahallesi': 134, 'Cevatpaşa Mahallesi': 135, 'Cevizli Mahallesi': 136, 'Cikcilli Mahallesi': 137,
     'Cumhuriyet Mahallesi': 138, 'Davultepe Mahallesi': 139, 'Davutlar Mahallesi': 140, 'Dedeosman Mahallesi': 141,
     'Demirel Mahallesi': 142, 'Demirkapı Mahallesi': 143, 'Demirlibahçe Mahallesi': 144,
     'Demirtaş Cumhuriyet Mahallesi': 145, 'Demirtaş Sakarya Mahallesi': 146, 'Denizli Mahallesi': 147,
     'Derbent Mahallesi': 148, 'Dereağzı Mahallesi': 149, 'Devlet Mahallesi': 150, 'Değirmenaltı Mahallesi': 151,
     'Değirmendere Mahallesi': 152, 'Diclekent Mahallesi': 153, 'Dikkaldırım Mahallesi': 154, 'Doğanay Mahallesi': 155,
     'Doğu Kent Mahallesi': 156, 'Doğukent Mahallesi': 157, 'Dr. Ziya Kaya Mahallesi': 158, 'Dumlupınar Mahallesi': 159,
     'Durak Mahallesi': 160, 'Durali Alıç Mahallesi': 161, 'Dutlubahçe Mahallesi': 162, 'Efeler Mahallesi': 163,
     'Efendi Mahallesi': 164, 'Efirli Mahallesi': 165, 'Ege Mahallesi': 166, 'Emecik Mahallesi': 167,
     'Emek Mahallesi': 168, 'Emre Mahallesi': 169, 'Engürücük Mahallesi': 170, 'Erenköy Mahallesi': 171,
     'Erenler Mahallesi': 172, 'Ergenekon Mahallesi': 173, 'Ertuğrul Gazi Mahallesi': 174, 'Ertuğrul Mahallesi': 175,
     'Eryaman Mahallesi': 176, 'Esenboğa Merkez Mahallesi': 177, 'Esenevler Mahallesi': 178, 'Esenlik Mahallesi': 179,
     'Esentepe Köyü': 180, 'Esentepe Mahallesi': 181, 'Esenyalı Mahallesi': 182, 'Esenyurt Mahallesi': 183,
     'Esertepe Mahallesi': 184, 'Etiler Mahallesi': 185, 'Etlik Mahallesi': 186, 'Evka-5 Mahallesi': 187,
     'Fabrika Mahallesi': 188, 'Fahri Korutürk Mahallesi': 189, 'Fatih Mahallesi': 190, 'Fenerbahçe Mahallesi': 191,
     'Feridun Çelik Mahallesi': 192, 'Fertek Mahallesi': 193, 'Fesleğen Mahallesi': 194, 'Fetih Mahallesi': 195,
     'Fevzi Çakmak Mahallesi': 196, 'Fevzipaşa Mahallesi': 197, 'Foça Mahallesi': 198, 'Fırat Mahallesi': 199,
     'Fıstıklık Mahallesi': 200, 'Gap Mahallesi': 201, 'Gazi Mustafa Kemal Paşa OSB Mahallesi': 202,
     'Gazi Mustafa Kemalpaşa Mahallesi': 203, 'Gazi Osman Paşa Mahallesi': 204, 'Gazicelal Mahallesi': 205,
     'Gaziler Mahallesi': 206, 'Gaziosmanpaşa Mahallesi': 207, 'General Zeki Doğan Mahallesi': 208,
     'Geriş Mahallesi': 209, 'Gökmeydan Mahallesi': 210, 'Gökpınar Mahallesi': 211, 'Göksu Mahallesi': 212,
     'Göktürk Merkez Mahallesi': 213, 'Gökçek Mahallesi': 214, 'Görükle Mahallesi': 215, 'Gözne Mahallesi': 216,
     'Göztepe Mahallesi': 217, 'Gülbahçesi Mahallesi': 218, 'Güllübağ Mahallesi': 219, 'Güllük Mahallesi': 220,
     'Gülpınar Mahallesi': 221, 'Gültepe Mahallesi': 222, 'Gümüşler Bld. (Yeni Gümüş Mahallesi)': 223,
     'Gümüşlük Mahallesi': 224, 'Gümüştepe Mahallesi': 225, 'Gündoğan Mahallesi': 226, 'Gündoğdu Mahallesi': 227,
     'Gündoğu Mahallesi': 228, 'Güney Mahallesi': 229, 'Güneşli Mahallesi': 230, 'Güre Mahallesi': 231,
     'Gürpınar Mahallesi': 232, 'Gürsel Mahallesi': 233, 'Gürselpaşa Mahallesi': 234, 'Güvenevler Mahallesi': 235,
     'Güvercintepe Mahallesi': 236, 'Güzelce Mahallesi': 237, 'Güzeloluk Mahallesi': 238,
     'Güzelyalı Burgaz Mahallesi': 239, 'Güzelyalı Eğitim Mahallesi': 240, 'Güzelyalı Mahallesi': 241,
     'Güzelyurt Mahallesi': 242, 'Güzelçamlı Mahallesi': 243, 'Hacıfeyzullah Mahallesi': 244,
     'Hacıkaplanlar Mahallesi': 245, 'Hacılar Mahallesi': 246, 'Hacımiktat Mahallesi': 247, 'Halilağa Mahallesi': 248,
     'Halitpaşa Mahallesi': 249, 'Halkalı Merkez Mahallesi': 250, 'Hamambaşı Mahallesi': 251, 'Hamitler Mahallesi': 252,
     'Hamzabey Mahallesi': 253, 'Harmandere Mahallesi': 254, 'Harmanlar Mahallesi': 255, 'Hatip Mahallesi': 256,
     'Hekimzade Mahallesi': 257, 'Hisar Mahallesi': 258, 'Hoşnudiye Mahallesi': 259, 'Humanız Mahallesi': 260,
     'Hurma Mahallesi': 261, 'Huzur Mahallesi': 262, 'Hürriyet Mahallesi': 263, 'Hıdırlık Mahallesi': 264,
     'Ihlamurkent Mahallesi': 265, 'Ilıca Mahallesi': 266, 'Kabaağaç Mahallesi': 267, 'Kabakoz Mahallesi': 268,
     'Kabakum Mahallesi': 269, 'Kadriye Mahallesi': 270, 'Kadıköy Bld. (Merkez Mahallesi)': 271,
     'Kadıköy Mahallesi': 272, 'Kadıovacık Mahallesi': 273, 'Kafkas Mahallesi': 274, 'Kanal Mahallesi': 275,
     'Kanuni Mahallesi': 276, 'Karaağaç Mahallesi': 277, 'Karaağaçlı Mahallesi': 278, 'Karaburun Mahallesi': 279,
     'Karadeniz Mahallesi': 280, 'Karadere Mahallesi': 281, 'Karagümrük Mahallesi': 282, 'Karakaya Mahallesi': 283,
     'Karakaş Mahallesi': 284, 'Karaman Mahallesi': 285, 'Karamanlı Mahallesi': 286, 'Karamazak Mahallesi': 287,
     'Karaosman Mahallesi': 288, 'Karaova Mahallesi': 289, 'Karapürçek Mahallesi': 290, 'Karaçulha Mahallesi': 291,
     'Kardelen Mahallesi': 292, 'Kardeşler Mahallesi': 293, 'Karlıktepe Mahallesi': 294, 'Karslılar Mahallesi': 295,
     'Kartaltepe Mahallesi': 296, 'Karyağdı Mahallesi': 297, 'Karşıyaka Mahallesi': 298, 'Kavaklar Mahallesi': 299,
     'Kavaklı Mahallesi': 300, 'Kayabaşı Mahallesi': 301, 'Kayacıkaraplar Mahallesi': 302, 'Kayalar Mahallesi': 303,
     'Kazım Karabekir Mahallesi': 304, 'Kaşüstü Mahallesi': 305, 'Keli Mahallesi': 306, 'Kemal Atatürk Mahallesi': 307,
     'Kemaliye Mahallesi': 308, 'Kemalpaşa Mahallesi': 309, 'Kemalöz Mahallesi': 310, 'Kentkoop Mahallesi': 311,
     'Kepez Bld. (Cumhuriyet Mahallesi)': 312, 'Kethüda Mahallesi': 313, 'Kireli Mahallesi': 314,
     'Kiçiköy Mahallesi': 315, 'Koca Sinan Mahallesi': 316, 'Kocasinan Mahallesi': 317, 'Konacık Mahallesi': 318,
     'Konaklı Mahallesi': 319, 'Koru Bld. (Cumhuriyet Mahallesi)': 320, 'Korucuk Mahallesi': 321,
     'Korutürk Mahallesi': 322, 'Kosova Mahallesi': 323, 'Kozağaç Mahallesi': 324, 'Koçyazı Mahallesi': 325,
     'Kumburgaz Mahallesi': 326, 'Kumluca Mahallesi': 327, 'Kurtuluş Mahallesi': 328, 'Kuruçeşme Mahallesi': 329,
     'Kuzeyyaka Mahallesi': 330, 'Kuşlubahçe Mahallesi': 331, 'Kuştepe Mahallesi': 332, 'Kökez Mahallesi': 333,
     'Körpeşler Mahallesi': 334, 'Kötekli Mahallesi': 335, 'Köşk Mahallesi': 336, 'Kütükçü Mahallesi': 337,
     'Küçük Çiğli Mahallesi': 338, 'Küçükhusun Köyü': 339, 'Kılıç Reis Mahallesi': 340, 'Kılıçarslan Mahallesi': 341,
     'Kındam Mahallesi': 342, 'Kırkpınar Tepebaşı Mahallesi': 343, 'Kırmızıtoprak Mahallesi': 344,
     'Kızkalesi Mahallesi': 345, 'Kızlar Pınarı Mahallesi': 346, 'Kızılarık Mahallesi': 347,
     'Kızılcaterzi Mahallesi': 348, 'Kızılcaşar Mahallesi': 349, 'Kızılpınar Atatürk Mahallesi': 350,
     'Lalapaşa Mahallesi': 351, 'Laleli Mahallesi': 352, 'Levent Mahallesi': 353, 'Liman Mahallesi': 354,
     'Mahfesığmaz Mahallesi': 355, 'Mahmudiye Mahallesi': 356, 'Mahmutlar Mahallesi': 357, 'Malatya-İncesu Köyü': 358,
     'Malazgirt Mahallesi': 359, 'Maltepe Mahallesi': 360, 'Mareşal Çakmak Mahallesi': 361, 'Marmara Mahallesi': 362,
     'Mavişehir Mahallesi': 363, 'Maşuk Mahallesi': 364, 'Mebusevleri Mahallesi': 365, 'Medya Mahallesi': 366,
     'Mehmet Akif Ersoy Mahallesi': 367, 'Mehmet Akif Mahallesi': 368, 'Mehmet Sanlı Mahallesi': 369,
     'Mehmetçik Mahallesi': 370, 'Mehterçeşme Mahallesi': 371, 'Menderes Mahallesi': 372, 'Merkez Mahallesi': 373,
     'Metin Oktay Mahallesi': 374, 'Mevlana Mahallesi': 375, 'Meydan Mahallesi': 376, 'Mezopotamya Mahallesi': 377,
     'Meşrutiyet Mahallesi': 378, 'Millet Mahallesi': 379, 'Milli Egemenlik Mahallesi': 380,
     'Mimar Sinan Mahallesi': 381, 'Mithatpaşa Mahallesi': 382, 'Muhittin Mahallesi': 383, 'Muradiye Mahallesi': 384,
     'Murat Mahallesi': 385, 'Murat Reis Mahallesi': 386, 'Muratbey Mahallesi': 387, 'Muratdede Mahallesi': 388,
     'Mustafa Kemal Atatürk Mahallesi': 389, 'Mustafa Kemal Mahallesi': 390, 'Mustafa Kemal Paşa Mahallesi': 391,
     'Mustafalar Mahallesi': 392, 'Mutlu Mahallesi': 393, 'Mürsel Mahallesi': 394, 'Namık Kemal Mahallesi': 395,
     'Narlıkuyu Mahallesi': 396, 'Necip Fazıl Kısakürek Mahallesi': 397, 'Necip Fazıl Mahallesi': 398,
     'Necmettin Erbakan Mahallesi': 399, 'Nisbetiye Mahallesi': 400, 'Nişancıpaşa Mahallesi': 401,
     'Nusratiye Mahallesi': 402, 'Oba Mahallesi': 403, 'Okçular Mahallesi': 404, 'Orta Mahallesi': 405,
     'Osman Gazi Mahallesi': 406, 'Osmangazi Mahallesi': 407, 'Osmanlı Mahallesi': 408, 'Ovacık Mahallesi': 409,
     'Ozanköy Köyü': 410, 'Oğuzlar Mahallesi': 411, 'Pamuklar Mahallesi': 412, 'Payamlı Mahallesi': 413,
     'Paşaköy Mahallesi': 414, 'Pelitlibağ Mahallesi': 415, 'Piremir Mahallesi': 416, 'Pirili Mahallesi': 417,
     'Plevne Mahallesi': 418, 'Poligon Mahallesi': 419, 'Pınar Mahallesi': 420, 'Pınarbaşı Mahallesi': 421,
     'Refet Bele Mahallesi': 422, 'Reis Mahallesi': 423, 'Sakarya Mahallesi': 424, 'Salihler Mahallesi': 425,
     'Sancak Mahallesi': 426, 'Saray Cumhuriyet Mahallesi': 427, 'Saray Fatih Mahallesi': 428, 'Saray Mahallesi': 429,
     'Sarıahmetli Köyü': 430, 'Sarıcalı Mahallesi': 431, 'Sarıkız Mahallesi': 432, 'Sarılar Mahallesi': 433,
     'Sarısu Mahallesi': 434, 'Sarıyurt Mahallesi': 435, 'Selahaddin Eyyubi Mahallesi': 436, 'Selimiye Mahallesi': 437,
     'Selimpaşa Mahallesi': 438, 'Selimzade Mahallesi': 439, 'Selçuk Mahallesi': 440, 'Selçuklu Mahallesi': 441,
     'Seyit Ahmet Mahallesi': 442, 'Seyran Mahallesi': 443, 'Seyrantepe Mahallesi': 444, 'Seyyid Ömer Mahallesi': 445,
     'Seğmenler Mahallesi': 446, 'Side Mahallesi': 447, 'Sinandede Mahallesi': 448, 'Sinanpaşa Mahallesi': 449,
     'Siyavuşpaşa Mahallesi': 450, 'Sofudede Mahallesi': 451, 'Soğanlı Mahallesi': 452, 'Soğucak Mahallesi': 453,
     'Soğukkuyu Mahallesi': 454, 'Soğukpınar Mahallesi': 455, 'Sultaniye Mahallesi': 456,
     'Sultançiftliği Mahallesi': 457, 'Söğütlü Mahallesi': 458, 'Sümbül Efendi Mahallesi': 459, 'Sümer Mahallesi': 460,
     'Sütlüce Mahallesi': 461, 'Sütçüler Mahallesi': 462, 'Sırrın Mahallesi': 463, 'Tahtakuşlar Mahallesi': 464,
     'Tahılpazarı Mahallesi': 465, 'Talatpaşa Mahallesi': 466, 'Talaytepe Mahallesi': 467, 'Tandoğan Mahallesi': 468,
     'Tarabya Mahallesi': 469, 'Tayakadın Mahallesi': 470, 'Taşpınar Mahallesi': 471, 'Taşyaka Mahallesi': 472,
     'Teferrüç Mahallesi': 473, 'Tekneçukur Köyü': 474, 'Tepe Mahallesi': 475, 'Terkos Mahallesi': 476,
     'Tersane Mahallesi': 477, 'Terzialiler Mahallesi': 478, 'Teyyaredüzü Mahallesi': 479, 'Torbalı Mahallesi': 480,
     'Toros Mahallesi': 481, 'Tulumtaş Mahallesi': 482, 'Tuna Mahallesi': 483, 'Tunahan Mahallesi': 484,
     'Turgutreis Mahallesi': 485, 'Tuzcumurat Mahallesi': 486, 'Tuzluçayır Mahallesi': 487, 'Tömük Mahallesi': 488,
     'Törekent Mahallesi': 489, 'Türkmen Mahallesi': 490, 'Türkmenköy Mahallesi': 491, 'Ufuktepe Mahallesi': 492,
     'Ulamış Mahallesi': 493, 'Ulu Camii Mahallesi': 494, 'Ulu Kent Mahallesi': 495, 'Umurbey Mahallesi': 496,
     'Uncubozköy Mahallesi': 497, 'Uzuncaorman Mahallesi': 498, 'Uzundere Mahallesi': 499, 'Uzunoluk Mahallesi': 500,
     'Vali Mithat Bey Mahallesi': 501, 'Vali Rahmi Bey Mahallesi': 502, 'Varlık Mahallesi': 503, 'Vatan Mahallesi': 504,
     'Vıraca Mahallesi': 505, 'Yaka Mahallesi': 506, 'Yakacık Mahallesi': 507, 'Yakakent Mahallesi': 508,
     'Yakuplu Mahallesi': 509, 'Yalı Mahallesi': 510, 'Yalım Mahallesi': 511, 'Yalınayak Mahallesi': 512,
     'Yalıncak Mahallesi': 513, 'Yarenler Mahallesi': 514, 'Yarhasanlar Mahallesi': 515, 'Yavansu Mahallesi': 516,
     'Yavuz Selim Mahallesi': 517, 'Yayla Mahallesi': 518, 'Yaylacık Mahallesi': 519, 'Yaşamkent Mahallesi': 520,
     'Yedi Aralık Mahallesi': 521, 'Yedikule Mahallesi': 522, 'Yeni Batı Mahallesi': 523, 'Yeni Emek Mahallesi': 524,
     'Yeni Mahallesi': 525, 'Yenice Mahallesi': 526, 'Yenidoğan Mahallesi': 527, 'Yenigün Mahallesi': 528,
     'Yenikent Mahallesi': 529, 'Yeniköy Mahallesi': 530, 'Yenimahalle Mahallesi': 531, 'Yeniçiftlik Mahallesi': 532,
     'Yenişehir Mahallesi': 533, 'Yeşilkent Mahallesi': 534, 'Yeşilova Mahallesi': 535, 'Yeşilpınar Mahallesi': 536,
     'Yeşiltepe Mahallesi': 537, 'Yeşilyurt Mahallesi': 538, 'Yeşilyuva Mahallesi': 539, 'Yiğitler Mahallesi': 540,
     'Yokuşbaşı Mahallesi': 541, 'Yukarı Bahçelievler Mahallesi': 542, 'Yukarı Öveçler Mahallesi': 543,
     'Yunus Emre Mahallesi': 544, 'Yurt Mahallesi': 545, 'Yuvaköy Mahallesi': 546, 'Yüksekalan Mahallesi': 547,
     'Yükseltepe Mahallesi': 548, 'Yıldırım Beyazıt Mahallesi': 549, 'Yıldırım Mahallesi': 550, 'Yıldız Mahallesi': 551,
     'Yıldızlı Mahallesi': 552, 'Yıldıztepe Mahallesi': 553, 'Zafer Mahallesi': 554, 'Zafertepe Mahallesi': 555,
     'Zeytinköy Mahallesi': 556, 'Zeytinli Mahallesi': 557, 'Zeytinlik Mahallesi': 558, 'Zirvekent Mahallesi': 559,
     'Zümrüt Mahallesi': 560, 'Çalı Mahallesi': 561, 'Çamlıbel Mahallesi': 562, 'Çamlıca Mahallesi': 563,
     'Çamlık Mahallesi': 564, 'Çandarlı Mahallesi': 565, 'Çanta Sancaktepe Mahallesi': 566, 'Çarşıbaşı Mahallesi': 567,
     'Çatalköy Köyü': 568, 'Çatalmeşe Mahallesi': 569, 'Çavuş Mahallesi': 570, 'Çaybaşı Fuadiye Mahallesi': 571,
     'Çaybaşıyeniköy Mahallesi': 572, 'Çağlayan Mahallesi': 573, 'Çekirge Mahallesi': 574, 'Çelebi Mahallesi': 575,
     'Çiftlik Mahallesi': 576, 'Çiftlikönü Mahallesi': 577, 'Çiğdem Mahallesi': 578, 'Çiğdemtepe Mahallesi': 579,
     'Çobançeşme Mahallesi': 580, 'Çukuraltı Mahallesi': 581, 'Çukurçayır Mahallesi': 582, 'Çöşnük Mahallesi': 583,
     'Çınar Mahallesi': 584, 'Çırpıcı Mahallesi': 585, 'Ömerbey Mahallesi': 586, 'Ömerli Mahallesi': 587,
     'Önerler Mahallesi': 588, 'Örnek Mahallesi': 589, 'Örnekköy Mahallesi': 590, 'Özevler Mahallesi': 591,
     'Öğretmenler Mahallesi': 592, 'Üniversite Mahallesi': 593, 'Üçevler Mahallesi': 594, 'Üçkuyu Mahallesi': 595,
     'İdealtepe Mahallesi': 596, 'İkizçay Mahallesi': 597, 'İkiçeşmelik Mahallesi': 598, 'İlbade Mahallesi': 599,
     'İlhanlı Mahallesi': 600, 'İlkadım Mahallesi': 601, 'İlkbahar Mahallesi': 602, 'İmbatlı Mahallesi': 603,
     'İncek Mahallesi': 604, 'İncesu Mahallesi': 605, 'İncilipınar Mahallesi': 606, 'İncilli Mahallesi': 607,
     'İncirli Mahallesi': 608, 'İnönü Mahallesi': 609, 'İrfaniye Mahallesi': 610, 'İskele Mahallesi': 611,
     'İskenderpaşa Mahallesi': 612, 'İslambey Mahallesi': 613, 'İslice Mahallesi': 614, 'İsmetpaşa Mahallesi': 615,
     'İstasyon Mahallesi': 616, 'İstiklal Mahallesi': 617, 'İşçi Blokları Mahallesi': 618, 'Şafak Mahallesi': 619,
     'Şafaktepe Mahallesi': 620, 'Şahap Gürler Mahallesi': 621, 'Şahincili Mahallesi': 622, 'Şahintepe Mahallesi': 623,
     'Şehit Cengiz Karaca Mahallesi': 624, 'Şehit Cevdet Özdemir Mahallesi': 625, 'Şehit Kubilay Mahallesi': 626,
     'Şehitler Mahallesi': 627, 'Şehitlik Mahallesi': 628, 'Şelale Mahallesi': 629, 'Şemikler Mahallesi': 630,
     'Şemsitebrizi Mahallesi': 631, 'Şenlik Mahallesi': 632, 'Şentepe Mahallesi': 633, 'Şeyh Sinan Mahallesi': 634,
     'Şeyhmuhittin Mahallesi': 635, 'Şirinevler Mahallesi': 636, 'Şükrüpaşa Mahallesi': 637,
     'Şıh Mehmet Mahallesi': 638}

    difference = list(set(cat_cols) - set(binary_cols) - set(num_but_cat))

    def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
        dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
        return dataframe

    df = one_hot_encoder(df, difference, drop_first=True)

    esya_durumu = 0 if esya_durumu[0] == "Boş" else 1
    sitemi = 1 if sitemi[0] == "Hayır" else 0
    takas = 0 if takas[0] == "Var" else 1
    balkon_durumu = 0 if balkon_durumu[0] == "Var" else 1

    il = int(dict_il.get(il[0]))
    ilce = int(dict_ilce.get(ilce[0]))
    mahalle = int(dict_mahalle.get(mahalle[0]))

    top = 0
    degerler = str(oda_sayisi[0]).split("+")
    for deger in degerler:
        try:
            top += int(deger)
        except ValueError:
            continue
    total_rooms = top + int(banyo_sayisi[0])
    brut_div_net = int(brut_metrakere[0]) / int(net_metrakere[0])
    rooms_per_bathroom = int(banyo_sayisi[0]) / total_rooms
    air_conditioning = 0 if isitma_tipi[0] == "Isıtma Yok" else 1
    maintenance_status = 1 if int(aidat[0]) > 0 else 0
    room_size_ratio = int(brut_metrakere[0]) / total_rooms
    total_room_size = int(brut_metrakere[0]) * total_rooms

    ############################################################################

    tapu_Hisselitapu = 1 if tapu[0] == "Hisseli Tapu" else 0
    tapu_Katmülkiyetli = 1 if tapu[0] == "Kat Mülkiyetli" else 0
    tapu_Katirtifaki = 1 if tapu[0] == "Kat İrtifakı" else 0
    tapu_yok = 1 if tapu[0] == "Yok" else 0
    oda_sayisi_1arti1 = 1 if oda_sayisi[0] == "1+1" else 0
    oda_sayisi_2arti0 = 1 if oda_sayisi[0] == "2+0" else 0
    oda_sayisi_2arti1 = 1 if oda_sayisi[0] == "2+1" else 0
    oda_sayisi_2arti2 = 1 if oda_sayisi[0] == "2+2" else 0
    oda_sayisi_3arti1 = 1 if oda_sayisi[0] == "3+1" else 0
    oda_sayisi_3arti2 = 1 if oda_sayisi[0] == "3+2" else 0
    oda_sayisi_4arti1 = 1 if oda_sayisi[0] == "4+1" else 0
    oda_sayisi_4arti2 = 1 if oda_sayisi[0] == "4+2" else 0
    oda_sayisi_4arti4 = 1 if oda_sayisi[0] == "4+4" else 0
    oda_sayisi_5arti0 = 1 if oda_sayisi[0] == "5+0" else 0
    oda_sayisi_5arti1 = 1 if oda_sayisi[0] == "5+1" else 0
    oda_sayisi_5arti2 = 1 if oda_sayisi[0] == "5+2" else 0
    oda_sayisi_6arti1 = 1 if oda_sayisi[0] == "6+1" else 0
    oda_sayisi_6arti2 = 1 if oda_sayisi[0] == "6+2" else 0
    oda_sayisi_7arti2 = 1 if oda_sayisi[0] == "7+2" else 0
    oda_sayisi_7arti3 = 1 if oda_sayisi[0] == "7+3" else 0
    oda_sayisi_8arti2 = 1 if oda_sayisi[0] == "8+2" else 0
    oda_sayisi_9arti = 1 if oda_sayisi[0] == "9+" else 0
    isitma_tipi_Elektrikliradyator = 1 if isitma_tipi[0] == "Elektrikli Radyatör" else 0
    isitma_tipi_Gunesenerjisi = 1 if isitma_tipi[0] == "Güneş Enerjisi" else 0
    isitma_tipi_Isipompasi = 1 if isitma_tipi[0] == "Isı Pompası" else 0
    isitma_tipi_Isitmayok = 1 if isitma_tipi[0] == "Isıtma Yok" else 0
    isitma_tipi_Jeotermal = 1 if isitma_tipi[0] == "Jeotermal" else 0
    isitma_tipi_Katkaloriferi = 1 if isitma_tipi[0] == "Kat Kaloriferi" else 0
    isitma_tipi_Klimali = 1 if isitma_tipi[0] == "Klimalı" else 0
    isitma_tipi_Kombidogalgaz = 1 if isitma_tipi[0] == "Kombi Doğalgaz" else 0
    isitma_tipi_Merkezipayolcer = 1 if isitma_tipi[0] == "Merkezi (Pay Ölçer)" else 0
    isitma_tipi_Merkezidogalgaz = 1 if isitma_tipi[0] == "Merkezi Doğalgaz" else 0
    isitma_tipi_Merkezikomur = 1 if isitma_tipi[0] == "Merkezi Kömür" else 0
    isitma_tipi_Sobali = 1 if isitma_tipi[0] == "Sobalı" else 0
    isitma_tipi_VRV = 1 if isitma_tipi[0] == "VRV" else 0
    isitma_tipi_Yerdenisitma = 1 if isitma_tipi[0] == "Yerden Isıtma" else 0
    isitma_tipi_Somine = 1 if isitma_tipi[0] == "Şömine" else 0

    ############################################################################
    newEmlak = [
        brut_metrakere[0], net_metrakere[0], yasi[0], esya_durumu, banyo_sayisi[0], sitemi, kat_sayisi[0],
        balkon_durumu,
        aidat[0], takas, il, ilce, mahalle, total_rooms, brut_div_net, rooms_per_bathroom, air_conditioning,
        maintenance_status, room_size_ratio, total_room_size,
        tapu_Hisselitapu, tapu_Katmülkiyetli, tapu_Katirtifaki, tapu_yok, oda_sayisi_1arti1, oda_sayisi_2arti0,
        oda_sayisi_2arti1, oda_sayisi_2arti2, oda_sayisi_3arti1, oda_sayisi_3arti2, oda_sayisi_4arti1,
        oda_sayisi_4arti2, oda_sayisi_4arti4, oda_sayisi_5arti0, oda_sayisi_5arti1, oda_sayisi_5arti2,
        oda_sayisi_6arti1, oda_sayisi_6arti2, oda_sayisi_7arti2, oda_sayisi_7arti3, oda_sayisi_8arti2, oda_sayisi_9arti,
        isitma_tipi_Elektrikliradyator, isitma_tipi_Gunesenerjisi, isitma_tipi_Isipompasi, isitma_tipi_Isitmayok,
        isitma_tipi_Jeotermal, isitma_tipi_Katkaloriferi, isitma_tipi_Klimali, isitma_tipi_Kombidogalgaz,
        isitma_tipi_Merkezipayolcer, isitma_tipi_Merkezidogalgaz, isitma_tipi_Merkezikomur, isitma_tipi_Sobali,
        isitma_tipi_VRV, isitma_tipi_Yerdenisitma, isitma_tipi_Somine
    ]

    model_ctb = pickle.load(open('emlakjet_model.pkl', 'rb'))
    newEmlak = np.array(newEmlak).reshape(1, -1)
    y_pred = int(model_ctb.predict(newEmlak))

    result_emlak = {
        'fiyat': y_pred
    }
    return result_emlak, 200


if __name__ == '__main__':
    app.run(debug=True)
