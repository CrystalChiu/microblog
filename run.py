# This import statement means: go into the app folder (the first app) and
# import the variable app (defined in line 4 of __init__.py).
# Note that python detects and runs all __init__.py files, so you don't have
# to explicitly call it.
from app import app

# This line starts the app. Then you can visit 'localhost:5000' or
# 'http://127.0.0.1:5000/'
# Press control + c to quit
app.run(debug=True)
