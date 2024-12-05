from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.reactive import reactive
from textual.theme import Theme
from textual.widget import Widget
from textual.widgets import Header, Footer, Label, Static, ProgressBar

# Pinewood surprise
pwood="#0e330a"
# Norway spruce
nspruce="#1e431a"
# Sprouts green:
sgreen="#829a46"
# Mince pie pastry:
mpie="#eed1a5"
# Ho, Ho, Ho red:
hohoho="#b0261b"
# Mulled Spice:
mspice="#5d1c24"
# Pudding Brown:
pudding="#330f11"

advent_theme = Theme(
  name="advent",
  primary=sgreen,
  secondary=mpie,
  accent=hohoho,
  foreground=mpie,
  background="#000000",
  success="#A3BE8C",
  warning=hohoho,
  error="#BF616A",
  surface=pwood,
  panel=nspruce,
  dark=True,
  variables={
    "block-cursor-text-style": "none",
    "footer-key-foreground": "#88C0D0",
    "input-selection-background": "#81a1c1 35%",
  },
)


class AdventApp(App):

  # Each is a text id
  progress_ids = []

  # Key is text id, value is (heading, step, total)
  progress_bars = {}

  CSS_PATH = "frames_v1.tcss"

  def on_mount(self) -> None:
    self.register_theme(advent_theme)
    self.theme = "advent"

  def compose(self) -> ComposeResult:
    #yield Header()
    with Horizontal(id="top"):
      with Static(id="mainpane"):
        yield Label("Here's your content")

      with Vertical(id="rightside"):
        yield Label("I've got some text for you")

    with Container(id="bottom"):
      for i in self.progress_ids:
        heading, step,total = self.progress_bars[i]
        with Horizontal(classes="progress_row"):
          yield Label(heading, classes="progress_label")
          b = ProgressBar(id=i, classes="bottom_progress", show_eta=False, total=total)
          b.update(progress=step)
          yield b

    #yield Footer()

  def progress(self, bar_id, heading, step, count):
    #pane = self.query_one("#bottom")
    #pane.border_title = heading

    self.progress_bars[bar_id] = (heading, step+1, count)

    if bar_id not in self.progress_ids:
      self.progress_ids += [ bar_id ]

      self.refresh(recompose=True)
    else:
      bar = self.query_one(f"#{bar_id}")
      bar.update(progress=step+1, total=count)

