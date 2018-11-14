import random
grammar = """
sentence = adj noun verb adv noun2
adj = adj_single 的 adj_single 的 | null
adj_single = 漂亮  | 蓝色 | 好看
adv = 安静地 | 静静
noun = 猫 | 女人 | 男人
verb = adv 看着 | adv 坐着 
noun2 = 桌子 | 皮球 
"""
#print(grammar)
#
def adj(): return random.choice('漂亮|蓝色|好看'.split("|") )
def noun():return random.choice('猫|女人|男人'.split('|'))
def verb():return random.choice('看着|坐着'.split('|'))
def noun2():return random.choice('桌子|皮球'.split('|'))
def sentence():return "".join([adj(),noun(),verb(),noun2()])
print(sentence())

#定义语法创建函数：从语法内容中读取语法规则并映射到创建的字典，键值为声明，值为表达式
def build_grammar(grammar_str, split='='):
    grammar_pattern = {}
    for line in grammar_str.split('\n'):
        if not line: continue
        stmt, expr = line.split(split)
        grammar_pattern[stmt.strip()] = [e.split() for e in expr.split('|')]
    return grammar_pattern
grammar_pattern = build_grammar(grammar)

print(grammar_pattern)

def generate(grammar_pattern, target):
	if target not in grammar_pattern: return target

	expr = random.choice(grammar_pattern[target])

	tokens = [generate(grammar_pattern, e) for e in expr]  # 递归调用自己，直到表达式中不含有已声明内容

	return ''.join([t for t in tokens if t != 'null'])
print(generate(grammar_pattern, 'sentence'))

