import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CharacterProfiles.models import CharacterProfile


# Create your views here.
@csrf_exempt
def addprofile(request: HttpRequest):
    if request.method == "POST":
        content = json.loads(request.body)
        character = CharacterProfile(
            name=content["name"],
            date_of_birth=content["date_of_birth"],
            age=content["age"],
            email=content["email"],
        )

        character.save()

        return JsonResponse({})

    response = JsonResponse({})
    response.status_code = 400

    return response


@csrf_exempt
def getprofiles(request: HttpRequest):
    if request.method == "GET":
        if len(request.META["QUERY_STRING"]) > 0:
            profile_id = request.META["QUERY_STRING"][10:]
            profile = CharacterProfile.objects.get(id=int(profile_id))

            return JsonResponse(
                {
                    "id": profile.id,
                    "name": profile.name,
                    "date of birth": profile.date_of_birth,
                    "age": profile.age,
                    "email": profile.email,
                }
            )
        else:
            all_profiles = {"profiles": []}
            for profile in CharacterProfile.objects.all():

                all_profiles["profiles"].append(
                    {
                        "id": profile.id,
                        "name": profile.name,
                        "date of birth": profile.date_of_birth,
                        "age": profile.age,
                        "email": profile.email,
                    }
                )

            return JsonResponse(all_profiles)


@csrf_exempt
def editprofile(request: HttpRequest):
    if request.method == "PUT":
        content = json.loads(request.body)
        profile = CharacterProfile.objects.get(id=int(content["id"]))

        profile.name = content["name"]
        profile.age = content["age"]
        profile.date_of_birth = content["date_of_birth"]
        profile.email = content["email"]
        profile.save()

        return JsonResponse({})

    response = JsonResponse({})
    response.status_code = 400
    return response


@csrf_exempt
def deleteprofile(request: HttpRequest):
    if request.method == "DELETE":
        content = json.loads(request.body)
        profile = CharacterProfile.objects.get(id=int(content["id"]))

        profile.delete()

        return JsonResponse({})

    response = JsonResponse({})
    response.status_code = 400
    return response
