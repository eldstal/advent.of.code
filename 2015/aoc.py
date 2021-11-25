
import requests

def get_input(day, cookie=None, cookie_file="cookie.txt", year=2015):

  local_file = f"{year:04}_{day:02}.txt"

  raw_data = None

  # Locally cached copy
  try:
    raw_data = open(local_file, "r").read()
  except:
    pass

  # No local copy available. Download and cache it.
  if raw_data is None:
    if cookie is None and cookie_file is not None:
      cookie=open(cookie_file, "r").read().strip()

    if cookie is None:
      raise RuntimeError("No authentication session cookie provided. Set cookie_file= or something.")
    session = requests.Session()
    session.cookies.set("session", cookie)

    res = session.get(f"https://adventofcode.com/{year}/day/{day}/input")

    if res.status_code != 200:
      raise RuntimeError("Failed to get input")

    raw_data = res.text
    open(local_file, "w+").write(raw_data)


  # Most of the input is text files meant to be read row by row
  lines = [ l.strip() for l in raw_data.split("\n") if len(l.strip()) > 0 ]

  return raw_data, lines
