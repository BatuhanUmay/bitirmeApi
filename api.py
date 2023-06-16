from flask import Flask, request
import pickle
import numpy as np
import datetime
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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

    unique_esya_durumu = df["esya_durumu"].unique()
    unique_isitma_tipi = df["isitma_tipi"].unique()
    unique_sitemi = df["sitemi"].unique()
    unique_balkon_durumu = df["balkon_durumu"].unique()
    unique_takas = df["takas"].unique()
    unique_tapu = df["tapu"].unique()
    unique_il = df["il"].unique()
    unique_ilce = df["ilce"].unique()
    unique_mahalle = df["mahalle"].unique()
    unique_oda_sayisi = df["oda_sayisi"].unique()

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

    le = LabelEncoder()
    df["il"] = le.fit_transform(df["il"])
    dict_il = dict(zip(le.classes_, le.transform(le.classes_)))
    df["ilce"] = le.fit_transform(df["ilce"])
    dict_ilce = dict(zip(le.classes_, le.transform(le.classes_)))
    df["mahalle"] = le.fit_transform(df["mahalle"])
    dict_mahalle = dict(zip(le.classes_, le.transform(le.classes_)))

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
