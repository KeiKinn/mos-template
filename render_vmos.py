#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment
from utils import QuestionGenerator_FMOS as QuestionGenerator


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("vmos.html.jinja2")

    html = template.render(
        page_title="MOS Experiment Form 1",
        form_id=1,
        type="v-MOS",
        questions = QuestionGenerator("filelist/filelist.csv").questions
    )
    # write html into file
    with open("rendered_mos.html", "w") as f:
        f.write(html)
        print("Done!")


if __name__ == "__main__":
    main()