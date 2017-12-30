from sanic import Sanic, Blueprint
from sanic.response import text, json

app = Sanic()

passing_bp= Blueprint('passing_blueprint')
failing_bp = Blueprint('failing_blueprint', url_prefix='/api/failing')


@passing_bp.get("/api/passing")
async def get_data(request):
    return json({
        "hello": "world",
        "I am working if": "you see me",
        "from": "the passing blueprint"
    })


@passing_bp.post("/api/passing")
async def post_data(request):
    return text("POST [PASSING] - {}\n\n{}".format(
        request.headers, request.body
    ))


@failing_bp.get("/")
async def get_data(request):
    return json({
        "hello": "world",
        "I am working if": "you see me",
        "from": "the failing blueprint"
    })


"""
This is the part that is failing
"""
@failing_bp.post("/")
async def post_data(request):
    return text("POST [FAILING] - {}\n\n{}".format(
        request.headers,
        request.body
    ))

if __name__ == "__main__":
    app.blueprint(passing_bp)
    app.blueprint(failing_bp)

    app.run(debug=True, host="0.0.0.0", port=8000)
