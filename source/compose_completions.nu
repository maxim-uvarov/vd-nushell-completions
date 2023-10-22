let $types = {str: string, bool: null, NoneType: null, Path: path, dict: string}

open parsed_options_final.json 
| upsert type {|i| $types  | get -i ($i.type  | default 'bool')} 
| each {|i| (char tab) + $i.long + (if $i.type? != null {$': ($i.type)'} else {''}) + (char tab) + '# ' + $i.description} 
| str join (char nl) 
| 'export extern "vd" [' + (char nl) + $in + (char nl) + ']' 
| save -f ../vd_nushell_completions.nu

