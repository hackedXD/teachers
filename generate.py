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



    html = ""
    temp_html = """
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
        html += temp_html.format(
            image=teacher["photo"],
            email=teacher["email"],
            room=room,
        )

    print(html)

