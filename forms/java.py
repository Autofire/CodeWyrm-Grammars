from dragonfly import (Grammar,
                       MappingRule, CompoundRule, RuleRef,
                       Dictation, Key, Text, Function)
from base.vim import wrapped_insert, insert, Text
from base import fluid

print("Loading grammar: java")

special_rule = MappingRule(
	name = "java special",
	mapping = {
		"print line": Function(wrapped_insert, start="System.out.println(", end = ");"),
		},
	extras = [

		],
)


kw_rules = {}

keywords = [
	"true", "false",
	"import", "package",
	"class", "enum", "interface",
	"const", "final", "static",
	"private", "protected", "public",
	"for", "while", "if", "else", "switch",
	"this", "this", "new", "return",
	"throw", "throws", "volatile", "catch", "finally",
	"null", "true", "false",
]
for keyword in keywords:
	kw_rules[keyword] = Text(keyword)
kw_rules["instance of"] = Text("instanceof")
kw_rules["GL"] = Text("gl")
kw_rules["none"] = Text("null")

types = [
	"byte", "short", "int", "long",
	"float", "double",
	"boolean", "char",
	"void",

	"Vector3f",
]
for t in types:
	kw_rules["data " + t] = Text(t)
kw_rules["data integer"] = Text("int")
kw_rules["data (character|care)"] = Text("char")

boxed_types = [
	"Byte", "Short", "Integer", "Long",
	"Float", "Double",
	"Boolean", "Character"
]
for t in boxed_types:
	kw_rules["boxed " + t] = Text(t)
kw_rules["boxed care"] = Text("Character")
kw_rules["boxed int"] = Text("Integer")


keyword_rule = MappingRule( name = "java keywords", mapping = kw_rules )


def build_grammar(context):
	grammar = Grammar("java", context=(context))
	#grammar.add_rule(keyword_rule)  
	grammar.add_rule(special_rule)
	grammar.add_rule(fluid.build_rule(RuleRef(rule=keyword_rule)))  
	return grammar
