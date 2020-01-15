from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
import os
from collections import Counter

from wagtail.core.models import Page
from wagtail.search.models import Query


def reqVarInt(request, var):
    tmp = request.GET.get(var, None)
    return int(tmp) if tmp.isdigit() else None


def reqVarFloat(request, var):
    try:
        return float(request.GET.get(var, None))
    except:
        return None


def options(request):
    db = MongoClient("192.38.87.61").ribuild

    result = db.website.aggregate([{
         "$group": {
            "_id": "null",
            "wall_material": { "$addToSet": "$wall_material"},
            "int_plaster": { "$addToSet": "$int_plaster"},
            "ext_plaster": { "$addToSet": "$ext_plaster"}
        }
    }, {
        "$project": { "_id": 0 }
    }])

    res = result.next()
    res["prio"] = {
        "u_value": "U-value",
        "mould": "Mould Risk",
        "algae": "Algae Risk",
        "heat_loss": "Heat Loss",
        "surface_temp": "Surface temp.",
        "environment_impact": "Environmental impact"
    }
    return JsonResponse(res)


def sim(request):
    lon = reqVarFloat(request, 'lat') # ups TODO - DB FIX
    lat = reqVarFloat(request, 'lon') # ups TODO - DB FIX
    orien = reqVarInt(request, 'orien')
    thickness = reqVarInt(request, 'thickness')

    outer = request.GET.get('outer', None)
    inner = request.GET.get('inner', None)
    wall_material = request.GET.get('wall_material', None)
    sort = request.GET.get('sort', None)

    #db = MongoClient(os.getenv('MONGODB_URI')).ribuild
    db = MongoClient("192.38.87.61").ribuild


    weightInput = []
    totalWeight = 0
    s1 = request.GET.get('s1', None)
    s2 = request.GET.get('s2', None)
    s3 = request.GET.get('s3', None)

    if (s1):
        totalWeight += 1
    if (s2):
        totalWeight += 0.6
    if (s3):
        totalWeight += 0.3



    query = [{
        "$geoNear": {
            "near": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "distanceField": "distance",
            "query": {
                "wall_width": {
                    "$gt": thickness + 50,
                    "$lt": thickness - 50
                },
                "orientation": {
                    "$gt": orien - 45/2.,
                    "$lt": orien + 45/2.
                },
                "ext_plaster": outer,
                "int_plaster": inner,
                "wall_material": wall_material
            }
        }
    }, {
        "$group": {
            "_id": {
                "insulation_system": "$insulation_system",
                "insulation_thickness": "$insulation_thickness"
            },
            "u_value": { "$avg": "$u_value" },
            "mould": { "$avg": "$mould" },
            "algae": { "$avg": "$algae" },
            "heat_loss": { "$avg": "$heat_loss" },
            "surface_temp": { "$avg": "$surface_temp" },
            "environment_impact": { "$avg": "$environment_impact" },
            "count": { "$sum": 1 },
        }
    }, {
       "$addFields": {
            "insulation_system": "$_id.insulation_system",
            "insulation_thickness": "$_id.insulation_thickness",
       }
    }, {
        "$project": {
            "_id": 0
        }
    }]

    #return JsonResponse(query, safe=False)
    results = list(db.website.aggregate(query))
    #return JsonResponse({"res": list(results), "weights": weightInput}, safe=False)

    sumCols = ["u_value", "mould", "algae", "heat_loss", "surface_temp", "environment_impact"]

    c = Counter()
    for d in results:
        c.update(d)


    for t in results:
        tmp = 0;
        if (s1):
            tmp += t[s1] / c[s1] * 1 / totalWeight * (-1 if s1 != "surface_temp" else 1)
        if (s2):
            tmp += t[s2] / c[s2] * 1 / totalWeight * (-1 if s2 != "surface_temp" else 1)
        if (s3):
            tmp += t[s3] / c[s3] * 1 / totalWeight * (-1 if s3 != "surface_temp" else 1)

        t["weight"] = tmp

    #return JsonResponse(results, safe=False)



    return render(request, 'search/sim.html', {
        'results': sorted(results, key = lambda x: x["weight"], reverse = True)
    })


# db.website.aggregate([{
#     "$match": {
#         "wall_material": "name2",
#     }
# }, {
#     "$group": {
#         "_id": null,
#         "u_value_min": { "$min": "$u_value" },
#         "u_value_max": { "$max": "$u_value" },
#         "mould_min": { "$min": "$mould" },
#         "mould_max": { "$max": "$mould" },
#         "algae_min": { "$min": "$algae" },
#         "algae_max": { "$max": "$algae" },
#         "heat_loss_min": { "$min": "$heat_loss" },
#         "heat_loss_max": { "$max": "$heat_loss" },
#     }
# }, {
#     "$project": {
#         "u_value": {
#             "min": "$u_value_min",
#             "max": "$u_value_max"
#         },
#         "mould": {
#             "min": "$mould_min",
#             "max": "$mould_max"
#         },
#         "algae": {
#             "min": "$algae_min",
#             "max": "$algae_max"
#         },
#         "heat_loss": {
#             "min": "$heat_loss_min",
#             "max": "$heat_loss_max"
#         },
#     }
# }])
