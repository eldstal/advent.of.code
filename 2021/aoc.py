
import requests
from bs4 import BeautifulSoup

def get_input(day, cookie=None, cookie_file="cookie.txt", year=2021):

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


def get_test_input(day, cookie=None, cookie_file="cookie.txt", year=2021):

  local_file = f"{year:04}_{day:02}_test.txt"

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

    res = session.get(f"https://adventofcode.com/{year}/day/{day}")

    if res.status_code != 200:
      raise RuntimeError("Failed to get input")

    html = BeautifulSoup(res.text, "html.parser")

    blocks = [ ]
    for block in html.find_all("code"):
      txt = block.text
      n_lines = len(txt.split("\n"))
      blocks.append( (n_lines, txt) )

    #print(blocks)

    raw_data = ""
    try:
      n_lines,raw_data = sorted(blocks, key=lambda t: t[0])[-1]
      print(f"Best effort at locating test data: {n_lines} lines.")
    except:
      return None,None

    open(local_file, "w+").write(raw_data)


  # Most of the input is text files meant to be read row by row
  lines = [ l.strip() for l in raw_data.split("\n") if len(l.strip()) > 0 ]

  return raw_data, lines

# Returns (Success, message)
def post_result(day, part, value, cookie=None, cookie_file="cookie.txt", year=2021):

    if cookie is None and cookie_file is not None:
      cookie=open(cookie_file, "r").read().strip()

    if cookie is None:
      raise RuntimeError("No authentication session cookie provided. Set cookie_file= or something.")
    session = requests.Session()
    session.cookies.set("session", cookie)

    res = session.post(f"https://adventofcode.com/{year}/day/{day}/answer", data={ "level": part, "answer": value} )

    if res.status_code != 200:
      raise RuntimeError("Failed to post answer")

    html = BeautifulSoup(res.text, "html.parser")

    msg = html.find("article").text

    if "not the right answer" in msg: return False, msg.split(".")[0] + "."
    if "have to wait" in msg: return False, msg.split("[")[0]
    if "That's the right answer!" in msg: return True, msg.split("[")[0]

    return False, msg

