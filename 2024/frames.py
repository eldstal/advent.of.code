from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Header, Footer, Label, Static, ProgressBar


class AdventApp(App):

  #DEFAULT_CSS = """
  #  #rightside {
  #    width: 20%;
  #    height: 100%;
  #    dock: right;
  #  }
  #"""

  CSS_PATH = "frames_v1.tcss"

  def compose(self) -> ComposeResult:
    #yield Header()
    with Horizontal(id="top"):
      with Static(id="mainpane"):
        yield Label("Here's your content")

      with Vertical(id="rightside"):
        yield Label("I've got some text for you")

    with Container(id="bottom"):
      yield ProgressBar(id="progress_bar", show_eta=False)
      #yield Label(id="progress_label")

    #yield Footer()

  def progress(self, heading, step, max_step):
    pane = self.query_one("#bottom")
    pane.border_title = heading

    bar = self.query_one("#progress_bar")
    bar.update(progress=step, total=max_step)

