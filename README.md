# vd-nushell-completions

## Nushell parameters and flags completions for VD

## Install and use

```nushell
git clone https://github.com/maxim-uvarov/vd-nushell-completions
source vd-nushell-completions/vd_nushell_completions.nu
```

## About

I asked the GPT4 to parse a Visidata man file (`source/vd_COMMANDLINE_OPTIONS.roff`). After several attempts GPT4 succeded in parsing data correctly enough (`source/parsed_options_final.json`). It provided a python script used for parsing (`source/parsing_vd_help.py`).

Afterwards I wrote a nushell script to create nushell completions file (`source/compose_completions.nu`).
