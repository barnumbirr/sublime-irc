# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [2.0.0] - 2026-03-27

### Added
- Auto-detection of IRC log files via `first_line_match`
- Multi-format support: weechat (`-->`, `<--`, `--`), HexChat/mIRC (`*`), ZNC/Snak (`***`) event markers
- HexChat named-month timestamp format (`Mar 27 12:34:56`)
- Parenthesized timestamp format (`(12:34)`, `(12:34:56)`)
- ZNC bouncer event keywords (`Joins:`, `Parts:`, `Quits:`)
- ISO date-time with `T` separator and `/` date separators
- Nested contexts for layered highlighting (URLs/channels within event lines)
- Syntax test files for irssi, weechat, HexChat, mIRC, and edge cases
- Example log files for irssi, weechat, HexChat, mIRC, ZNC, and Snak formats
- Python plugin for auto-detection of IRC logs in `.txt` and `.log` files
- GitHub Actions CI pipeline with YAML validation and syntax tests

### Changed
- Remapped scopes from `comment.line` hack to semantic scopes for proper multi-color highlighting
- Channel regex now uses two capture groups for prefix and name
- Timestamp regex rewritten with strict bracket pairing (alternation-based)
- URL regex excludes common trailing punctuation (`)`, `]`, `}`, `>`, `,`, `"`, `'`)
- Event patterns use specific character classes instead of `\S+` where applicable
- Scope naming aligned with Sublime Text conventions (meta.date, punctuation.section, punctuation.separator.date, etc.)

### Fixed
- Dead `\b\B` regex that could never match (removed)
- Channel captures referenced non-existent second capture group
- Nickname regex excluded single-character nicks (`{1,31}` → `{0,31}`)
- Timestamp regex allowed mismatched brackets (`[12:34` or `12:34]`)
- Quit message highlighting now handles both `[reason]` (irssi) and `(reason)` (weechat) formats

## [1.0.1] - 2021-07-20

### Fixed
- Removed file extension detection ([see wbond/package_control_channel#8302](https://github.com/wbond/package_control_channel/pull/8302))

## [1.0.0] - 2021-05-27

Initial release.
