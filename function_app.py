import json

import azure.functions as func

from aqi import kategori_pm25

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="kategori", methods=["GET"])
def kategori(req: func.HttpRequest) -> func.HttpResponse:
    nilai = req.params.get("pm25")
    if nilai is None:
        return func.HttpResponse("Parameter pm25 wajib, contoh: ?pm25=60", status_code=400)
    try:
        hasil = kategori_pm25(float(nilai))
    except ValueError as e:
        return func.HttpResponse(str(e), status_code=400)
    body = json.dumps({"pm25": float(nilai), "kategori": hasil})
    return func.HttpResponse(body, mimetype="application/json")