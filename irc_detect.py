import re

import sublime
import sublime_plugin

_IRC_PATTERN = re.compile(
    r"^\[?\d{4}[-/]\d{2}[-/]\d{2}[\sT]\d{2}:\d{2}"
    r"|^\[?\d{2}:\d{2}(?::\d{2})?:?\]?\s+(?:[<*]|-!-|===|-->|\*{3})"
    r"|^\(\d{2}:\d{2}(?::\d{2})?\)\s+[<*]"
    r"|^[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}"
    r"|^---\s+Log\s+opened"
    r"|^Session\s+Start:"
    r"|^\*{4}\s+BEGIN\s+LOGGING"
)

_SYNTAX_PATH = "Packages/IRC Syntax/Syntaxes/IRC.sublime-syntax"
_ST4 = None


def _is_st4():
    global _ST4
    if _ST4 is None:
        _ST4 = int(sublime.version()) >= 4000
    return _ST4


def _is_plain_text(view):
    if _is_st4():
        syntax = view.syntax()
        return syntax is not None and syntax.scope == "text.plain"
    return "Plain text" in view.settings().get("syntax", "")


def _set_syntax(view, path):
    if _is_st4():
        view.assign_syntax(path)
    else:
        view.set_syntax_file(path)


class IrcSyntaxDetector(sublime_plugin.EventListener):
    def on_load_async(self, view):
        if not _is_plain_text(view):
            return

        content = view.substr(sublime.Region(0, min(view.size(), 8192)))
        for line in content.split("\n")[:20]:
            if _IRC_PATTERN.match(line):
                _set_syntax(view, _SYNTAX_PATH)
                return
