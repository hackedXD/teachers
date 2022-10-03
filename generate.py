import json
from re import template

def sortKey(value):
    global priority_dict
    try:
        if value["room"][0] in priority_dict.keys():
            return priority_dict.get(value["room"][0])
        else:
            return priority_dict.get('default')
    except KeyError:
        return priority_dict.get('default')
if __name__ == "__main__":
    with open("hsteachers.json") as f:
        data = json.load(f)
    
    # priority = ["H", "S", "default"]
    priority_dict = {
        "H": 1,
        "S": 2,
        "default": 3
    }

    data = sorted(data, key=sortKey)



    cards = ""
    temp_html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Bootstrap demo</title>
            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
                rel="stylesheet"
                integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi"
                crossorigin="anonymous"
            />
        </head>
        <body>
            <div class="container text-center">
                <div class="row row-cols-4">
                {cards}
                </div>
            </div>

            <script
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3"
                crossorigin="anonymous"
            ></script>
        </body>
    </html>
    """
    temp_card = """
        <div class="col">
            <div class="card my-3">
                <img
                    src="{image}"
                    class="card-img-top"
                />
                <div class="card-body">
                    <h6 class="card-text">Email: {email}<br />Room: {room}</h6>
                </div>
            </div>
        </div>
    """
    for teacher in data:
        try:
            room = teacher["room"]
        except:
            room = "N/A"
        cards += temp_card.format(
            image=teacher["photo"],
            email=teacher["email"],
            room=room,
        )

    with open("index.html", "w") as f:
        f.write(temp_html.format(cards=cards))

