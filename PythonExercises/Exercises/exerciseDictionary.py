# user = {
#     "DNI" : "1003178092",
#     "name" : "Luis",
#     "lastName" : "Campillo",
#     "age" : 23,
#     "e-mail" : "lgcampillo19@gmail.com",
#     "address" : "CRA 26 #56 - 20",
#     "favoriteFood" : "Espaguetis",
#     "skill" : "Desarrollador"
# }


# for key, value in user.items():
#     print(f"{key}: {value}")



animals = ["cat", "dog", "fish", "bird"]

def showpriandlast(cosas):

    firsts = cosas[0]
    lasts = cosas[-1]
    return firsts, lasts


showpriandlast(animals)