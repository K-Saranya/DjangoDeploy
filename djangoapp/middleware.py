# myapp/middleware.py

class SimpleMiddleware:
    def __init__(self, get_response):
        # Runs only once when the server starts
        self.get_response = get_response

    def __call__(self, request):
        # 👉 Code that runs before the view
        print("➡️ Before the view is called")
        # Call the next middleware / view
        response = self.get_response(request)

        # 👉 Code that runs after the view
        print("⬅️ After the view is called")

        return response
