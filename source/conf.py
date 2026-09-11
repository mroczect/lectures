# -- Path setup --------------------------------------------------------------
from datetime import date

project = "lectures"
copyright = f"{date.today().year}, mroczect"
author = "mroczect"

version = "0.0.1"
release = "0.0.1"


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.duration",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.linkcode",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

root_doc = "index"

language = "en"

pygments_style = "sphinx"

highlight_language = "python"

rst_prolog = """
.. |proyek| replace:: lectures
"""

html_theme = "sphinx_book_theme"


html_theme_options = {
    "repository_url": "https://github.com/mroczect/lectures",
    "repository_branch": "master",
    "path_to_docs": "source",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_download_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "max_navbar_depth": 4,
    "collapse_navbar": False,
    "extra_footer": "",
    "toc_title": "Contents",
}

html_static_path = ["_static"]

html_title = f"{project} v{release} Documentation"

html_short_title = "Docs"

html_baseurl = ""

html_css_files = []
html_js_files = []

# html_sidebars = {
#     '**': [
#         'navbar-logo.html',
#         'icon-links.html',
#         'search-button-field.html',
#         'sbt-sidebar-nav.html',
#         'sbt-sidebar-footer.html',
#     ]
# }

html_show_sourcelink = True

html_copy_source = True

html_show_sphinx = True

html_last_updated_fmt = "%b %d, %Y"

html_css_files = ["custom.css"]
latex_engine = "xelatex"

latex_documents = [
    (root_doc, "lectures.tex", "Dokumentasi Kuliah", author, "manual"),
]

latex_logo = ""

latex_theme = "manual"

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
}


man_pages = [(root_doc, "lectures", "Dokumentasi Kuliah", [author], 1)]


texinfo_documents = [
    (
        root_doc,
        "lectures",
        "Dokumentasi Kuliah",
        author,
        "lectures",
        "Catatan kuliah dan materi.",
        "Miscellaneous",
    ),
]


epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright


linkcheck_ignore = [r"http://localhost:\d+"]
linkcheck_timeout = 10
linkcheck_retries = 2


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}


autodoc_member_order = "bysource"
autodoc_typehints = "description"


autosummary_generate = True


autosectionlabel_prefix_document = True


extlinks = {
    "issue": ("https://github.com/mroczect/lectures/issues/%s", "issue #%s"),
    "pr": ("https://github.com/mroczect/lectures/pull/%s", "PR #%s"),
}


graphviz_output_format = "svg"


inheritance_graph_attrs = dict(rankdir="TB", size='"8.0, 12.0"', fontsize=14)


todo_include_todos = True


math_number_all = True


nitpicky = True
nitpick_ignore = [
    ("py:class", "optional"),
]


smartquotes = True
smartquotes_action = "qDe"


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"https://github.com/mroczect/lectures/blob/master/{filename}.py"
