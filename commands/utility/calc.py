import ast
import operator as op
import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']

_ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("Expression non autorisee.")


async def setup(bot):
    @bot.command()
    async def calc(ctx, *, expression: str):
        if len(expression) > 120:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Calc]({WEBSITE})**
{THEME} Expression trop longue (max 120 caracteres).""")
            return

        try:
            tree = ast.parse(expression, mode='eval')
            result = _safe_eval(tree)
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Calc]({WEBSITE})**
{THEME} `{expression}` = **{result}**""")
        except Exception:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Calc]({WEBSITE})**
{THEME} Expression invalide. Exemple: `2*(10+5)`""")
