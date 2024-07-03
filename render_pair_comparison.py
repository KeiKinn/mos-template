"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment
from utils import QuestionGenerator_PMOS as QuestionGenerator


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("pair_comparison.html.jinja2")

    html = template.render(
        page_title="Emotion Perception Experiment Form 1", 
        form_id=1,
        type="s-MOS",
        questions = QuestionGenerator("filelist/s-mos.csv").questions
    )

    with open("rendered_pair_comparison.html", "w") as f:
        f.write(html)
        print("Done!")


if __name__ == "__main__":
    main()