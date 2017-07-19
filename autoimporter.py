#!/usr/bin/env python3
import codecs
import io
import pkgutil
import sys
import tokenize

utf8 = codecs.lookup("utf-8")
module_names = {module.name for module in pkgutil.iter_modules()}
module_names |= set(sys.builtin_module_names)


def _tokenize_string(text):
    return tokenize.tokenize(io.BytesIO(text.encode("utf-8")).readline)


def encode(text, errors="strict"):
    return utf8.encode(text, errors)


def decode(data, errors="strict"):
    text, bytes_used = utf8.decode(data, errors)
    text_lines = text.splitlines()
    import_lines = []

    for line in text_lines:
        if line.strip().startswith("#"):
            continue

        for token in _tokenize_string(line):
            if token.type == tokenize.NAME and token.string in module_names:
                import_lines.append("import " + token.string)

    return "\n".join(import_lines + text_lines), bytes_used


codecs.register(
    {"autoimport": codecs.CodecInfo(encode, decode, name="autoimport")}.get
)
