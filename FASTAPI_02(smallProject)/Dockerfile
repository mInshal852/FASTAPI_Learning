FROM python:3.12-slim

WORKDIR /app
# here ".(dot) means copying to current directory"
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY main.py main.py
COPY patients.json patients.json
COPY projectinfo projectinfo
COPY images images
# COPY myenv myenv(it should not be copied becuase we are also making a new enviorment.)
COPY setup.txt setup.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8005"]

# ---------------------------------------
#     # imp info:
#         Bro, `--host` and `--port` are just **command-line options** that you pass to Uvicorn.

# For example:

# ```bash
# uvicorn main:app --host 0.0.0.0 --port 8000
# ```

# means:

# * `--host 0.0.0.0` → Which network interface should listen for requests?
# * `--port 8000` → Which port number should listen for requests?

# ---

# ### Host

# ```bash
# --host 0.0.0.0
# ```

# means:

# > Accept connections from outside the container/machine.

# Examples:

# ```bash
# --host 127.0.0.1
# ```

# Only local machine can access.

# ```bash
# --host 0.0.0.0
# ```

# Everyone who can reach the machine can access.

# ---

# ### Port

# ```bash
# --port 8000
# ```

# means:

# > Listen on port 8000.

# Then your URL becomes:

# ```text
# http://localhost:8000
# ```

# If you use:

# ```bash
# --port 5000
# ```

# then:

# ```text
# http://localhost:5000
# ```

# ---

# ### Docker CMD form

# ```dockerfile
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# ```

# Think of it as:

# ```python
# [
#     "uvicorn",
#     "main:app",
#     "--host",
#     "0.0.0.0",
#     "--port",
#     "8000"
# ]
# ```

# Every item in the list is a separate argument.

# Docker runs:

# ```bash
# uvicorn main:app --host 0.0.0.0 --port 8000
# ```

# for you automatically.

# ### Easy memory trick

# * `host` = **where to listen**
# * `port` = **which door number to listen on**

# So:

# ```bash
# uvicorn main:app --host 0.0.0.0 --port 8000
# ```

# means:

# > "Start my FastAPI app, listen on all network interfaces, and use door number 8000."
