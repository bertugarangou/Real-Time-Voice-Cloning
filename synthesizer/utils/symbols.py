"""
Defines the set of symbols used in text input to the model.

The default here is adapted for Catalan, including accented characters and punctuation.
"""

_pad        = "_"
_eos        = "~"

# Catalan letters, accents, and punctuation
_characters = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            # Uppercase
    "abcdefghijklmnopqrstuvwxyz"            # Lowercase
    "àèéíïòóúüç"                            # Accented Catalan letters
    "ÀÈÉÍÏÒÓÚÜÇ"                            # Uppercase accents (optional)
    "!\'\"(),-.:;?¡¿·"                      # Punctuation including Spanish-style
    " "                                     # Space
)

# Final list of symbols used by the model
symbols = [_pad, _eos] + list(_characters)