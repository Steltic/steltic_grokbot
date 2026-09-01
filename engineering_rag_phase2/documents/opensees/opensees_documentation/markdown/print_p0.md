<!-- chunk_id: print_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/print.html",
 "title": "print Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "print",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/print.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 985,
 "word_count": 166,
 "has_code": false,
 "has_table": false
} -->

## print Command

This command is used to print output to screen or file. There are a number of

To print all objects of the domain to a file

..function:: print <-JSON> <-file $fileName>

To print all objects of the domain to a JSON file:

**print -JSON -file $fileName**

To print node information:

**print <-file $fileName> -node <-flag $flag> <$node1 $node2 ...>**

To print element information:

**print <-file $fileName> -ele <-flag $flag> <$ele1 $ele2 ...>**

> $fileName    (optional) name of file to which data will be sent. overwrites existing file. default is to print to stderr)
> $flag             integer flag to be sent to the print() method, depending on the node and element type (optional)
> $node1 $node2 ..     (optional) integer tags of nodes to be printed. default is to print all.
> $ele1 $ele2 ..            (optional) integer tags of elements to be printed. default is to print all.

EXAMPLE:

print -ele; # print all elements

print -node 1 2 3; # print data for nodes 1,2 & 3
