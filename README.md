# vd-nushell-completions

## Nushell parameters and flags completions for VisiData

![vd-completions3](https://github.com/maxim-uvarov/vd-nushell-completions/assets/4896754/56bd1846-afea-4128-85d4-e9f2dbbba461)

## Install and use

```nushell
git clone https://github.com/maxim-uvarov/vd-nushell-completions
source vd-nushell-completions/vd_nushell_completions.nu
```

## About

I asked the GPT4 to parse a Visidata man file (`source/vd_COMMANDLINE_OPTIONS.roff`). After several attempts GPT4 succeded in parsing data correctly enough (`source/parsed_options_final.json`). It provided a python script used for parsing (`source/parsing_vd_help.py`).

Afterwards I wrote a nushell script to create nushell completions file (`source/compose_completions.nu`). And here we are: Nushell completions for flags and options of VD  (`vd_nushell_completions.nu`)
