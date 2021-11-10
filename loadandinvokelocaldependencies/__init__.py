import logging
import azure.functions as func
import json


def loadandreadlocal():
    try:
        with open("./dependencies/dependencies.json") as f:
            jsondata = json.load(f)
            return jsondata
    except Exception as e:
        return {"Status": "Failed", "ErrorMessage": str(e)}


def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info("Python HTTP trigger function processed a request.")
    loadlocalflag = req.params.get("loadlocal")
    if not loadlocalflag:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            loadlocalflag = req_body.get("loadlocalflag")

    if loadlocalflag:
        response = loadandreadlocal()
        """
        return func.HttpResponse(
            f"Hello, {loadlocalflag}. This HTTP triggered function executed successfully."
        )
        """
        return func.HttpResponse(
            json.dumps(response), mimetype="application/json", status_code=200
        )

    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a parameter loadlocal in the query string or in the request body to load local dependencies.",
            status_code=200,
        )
